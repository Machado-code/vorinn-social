"""Reels "Mesa de controle": ficha YAML -> HTML -> vídeo com trilha + prévia + checagens."""
import json
import pathlib
import subprocess
import sys
import tempfile

import jinja2
from PIL import Image

from . import comum
from .comum import ErroFicha, esc

FPS = 30
SLOTS_CX = [-201, -67, 67, 201]          # centro de cada encaixe no mundo 3D
EASE = (.45, 0, .55, 1)                  # mesma curva da câmera no CSS

ICONES = {
    "calendario": '<rect x="9" y="14" width="46" height="40" rx="6"/><path d="M9 26h46M21 8v12M43 8v12"/><path d="M19 36h6M29 36h6M39 36h6M19 45h6M29 45h6"/>',
    "confirmado": '<circle cx="32" cy="32" r="22"/><path d="M21 33l7 7 15-16"/>',
    "checkin": '<path d="M36 10h14a4 4 0 0 1 4 4v36a4 4 0 0 1-4 4H36"/><path d="M10 32h30M30 21l11 11-11 11"/>',
    "despesa": '<circle cx="32" cy="32" r="23"/><text x="32" y="40" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1A1408" stroke="none">R$</text>',
    "sino": '<path d="M18 44V30a14 14 0 0 1 28 0v14l5 6H13z"/><path d="M27 54a5 5 0 0 0 10 0"/>',
    "equipe": '<circle cx="24" cy="24" r="8"/><circle cx="43" cy="26" r="6"/><path d="M10 52c1-9 7-14 14-14s13 5 14 14M38 52c1-7 4-11 9-11s8 4 9 11"/>',
    "painel": '<rect x="9" y="11" width="46" height="42" rx="6"/><path d="M9 23h46M24 23v30"/><path d="M31 33h16M31 42h10"/>',
    "agenda": '<rect x="12" y="10" width="40" height="46" rx="6"/><path d="M20 22h24M20 31h24M20 40h14"/>',
    "camera": '<rect x="8" y="20" width="48" height="32" rx="6"/><path d="M22 20l4-7h12l4 7"/><circle cx="32" cy="36" r="9"/>',
}
SVG = '<svg viewBox="0 0 64 64" fill="none" stroke="#1A1408" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{}</svg>'


# ---------------------------------------------------------------- câmera
def _bezier(t, p1x, p1y, p2x, p2y):
    """Valor y da curva cubic-bezier para um x = t (resolve por Newton + bisseção)."""
    def bx(u): return 3 * (1 - u) ** 2 * u * p1x + 3 * (1 - u) * u ** 2 * p2x + u ** 3
    def by(u): return 3 * (1 - u) ** 2 * u * p1y + 3 * (1 - u) * u ** 2 * p2y + u ** 3
    lo, hi, u = 0.0, 1.0, t
    for _ in range(40):
        x = bx(u)
        if abs(x - t) < 1e-6:
            break
        if x < t: lo = u
        else: hi = u
        u = (lo + hi) / 2
    return by(u)


def camera(tempos):
    """Pontos-chave da câmera (tempo, ty, tz, rx, rz)."""
    t1, t2, dur = tempos["pecas"], tempos["tela"], tempos["total"]
    pts = [(0, -10, 90, 61, 18)]
    if t2 - t1 > 0.3:
        pts.append((t1, 10, 170, 59, 22))
    pts += [(t2, 40, 250, 56, 30), (min(t2 + 0.8, dur), 90, 400, 53, 31), (dur, 90, 400, 53, 31)]
    return pts


def angulos(pts, t):
    for (ta, *va), (tb, *vb) in zip(pts, pts[1:]):
        if ta <= t <= tb:
            p = _bezier((t - ta) / (tb - ta), *EASE) if tb > ta else 1
            rx = va[2] + (vb[2] - va[2]) * p
            rz = va[3] + (vb[3] - va[3]) * p
            return round(rx, 2), round(rz, 2)
    return pts[-1][3], pts[-1][4]


