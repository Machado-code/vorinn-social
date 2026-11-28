"""Uso:
  python3 -m gerador <ficha.yaml>            gera a peça inteira (PNGs ou MP4) e a prévia
  python3 -m gerador <ficha.yaml> --previa   só a prévia e as checagens (rápido, para conferir)
  python3 -m gerador <ficha.yaml> --quadros 1.2,4.5   prévia com esses instantes (Reels)

Sai com código 1 se houver problema de layout, arquivo faltando ou texto que fere as regras
do PROJETO.md (aceite uma regra de propósito com `regras_aceitas` na ficha).
"""
import sys

import yaml

from .comum import ErroFicha


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    ficha_path = argv[0]
    so_previa = "--previa" in argv
    quadros = None
    if "--quadros" in argv:
        quadros = [float(x) for x in argv[argv.index("--quadros") + 1].split(",")]
    with open(ficha_path, encoding="utf-8") as f:
        ficha = yaml.safe_load(f)
    tipo = ficha.get("tipo")
    try:
        if tipo == "reel-mesa":
            from . import reel_mesa as mod
        elif tipo == "carrossel":
            from . import carrossel as mod
        else:
            raise ErroFicha("tipo: reel-mesa ou carrossel")
        r = mod.gerar(ficha_path, ficha, so_previa=so_previa, quadros=quadros)
    except ErroFicha as e:
        print(f"ERRO NA FICHA: {e}")
        return 2

    for k in ("mp4", "pasta", "html", "previa"):
        if r.get(k):
            print(f"{k}: {r[k]}")
    if r.get("duracao"):
        print(f"duração: {r['duracao']:.1f}s")
    for onde, trecho, motivo, padrao in r["avisos"]:
        print(f"REGRA ({onde}): '{trecho}' -> {motivo}  [para aceitar: regras_aceitas: [{padrao}]]")
    for p in r["problemas"]:
        print(f"PROBLEMA: {p}")
    ok = not r["avisos"] and not r["problemas"]
    print("OK" if ok else "REVISAR")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
