"""Peças comuns do gerador: caminhos, navegador, marcação de texto, regras e prévia."""
import html
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"


class ErroFicha(Exception):
    """Erro de preenchimento da ficha (campo faltando, arquivo inexistente...)."""


# ---------------------------------------------------------------- caminhos
def caminho_asset(rel):
    """Aceita 'assets/...' ou só o caminho dentro de assets/. Confere se existe."""
    p = pathlib.Path(rel)
    if not p.is_absolute():
        p = ROOT / rel if str(rel).startswith("assets/") else ASSETS / rel
    if not p.exists():
        raise ErroFicha(f"arquivo não encontrado: {rel}")
    return p


def rel_de(destino_dir, arquivo):
    """Caminho relativo de um arquivo visto da pasta do HTML gerado."""
    return os.path.relpath(arquivo, destino_dir).replace(os.sep, "/")


# ---------------------------------------------------------------- texto
def esc(t):
    return html.escape(str(t), quote=False)


def marcar(texto, abre, fecha):
    """*palavra* vira abre+palavra+fecha; **negrito** vira <strong>. Escapa o resto."""
    t = esc(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", lambda m: abre + m.group(1) + fecha, t)
    return t


def palavras(frase):
    """Divide a frase em (texto, é_chave, colada). *chave* pode ter espaço dentro; a pontuação
    logo depois dela (ex.: *sábado*?) vira um pedaço colado, fora do destaque."""
    out = []
    for m in re.finditer(r"\*([^*]+)\*([^\s*]*)|(\S+)", frase):
        if m.group(1):
            out.append((m.group(1), True, False))
            if m.group(2):
                out.append((m.group(2), False, True))
        else:
            out.append((m.group(3), False, False))
    return out


# ---------------------------------------------------------------- regras de conteúdo
# Saem do PROJETO.md ("O que os textos podem e não podem dizer"). Cada item: (regex, motivo).
REGRAS = [
    ("tempo-real", r"tempo real", "não prometer 'tempo real': o sino atualiza a cada minuto com o Unnar aberto"),
    ("gps", r"\bgps\b|geolocaliza|localiza[çc][ãa]o", "não falar em GPS ou localização"),
    ("prova-presenca", r"prova de presen", "não falar em prova de presença"),
    ("comprovante", r"comprovante|nota fiscal|foto da despesa", "despesa não tem foto nem comprovante"),
    ("reembolso", r"reembols", "o Unnar não faz reembolso"),
    ("aprovacao-despesa", r"aprova(r|[çc][ãa]o|da|do)\b.{0,20}despesa|despesa.{0,30}aprova", "despesa não tem aprovação"),
    ("notificacao", r"notifica[çc][ãa]o (no|pelo) celular|push|com o app fechado", "não prometer notificação no celular com o app fechado"),
    ("app-de-loja", r"app store|play store|loja de apps|baix(e|ar) o app", "o Unnar é web, não é app de loja"),
    ("teste-gratis", r"teste gr[áa]tis|cadastre-se|crie sua conta|per[íi]odo gr[áa]tis", "não há cadastro próprio nem teste grátis"),
    ("orcamento", r"(gera|envia|monta)r? (o |um |seu )?or[çc]amento", "o Unnar não gera nem envia orçamento"),
    ("gravacao", r"grava[çc][ãa]o", "dizer 'tela real', não 'gravação'"),
    ("endereco", r"\brua \w|\bav\. |\bavenida\b|\bcep\b", "não mostrar nem citar endereços"),
    ("gancho-proibido", r"pedi pra ia|comente \w+ que eu|comenta \w+ que eu", "gancho de IA ou pedido de comentário com palavra-chave estão fora"),
]


def conferir_texto(textos, aceitos=()):
    """Devolve avisos (onde, trecho, motivo) para cada regra violada, menos as aceitas na ficha."""
    avisos = []
    for onde, t in textos:
        baixo = str(t).lower()
        for nome, padrao, motivo in REGRAS:
            if nome in aceitos:
                continue
            m = re.search(padrao, baixo)
            if m:
                avisos.append((onde, m.group(0), motivo, nome))
    return avisos


# ---------------------------------------------------------------- navegador
def abrir(p, largura, altura):
    exe = os.environ.get("CHROME_PATH") or ("/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None)
    args = ["--no-sandbox", "--allow-file-access-from-files", "--autoplay-policy=no-user-gesture-required"]
    br = p.chromium.launch(executable_path=exe, args=args) if exe else p.chromium.launch(args=args)
    pg = br.new_page(viewport={"width": largura, "height": altura}, device_scale_factor=1)
    return br, pg


# Confere fontes pela largura do texto (document.fonts.check não serve para fontes do sistema).
JS_FONTES = """(nomes) => {
  const c = document.createElement('canvas').getContext('2d');
  const s = 'Gerencie menos, crie mais 0123456789';
  return nomes.filter(n => {
    c.font = '40px monospace'; const a = c.measureText(s).width;
    c.font = `40px '${n}', monospace`; const b = c.measureText(s).width;
    return Math.abs(a - b) < 0.5;
  });
}"""

JS_IMAGENS = """() => [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src'))
  .concat([...document.querySelectorAll('video')].filter(v => v.readyState < 2).map(v => v.getAttribute('src')))"""


# ---------------------------------------------------------------- prévia
def folha_previa(imagens, saida, largura=300, rotulos=None):
    """Junta as imagens lado a lado numa folha pequena (para conferir gastando pouco)."""
    from PIL import Image, ImageDraw
    ims = [Image.open(i).convert("RGB") for i in imagens]
    if not ims:
        return None
    alt = int(ims[0].height * largura / ims[0].width)
    folha = Image.new("RGB", (len(ims) * (largura + 8) - 8, alt + (26 if rotulos else 0)), (32, 32, 36))
    d = ImageDraw.Draw(folha)
    for k, im in enumerate(ims):
        folha.paste(im.resize((largura, alt)), (k * (largura + 8), 0))
        if rotulos:
            d.text((k * (largura + 8) + 6, alt + 6), str(rotulos[k]), fill=(200, 200, 200))
    folha.save(saida, quality=82)
    return saida


def avisar(msg):
    print(msg, file=sys.stderr)
