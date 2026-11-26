---
de: claude-ai
para: escritorio
status: aberto
---

# Pedido
Gravar clipes curtos do Unnar rodando de verdade, com dados de exemplo, para usar nos
Reels. De preferência por um script (Playwright, por exemplo) em
`scripts/gravar-unnar/`, para regravar quando a interface mudar.

Portal do profissional, no celular (viewport de celular, saída 1080×1920 ou maior):
1. Agenda com eventos de duas empresas na mesma lista.
2. Confirmar presença num evento.
3. Check-in e check-out.
4. Lançar uma despesa.
5. Aviso de nova escala chegando no sino.

Painel da empresa, no computador (1920×1080):
6. Dashboard.
7. Um evento aberto: status, checklist, serviços do pacote e equipe com função e cachê.
8. Presença e despesa chegando no painel (o lado da empresa dos itens 2 a 4).
9. Agenda de eventos em lista e em calendário.

# Pronto quando
- Um MP4 por item (H.264, 30 fps, sem áudio, de 4 a 8 s), em
  `assets/unnar/gravacoes/`, com nome que diga o que mostra
  (ex.: `portal-03-check-in.mp4`), mais um PNG de cada tela parada.
- Tema escuro, que é o padrão do material.
- Só dados de exemplo: nenhum nome, telefone ou documento real.
- O script roda de novo com um comando, descrito na resposta em `outbox/`.
- Nada de código-fonte do Unnar neste repositório; o script só abre o sistema e grava.

# Contexto
- Formato dos Reels em `PROJETO.md` (seção Formatos). O primeiro Reel
  (`reels/2026-11/reel-01-quem-confirmou.html`) usa capturas paradas do site; com as
  gravações, os próximos mostram o sistema em movimento.
- Os próximos Reels saem dos posts 6 (agenda do freelancer), 9 (despesas e avisos) e
  2 (conheça o Unnar) do lote 1.
