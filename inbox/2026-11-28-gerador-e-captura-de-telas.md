---
de: claude-ai
para: escritorio
status: aberto   # aberto | em-andamento | feito | bloqueado
---

# Pedido
O Matheus aprovou (28/11) trocar o HTML feito à mão por um gerador: a ideia vira uma ficha
YAML e o código monta o carrossel ou o Reel no padrão aprovado. A primeira versão está em
`gerador/` (leia `gerador/README.md`). São duas partes:

1. **Revisar e testar o gerador no seu ambiente.**
   - Rode os três exemplos com `--previa` e depois completos:
     - `gerador/exemplos/carrossel-conheca-o-unnar.yaml`
     - `reels/2026-12/reel-02-mesa-de-controle.yaml`
     - `reels/2026-12/reel-03-escala.yaml`
   - O que falhar no seu PC (caminho do Chrome, ffmpeg, fontes), corrija no código por PR.
   - Aponte o que for frágil ou mal resolvido no código.
2. **Captura automática das telas do Unnar.** Essa parte depende do Matheus autorizar subir o
   Unnar local; sem a autorização, faça só a parte 1 e marque esta como `bloqueado`.
   - Um script que abre o Unnar local com dados de demonstração e captura, por Playwright,
     as telas e os trechos que os posts usam:
     - painel: evento aberto, presença e despesas;
     - portal: agenda, confirmar presença, check-in, lançar despesa e o aviso no sino.
   - Saída em `assets/unnar/telas/AAAA-MM-DD/`, com um `manifesto.yaml` dizendo, para cada
     arquivo, a tela, o tamanho, a duração e o que aparece.
   - A ideia é que eu chame o script por uma ficha, sem gravação manual.

# Pronto quando
- Os três exemplos saem `OK` no seu PC, ou há um PR com as correções.
- `outbox/` traz a sua revisão do código: o que mudou e o que sugere.
- (Parte 2) O script gera as telas listadas, com a logo nova do Unnar e o manifesto, sem
  endereço, sem dado real e sem senha no repositório (credenciais só por variável de ambiente).

# Contexto
- Regras do que os textos e as telas podem mostrar: `PROJETO.md`, seção "O que os textos podem
  e não podem dizer". O gerador confere essas regras em `gerador/comum.py` (lista `REGRAS`).
- O repositório é público: nada de código-fonte do Unnar, chaves ou dados reais.
- Os vídeos do portal de hoje (`assets/unnar/gravacoes/`) têm o cabeçalho com a logo antiga
  (por isso o corte padrão) e o do sino mostra um endereço na lista de eventos.
