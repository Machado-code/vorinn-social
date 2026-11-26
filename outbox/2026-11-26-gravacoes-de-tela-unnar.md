---
de: escritorio
para: claude-ai
pedido: inbox/2026-11-26-gravacoes-de-tela-unnar.md
status: bloqueado
---

# Resultado

Entreguei os 9 itens em `assets/unnar/gravacoes/`. Cada item tem um MP4 (H.264, 30 fps, sem áudio,
de 4,2 a 8 s) e o PNG da tela parada. São todos telas reais do Unnar no tema escuro, com dados de
exemplo, mas **não são gravações do sistema rodando**. Saem do que já existia: as capturas de tela
feitas para o vídeo de 90 s da landing e o próprio vídeo.

- **Portal (itens 1 a 5):** clipes verticais 1080×1920 montados das capturas do celular. Uma tela
  passa para a seguinte com fusão, a agenda rola (a câmera percorre a captura da página inteira) e
  um círculo marca o toque.
- **Painel (itens 6 a 9):** trechos 16:9 (1920×1080) do vídeo de 90 s, com os textos e os destaques
  do vídeo.

O status é `bloqueado` porque o pedido não está cumprido inteiro:

- não há gravação ao vivo;
- faltam o check-out (item 3) e a agenda em lista (item 9);
- as telas têm a marca antiga do app e datas de outubro;
- o script refaz os cortes, mas não grava de novo.

O caminho para fechar está em **O que falta**.

# Detalhes

## O que é cada arquivo

Coloque o aviso "Tela real do Unnar, com dados de exemplo." em todo uso.

| Item | Arquivo | O que mostra | De onde veio |
| --- | --- | --- | --- |
| 1 | `portal-01-agenda-duas-empresas.mp4` (6,0 s) | A agenda do profissional rola do topo até o fim. A lista tem eventos da Aurora Fotografia e, no fim, um da Bruma Eventos | Capturas da agenda (topo, página inteira e fim da rolagem), com o cabeçalho e a barra de baixo parados como no aparelho |
| 1 | `portal-01-agenda-duas-empresas.png` | A agenda rolada: dois eventos da Aurora e um da Bruma na mesma tela | Captura do celular |
| 2 | `portal-02-confirmar-presenca.mp4` (4,9 s) | "Sua presença": toque em "Confirmar presença", e a etapa passa a "Confirmado", com data e hora | Duas capturas (antes e depois), alinhadas pela lista de etapas |
| 2 | `portal-02-confirmar-presenca.png` | A tela antes de confirmar, com o botão "Confirmar presença" | Captura do celular |
| 3 | `portal-03-check-in.mp4` (4,9 s) | Toque em "Fazer check-in", e a etapa "Check-in" ganha data e hora. **Termina no botão "Fazer check-out": o check-out não foi capturado** | Duas capturas, alinhadas |
| 3 | `portal-03-check-in.png` | Depois do check-in: a linha do tempo com convite, confirmação e check-in | Captura do celular |
| 4 | `portal-04-lancar-despesa.mp4` (5,7 s) | O formulário "Registrar despesa" vazio, depois preenchido ("Estacionamento no local", R$ 35,00), depois a despesa no topo da lista do evento | Três capturas, com fusão |
| 4 | `portal-04-lancar-despesa.png` | O formulário preenchido | Captura do celular |
| 5 | `portal-05-aviso-de-escala-no-sino.mp4` (4,7 s) | A agenda com o sino marcando 4, toque no sino, e abrem os avisos "Você foi escalado num evento", cada um com o nome da empresa | Duas capturas, com fusão |
| 5 | `portal-05-aviso-de-escala-no-sino.png` | Os avisos abertos | Captura do celular |
| 6 | `painel-06-dashboard.mp4` (7,5 s) | O painel da empresa entra, destaca o "Resumo da empresa" e depois os "Próximos eventos". À esquerda, o texto do vídeo ("Sua empresa num relance") | Vídeo de 90 s, de 11,0 a 18,5 s |
| 6 | `painel-06-dashboard.png` | O dashboard | Captura do painel |
| 7 | `painel-07-evento-aberto.mp4` (8,0 s) | Um evento aberto. Destaques em sequência: status, equipe com função e cachê e presença, checklist e serviços do pacote | Vídeo de 90 s, de 30,4 a 38,4 s |
| 7 | `painel-07-evento-aberto.png` | **A página inteira** do evento (2880×4688): status, equipe, despesas, checklist e serviços | Captura de página inteira |
| 8 | `painel-08-presenca-e-despesa.mp4` (8,0 s) | Os dois lados ao mesmo tempo: no celular, o check-in e a despesa. No painel, "Check-in da equipe" e depois "Quem lançou, o quê e quanto" | Vídeo de 90 s, de 61,8 a 69,8 s |
| 8 | `painel-08-presenca-no-painel.png` | O evento do dia no painel, com a profissional em "Check-in feito" | Captura do painel |
| 8 | `painel-08-despesas-no-painel.png` | As despesas do evento no painel: quem lançou, o quê, quanto e o total | Captura do painel |
| 9 | `painel-09-agenda-calendario.mp4` (4,2 s) | O calendário de outubro com os eventos (cerca de 2,5 s). O cursor clica no casamento e o evento abre. **Não há a agenda em lista** | Vídeo de 90 s, de 27,6 a 31,8 s |
| 9 | `painel-09-agenda-calendario.png` | O calendário do mês | Captura do painel |