# ---------------------------------------------------------------- ficha -> dados do modelo
def montar(ficha, ficha_path, html_dir):
    if ficha.get("tipo") != "reel-mesa":
        raise ErroFicha("tipo precisa ser reel-mesa")
    pecas = ficha.get("pecas") or []
    if not 1 <= len(pecas) <= 4:
        raise ErroFicha("pecas: de 1 a 4 (um por encaixe)")
    tela = ficha.get("tela") or {}
    if "arquivo" not in tela or not tela.get("frases"):
        raise ErroFicha("tela.arquivo e tela.frases são obrigatórios")

    caps, textos = [], []

    def legenda(frase, t_in, t_fim, onde):
        textos.append((onde, frase))
        ws = []
        k = 0
        for w, kw, colada in comum.palavras(frase):
            ws.append({"texto": esc(w), "kw": kw, "cola": colada, "t": round(t_in + 0.16 * k, 2)})
            k += 0 if colada else 1
        caps.append({"t_out": round(t_fim - 0.2, 2), "words": ws})
        return len(ws)

    # ---- tempos
    t = 0.1
    n = len(comum.palavras(ficha["gancho"]))
    dur_gancho = max(2.4, 0.5 + 0.17 * n + 1.2)
    legenda(ficha["gancho"], 0.1, t + dur_gancho, "gancho")
    t += dur_gancho

    slots = []
    t_pecas = t
    for i in range(4):
        cx = SLOTS_CX[i]
        s = {"n": i + 1, "cx": cx, "left": cx + 216, "estado": "vazia", "pill": None, "t_drop": 0, "t_land": 0}
        if i < len(pecas):
            p = pecas[i]
            estado = p.get("estado", "cai")
            if estado not in ("cai", "encaixada", "vazia"):
                raise ErroFicha(f"pecas[{i}].estado: cai, encaixada ou vazia")
            s["estado"] = estado
            ic = p.get("icone", "painel")
            if ic not in ICONES:
                raise ErroFicha(f"pecas[{i}].icone '{ic}' não existe. Opções: {', '.join(ICONES)}")
            s["icone"] = SVG.format(ICONES[ic])
            textos.append((f"pecas[{i}].nome", p.get("nome", "")))
            if estado == "cai":
                s["t_drop"] = round(t + 0.05, 2)
                s["t_land"] = round(t + 0.5, 2)
                if p.get("frase"):
                    legenda(p["frase"], t + 0.1, t + 2.0, f"pecas[{i}].frase")
                # as etiquetas das pontas puxam para o centro para não sair do quadro com a câmera girando
                s["pill"] = {"texto": esc(p["nome"]), "t_in": round(t + 0.55, 2), "t_out": round(t + 1.95, 2),
                             "dx": [70, 20, -20, -70][i]}
                t += 2.0
        slots.append(s)

    t_tela = round(t, 2)
    frases = tela["frases"]
    dur_tela = max(2.5, 0.2 + 2.3 * len(frases))
    for k, fr in enumerate(frases):
        ini = t_tela + 0.1 + 2.3 * k
        legenda(fr, ini, min(ini + 2.3, t_tela + dur_tela), f"tela.frases[{k}]")
    t_fecho = round(t_tela + dur_tela, 2)
    total = round(t_fecho + 2.7, 2)
    tempos = {"pecas": t_pecas, "tela": t_tela, "fecho": t_fecho, "total": total}

    # ---- câmera e etiquetas viradas para ela
    pts = camera(tempos)
    cam = [{"pct": round(100 * tk / total, 3), "ty": ty, "tz": tz, "rx": rx, "rz": rz} for tk, ty, tz, rx, rz in pts]
    sparks = []
    for s in slots:
        if s["pill"]:
            rx, rz = angulos(pts, s["t_land"])
            s["pill"].update(rx=rx, rz=rz)
            sparks.append([s["cx"], s["t_land"], rz, rx])

    # ---- telas
    arq = comum.caminho_asset(tela["arquivo"])
    a = {"marca": comum.rel_de(html_dir, comum.ASSETS / "marca" / "unnar-marca-fundo-escuro.svg"),
         "vorinn": comum.rel_de(html_dir, comum.ASSETS / "marca" / "vorinn-horizontal.png")}
    console = tela.get("console") or (tela["arquivo"] if arq.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp") else None)
    screen = {"img": comum.rel_de(html_dir, comum.caminho_asset(console)) if console else None,
              "t_flash": round(t_tela + 0.03, 2), "t_img": round(t_tela + 0.15, 2)}
    t_card = round(t_tela + 0.5, 2)
    card = {"t_in": t_card, "rotulo": esc(tela.get("rotulo", "Tela real do Unnar")), "src": comum.rel_de(html_dir, arq), "destaques": []}
    if arq.suffix.lower() in (".mp4", ".webm", ".mov"):
        # vídeo do portal (1080x1920): o corte padrão esconde o cabeçalho com a logo antiga
        cx0, cy0, cw, ch = tela.get("corte", [120, 330, 840, 1208])
        formato = tela.get("formato", "celular")
        if formato not in ("celular", "cartao"):
            raise ErroFicha("tela.formato para vídeo: celular ou cartao")
        borda = 10 if formato == "celular" else 1
        largura = 600 if formato == "celular" else 940
        esc_ = (largura - 2 * borda) / cw
        altura = round(ch * esc_ + 2 * borda)
        if altura > 960:
            raise ErroFicha("tela.corte alto demais para caber acima da legenda; corte menos altura")
        card.update(tipo="video", classe="phone" if formato == "celular" else "card", x=round((1080 - largura) / 2),
                    y=300 if formato == "celular" else 330, w=largura, h=altura, inicio=tela.get("inicio", 0.3),
                    vx=round(-cx0 * esc_, 1), vy=round(-cy0 * esc_, 1), vw=round(1080 * esc_, 1), vh=round(1920 * esc_, 1))
        def fx(d): return (d["x"] - cx0) * esc_
        def fy(d): return (d["y"] - cy0) * esc_
    else:
        iw, ih = Image.open(arq).size
        w = 940
        h = w * ih / iw
        if h > 860:
            h, w = 860, 860 * iw / ih
        x = (1080 - w) / 2
        esc_ = w / iw
        card.update(tipo="imagem", x=round(x), y=330, w=round(w))
        def fx(d): return d["x"] * esc_
        def fy(d): return d["y"] * esc_
    card["tag_x"], card["tag_y"] = card["x"], card["y"] - 68
    k_ = esc_
    for j, d in enumerate(tela.get("destaques") or []):
        pad = 8
        card["destaques"].append({"x": round(fx(d) - pad), "y": round(fy(d) - pad), "w": round(d["w"] * k_ + 2 * pad),
                                  "h": round(d["h"] * k_ + 2 * pad), "r": round(d.get("raio", 999) * k_ if d.get("raio") else 999),
                                  "t": round(t_card + d["aos"], 2) if "aos" in d else round(t_card + 0.75 + 0.25 * j, 2)})

    f = ficha.get("fecho") or {}
    fecho = {"t": t_fecho,
             "linha1": comum.marcar(f.get("linha1", "Gerencie menos."), "<em>", "</em>"),
             "linha2": comum.marcar(f.get("linha2", "*Crie mais.*"), "<em>", "</em>"),
             "botao": esc(f.get("botao", "Conheça o Unnar · link na bio"))}
    textos += [("fecho", f.get("linha1", "")), ("fecho", f.get("linha2", "")), ("fecho", f.get("botao", ""))]
    if ficha.get("legenda"):
        textos.append(("legenda", ficha["legenda"]))

    ticks = [0.1] + [s["t_land"] for s in slots if s["estado"] == "cai"] + [t_tela + 0.03, t_card + 0.05, t_fecho + 0.05, t_fecho + 1.0]
    dados = {"ficha": ficha_path.name, "dur": total, "cam": cam, "slots": slots, "screen": screen, "card": card,
             "caps": caps, "fecho": fecho, "a": a, "sparks": json.dumps(sparks)}
    return dados, tempos, ticks, textos


# ---------------------------------------------------------------- checagens no navegador
JS_CHECAR = """() => {
  const p = [];
  const vis = e => parseFloat(getComputedStyle(e).opacity) > 0.5;
  document.querySelectorAll('.cap').forEach(c => {
    const ws = [...c.querySelectorAll('.w')].filter(vis);
    if (!ws.length || !vis(c)) return;
    const r = c.getBoundingClientRect();
    if (r.height > 180) p.push(`legenda em mais de 2 linhas: "${c.innerText.trim()}"`);
    if (r.bottom > 1500) p.push(`legenda abaixo da área segura: "${c.innerText.trim()}"`);
  });
  document.querySelectorAll('.pill').forEach(e => { if (!vis(e)) return; const r = e.getBoundingClientRect();
    if (r.left < 12 || r.right > 1068 || r.top < 200) p.push(`etiqueta fora do quadro: "${e.innerText.trim()}"`); });
  document.querySelectorAll('.card,.phone').forEach(e => { if (!vis(e)) return; const r = e.getBoundingClientRect();
    if (r.left < 0 || r.right > 1080 || r.top < 180 || r.bottom > 1290) p.push('tela real fora da área segura'); });
  return p;
}"""


def gerar(ficha_path, ficha, so_previa=False, quadros=None):
    from playwright.sync_api import sync_playwright
    ficha_path = pathlib.Path(ficha_path).resolve()
    saida = pathlib.Path(ficha.get("saida") or ficha_path.with_suffix(""))
    if not saida.is_absolute():
        saida = comum.ROOT / saida
    saida.parent.mkdir(parents=True, exist_ok=True)
    html_path = saida.with_suffix(".html")

    dados, tempos, ticks, textos = montar(ficha, ficha_path, html_path.parent)
    avisos = comum.conferir_texto(textos, ficha.get("regras_aceitas") or ())
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(pathlib.Path(__file__).parent / "modelos")), autoescape=False)
    html_path.write_text(env.get_template("reel_mesa.html.j2").render(**dados), encoding="utf-8")

    total = tempos["total"]
    momentos = quadros or [0.6, tempos["pecas"] + 0.9, (tempos["pecas"] + tempos["tela"]) / 2 + 0.6,
                           tempos["tela"] + 1.6, total - 0.6]
    momentos = sorted({round(min(max(m, 0), total - 0.05), 2) for m in momentos})
    # momentos extras só para checar (meio de cada legenda e de cada etiqueta)
    checar_em = sorted(set(momentos) | {round(c["words"][-1]["t"] + 0.45, 2) for c in dados["caps"]}
                       | {round(s["pill"]["t_in"] + 0.5, 2) for s in dados["slots"] if s["pill"]}
                       | {round(s["pill"]["t_out"] - 0.1, 2) for s in dados["slots"] if s["pill"]})
    problemas = []
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="gerador-"))
    with sync_playwright() as p:
        br, pg = comum.abrir(p, 1080, 1920)
        pg.goto(html_path.as_uri())
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.evaluate("window.ready()")
        faltam = pg.evaluate(comum.JS_IMAGENS)
        problemas += [f"arquivo não carregou: {f}" for f in faltam]
        problemas += [f"fonte não instalada: {f}" for f in pg.evaluate(comum.JS_FONTES, ["Inter", "Gelasio"])]
        for t in checar_em:
            pg.evaluate(f"seek({t})")
            problemas += [f"{t:.2f}s: {x}" for x in pg.evaluate(JS_CHECAR)]
        imgs = []
        for t in momentos:
            pg.evaluate(f"seek({t})")
            f = tmp / f"q{t:05.2f}.jpg"
            pg.screenshot(path=str(f), type="jpeg", quality=80)
            imgs.append(f)
        previa = comum.folha_previa(imgs, saida.parent / (saida.name + "-previa.jpg"), 260, [f"{t:.1f}s" for t in momentos])

        mp4 = None
        if not so_previa:
            video_tmp = tmp / "video.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(video_tmp)], stdin=subprocess.PIPE)
            for i in range(int(round(total * FPS))):
                pg.evaluate(f"seek({i / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() != 0:
                raise RuntimeError("ffmpeg falhou ao montar o vídeo")
            audio = tmp / "trilha.wav"
            subprocess.run([sys.executable, str(comum.ROOT / "scripts" / "make_audio.py"), str(audio), str(total),
                            ",".join(f"{x:.2f}" for x in sorted(ticks))], check=True, stdout=subprocess.DEVNULL)
            mp4 = saida.with_suffix(".mp4")
            parcial = saida.parent / (saida.name + ".tmp.mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video_tmp), "-i", str(audio), "-map", "0:v", "-map", "1:a",
                            "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(parcial)], check=True)
            parcial.replace(mp4)
        br.close()
    return {"html": html_path, "mp4": mp4, "previa": previa, "duracao": total, "problemas": problemas, "avisos": avisos}
