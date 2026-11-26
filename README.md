# vorinn-social

Artes, Reels e roteiros do Instagram @vorinn (Vorinn e Unnar).

- `PROJETO.md`: decisões e memória do projeto.
- `ESCRITORIO.md`: como o escritório (Claude Code) trabalha aqui.
- `inbox/` e `outbox/`: pedidos e respostas entre o claude.ai e o escritório.
- `posts/`: carrosséis (PNG 1080×1350) e legendas.
- `reels/`: Reels (MP4 1080×1920) e o HTML de onde eles saem.
- `assets/`: logos, capturas e gravações de tela.
- `scripts/`: render das artes (`render.py`), dos Reels (`render_reel.py`) e da trilha
  (`make_audio.py`). Fora do claude.ai, defina `CHROME_PATH` se quiser usar um Chrome
  instalado; sem ele, o Playwright usa o Chromium dele.
