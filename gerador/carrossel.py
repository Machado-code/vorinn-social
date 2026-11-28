"""Carrosséis 1080x1350: ficha YAML com blocos -> slides no visual aprovado -> PNGs + legenda + prévia."""
import importlib.util
import pathlib
import tempfile

from . import comum
from .comum import ErroFicha, esc

# Reaproveita o CSS e a moldura (topo, rodapé, marca d'água) do scripts/render.py do lote 1.
_spec = importlib.util.spec_from_file_location("render_lote1", comum.ROOT / "scripts" / "render.py")
import sys as _sys
_sys.path.insert(0, str(comum.ROOT / "scripts"))
_render = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_render)

MARGEM = {"selo": "", "titulo": "mt32", "h1": "mt32", "h2": "mt32", "texto": "mt32", "grande": "mt40", "lista": "mt48",
          "cartoes": "mt48", "passos": "mt48", "tela": "mt56", "cta": "mt56", "nota": "mt24"}
CHAVES = set(MARGEM) | {"monograma", "lado_a_lado"}


def _uri(rel):
    return comum.caminho_asset(rel).as_uri()


def _marca(texto, b):
    t = comum.marcar(texto, '<span class="acc">', "</span>") if b == "v" else comum.marcar(texto, "<em>", "</em>")
    return t.strip().replace("\n", "<br>")


def _bloco(chave, valor, b, i_slide, primeiro, slide):
    mt = "" if primeiro else MARGEM.get(chave, "")
    cls = lambda base: f'{base} {mt}'.strip()
    if chave == "selo":
        return f'<div class="{cls("pill" if b == "v" else "eyebrow")}">{esc(valor)}</div>'
    if chave in ("titulo", "h1", "h2"):
        tag = chave if chave != "titulo" else ("h1" if i_slide == 0 else "h2")
        return f'<{tag} class="{mt}">{_marca(valor, b)}</{tag}>'
    if chave == "texto":
        vs = valor if isinstance(valor, list) else [valor]
        return "".join(f'<p class="{cls("lead") if k == 0 else "lead mt24"}">{_marca(v, b)}</p>' for k, v in enumerate(vs))
    if chave == "grande":
        return f'<p class="{cls("big")}">{_marca(valor, b)}</p>'
    if chave == "nota":
        return f'<p class="{cls("cta-sub")}">{esc(valor)}</p>'
    if chave == "lista":
        itens = []
        for k, it in enumerate(valor, 1):
            num = f"{k:02d}" if b == "v" else str(k)
            if isinstance(it, dict):
                corpo = f'<h3>{_marca(it.get("titulo", ""), b)}</h3>' + (f'<p>{_marca(it["texto"], b)}</p>' if it.get("texto") else "")
            else:
                corpo = f'<p class="big">{_marca(it, b)}</p>'
            itens.append(f'<div class="item"><div class="num">{num}</div><div>{corpo}</div></div>')
        return f'<div class="{cls("list")}">{"".join(itens)}</div>'
    if chave == "cartoes":
        cards = []
        for k, c in enumerate(valor):
            extra = "" if (slide.get("lado_a_lado") or k == 0) else " mt32"
            cards.append(f'<div class="card{extra}">' + (f'<div class="card-tag">{esc(c["selo"])}</div>' if c.get("selo") else "")
                         + f'<h3>{_marca(c.get("titulo", ""), b)}</h3>' + (f'<p>{_marca(c["texto"], b)}</p>' if c.get("texto") else "") + "</div>")
        if slide.get("lado_a_lado"):
            return f'<div class="{cls("two")}">{"".join(cards)}</div>'
        return f'<div class="{mt}">{"".join(cards)}</div>'
    if chave == "passos":
        return f'<div class="{cls("steps")}">' + "".join(f'<div class="step"><span>{k}</span>{_marca(s, b)}</div>' for k, s in enumerate(valor, 1)) + "</div>"
    if chave == "cta":
        sub = f'<div class="cta-sub">{esc(valor["sub"])}</div>' if valor.get("sub") else ""
        return f'<div class="{cls("cta")}"><div class="btn">{esc(valor["botao"])}</div>{sub}</div>'
    if chave == "tela":
        fmt = valor.get("formato", "larga")
        nota = f'<div class="note">{esc(valor["nota"])}</div>' if valor.get("nota") else ""
        if fmt == "capa":
            return f'<img class="shot shot-cover" src="{_uri(valor["arquivo"])}">{nota}'
        if fmt in ("larga", "corte"):
            return f'<img class="shot shot-{"wide" if fmt == "larga" else "crop"} {mt}" src="{_uri(valor["arquivo"])}">{nota}'
        raise ErroFicha(f"tela.formato '{fmt}': use capa, larga, corte ou celular")
    if chave == "monograma":
        return f'<img class="mono-hero" src="{(comum.ASSETS / "marca" / "vorinn-monograma.png").as_uri()}">' if valor else ""
    if chave == "lado_a_lado":
        return ""
    raise ErroFicha(f"bloco desconhecido '{chave}'. Use: {', '.join(sorted(CHAVES))}")