Formatos:

- **Clipes do portal:** 1080×1920. A tela do celular ocupa 888 px de largura, centralizada sobre
  `#0E0D12` (o fundo do tema escuro do app).
- **PNG do portal:** a captura original, 1170×2532 (tela de 390×844 a 3x). Não foi convertida para
  1080×1920.
- **PNG do painel:** 2880×1800 (1440×900 a 2x), exceto o 7 e o 9, que são a página inteira
  (2880×4688 e 2880×2488).
- **Cortes 16:9:** trazem a moldura de navegador e de celular, os títulos e os selos de destaque do
  vídeo. A barra de endereço mostra só "Unnar".
- **Tamanho:** os 19 arquivos (9 MP4 e 10 PNG) somam 8,4 MB, e nenhum clipe passa de 1,6 MB.

## Dados de exemplo

Todos os nomes, empresas, clientes, locais e valores vêm do script que popula o ambiente de
desenvolvimento e são fictícios. Conferi cada PNG e quadros de cada clipe. Nenhum mostra e-mail,
documento, endereço de máquina nem dado de cliente real. Ficaram de fora duas telas: a de informações
do evento no celular, que mostra o telefone do cliente de exemplo, e a ficha do cliente no painel,
que mostra o documento dele. Os dois são fictícios, mas estão num formato que poderia ser de alguém.
Os locais são fictícios, mas os endereços usam nomes de ruas reais, com número e CEP: não dê zoom no
cartão "Resumo" do painel nem cite endereço nos textos.

## Como refazer os cortes

O script público `scripts/gravar-unnar/cortes.mjs` (Node 18+, sem dependências, só ffmpeg) refaz os 9
clipes e os PNG. Não abre o sistema, não usa rede nem credenciais, e os caminhos entram por argumento:

```
node scripts/gravar-unnar/cortes.mjs --video <vídeo de 90 s> --capturas <pasta das capturas, com o meta.js> [--ffmpeg <ffmpeg>] [--saida <pasta>] [--so portal-03,painel-07]
```

As entradas ficam fora deste repositório, no projeto privado do vídeo, então quem roda é o
escritório. A posição dos botões e das listas vem do `meta.js` das capturas. Com capturas novas, o
script se ajusta sozinho. Os tempos dos cortes 16:9 seguem o roteiro do vídeo de 90 s: se o vídeo
mudar, ajuste a tabela `CORTES`.

# Divergências

1. **Não é gravação ao vivo.** O vídeo de 90 s também não é: ele monta as capturas paradas com câmera,
   cursor e toques animados. Os toques destes clipes também são desenhados. Nos textos, prefira "tela
   real" a "gravação".
2. **Marca antiga nas telas:** o cabeçalho do app nas capturas ainda tem o "U" com "Unnar" em serifa.
   Desde 2026-10-03, o app usa o "N" dourado com a barra (`assets/marca/`). Nos clipes do portal, o
   cabeçalho aparece pequeno no topo.
3. **Datas:** as capturas são de 2026-10-01. Mostram "Outubro de 2026", "Hoje é quinta-feira, 1 de
   outubro de 2026" e horários como "01/10/2026, 17:34".
4. **Item 3 sem check-out** e **item 9 sem a vista em lista:** essas telas não foram capturadas.
5. **Sino do painel fora do item 8:** na captura de outubro, o aviso de despesa do lado da empresa
   saiu sem acento ("lancou"). Por isso o vídeo e estes arquivos mostram só a presença no sino do
   painel. O sistema já corrigiu esse texto, e uma gravação nova pode mostrar o sino inteiro.
6. **O que o sistema não faz e os posts não devem prometer** (regra do vídeo, conferida no código):
   - "tempo real" ou "na hora": o sino consulta a cada 60 s;
   - GPS ou "prova de presença": a localização do check-in é opcional;
   - aprovação, reembolso ou comprovante de despesa: o formulário avisa que não há envio de
     comprovante;
   - aviso no celular com o Unnar fechado (notificação do sistema) ou app de loja: hoje não há;
   - cadastro por conta própria ou teste grátis.

# O que falta e como fechar

Uma gravação nova, com o Unnar rodando na máquina do escritório e dados de exemplo novos:

- a marca atual já sai no cabeçalho;
- datas atuais;
- celular em 9:16 nativo;
- gravação de verdade da tela;
- o check-out e a agenda em lista.

Isso depende de subir o ambiente local do Unnar (API, web e bancos em contêiner), o que precisa da
autorização do Matheus. A captura e o seed continuam no projeto privado, porque usam o ambiente e as
contas de desenvolvimento. Neste repositório entra só o resultado, refeito pelo `cortes.mjs` ou por
um sucessor do mesmo tipo. **Estimativa: de 4 a 6 h do escritório**, entre subir o ambiente, ajustar a
captura para 9:16 com os itens que faltam, gravar e conferir os dados de cada quadro.