def miolo(slide, b, i):
    for k in slide:
        if k not in CHAVES:
            raise ErroFicha(f"slide {i + 1}: bloco desconhecido '{k}'. Use: {', '.join(sorted(CHAVES))}")
    tela = slide.get("tela")
    if tela and tela.get("formato") == "celular":
        col, primeiro = [], True
        for k, v in slide.items():
            if k == "tela":
                continue
            h = _bloco(k, v, b, i, primeiro, slide)
            primeiro = primeiro and not h
            col.append(h)
        nota = f'<div class="note">{esc(tela["nota"])}</div>' if tela.get("nota") else ""
        return (f'<div class="row"><div class="col-text">{"".join(col)}</div>'
                f'<div class="phone"><img src="{_uri(tela["arquivo"])}"></div></div>{nota}')
    partes, primeiro = [], True
    for k, v in slide.items():
        h = _bloco(k, v, b, i, primeiro, slide)
        if h and k not in ("monograma", "lado_a_lado"):
            primeiro = False
        partes.append(h)
    return "".join(partes)


JS_CHECAR = """() => {
  const p = [], c = document.querySelector('.content'), cr = c.getBoundingClientRect();
  const solto = e => getComputedStyle(e).position === 'absolute' || e.closest('.shot-cover,.mono-hero,.note');
  [...c.children].forEach(e => { if (solto(e)) return; const r = e.getBoundingClientRect();
    if (r.top < cr.top - 1 || r.bottom > cr.bottom + 1) p.push('o conteúdo passou da altura do slide'); });
  const fora = [];
  c.querySelectorAll('*').forEach(e => {
    if (solto(e) || fora.some(f => f.contains(e))) return;
    const r = e.getBoundingClientRect(); if (!r.width) return;
    const nome = `<${e.tagName.toLowerCase()} class="${e.className}">`;
    if (r.right > 1022) { p.push(`passou da margem direita: ${nome}`); fora.push(e); }
    else if (r.bottom > 1214) { p.push(`encostou no rodapé: ${nome}`); fora.push(e); }
  });
  return [...new Set(p)];
}"""


def gerar(ficha_path, ficha, so_previa=False, quadros=None):
    from playwright.sync_api import sync_playwright
    ficha_path = pathlib.Path(ficha_path).resolve()
    b = ficha.get("marca")
    if b not in ("u", "v"):
        raise ErroFicha("marca: 'u' (Unnar) ou 'v' (Vorinn)")
    slides = ficha.get("slides") or []
    if not 1 <= len(slides) <= 10:
        raise ErroFicha("slides: de 1 a 10")
    saida = pathlib.Path(ficha.get("saida") or ficha_path.with_suffix(""))
    if not saida.is_absolute():
        saida = comum.ROOT / saida
    saida.mkdir(parents=True, exist_ok=True)

    textos = []
    def junta(v, onde):
        if isinstance(v, str): textos.append((onde, v))
        elif isinstance(v, list): [junta(x, onde) for x in v]
        elif isinstance(v, dict): [junta(x, f"{onde}.{k}") for k, x in v.items() if k not in ("arquivo", "formato")]
    for i, s in enumerate(slides):
        junta(s, f"slide {i + 1}")
    if ficha.get("legenda"):
        textos.append(("legenda", ficha["legenda"]))
    avisos = comum.conferir_texto(textos, ficha.get("regras_aceitas") or ())

    post = {"brand": b}
    problemas, pngs = [], []
    with sync_playwright() as p:
        br, pg = comum.abrir(p, 1080, 1350)
        for old in saida.glob("[0-9][0-9].png"):
            old.unlink()
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="gerador-"))
        fontes = ["Inter", "Sora" if b == "v" else "Gelasio"]
        for i, s in enumerate(slides):
            html = _render.page(post, i, len(slides), miolo(s, b, i))
            hp = tmp / f"slide-{i + 1}.html"
            hp.write_text(html, encoding="utf-8")
            pg.goto(hp.as_uri())
            pg.wait_for_load_state("networkidle")
            pg.evaluate("document.fonts.ready")
            if i == 0:
                problemas += [f"fonte não instalada: {f}" for f in pg.evaluate(comum.JS_FONTES, fontes)]
            problemas += [f"slide {i + 1}: arquivo não carregou: {f}" for f in pg.evaluate(comum.JS_IMAGENS)]
            problemas += [f"slide {i + 1}: {x}" for x in pg.evaluate(JS_CHECAR)]
            png = saida / f"{i + 1:02d}.png"
            pg.screenshot(path=str(png))
            pngs.append(png)
        br.close()
    if ficha.get("legenda"):
        (saida / "legenda.md").write_text(ficha["legenda"].strip() + "\n", encoding="utf-8")
    previa = comum.folha_previa(pngs, saida / "previa.jpg", 240, [f"{i + 1}" for i in range(len(pngs))])
    return {"pasta": saida, "pngs": pngs, "previa": previa, "problemas": problemas, "avisos": avisos}
