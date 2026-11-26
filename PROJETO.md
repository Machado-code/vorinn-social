# Projeto: Instagram da Vorinn (@vorinn.com.br)

Memória compartilhada entre o Claude do claude.ai e o escritório (Claude Code no VS Code).
Quem mudar uma decisão atualiza este arquivo no mesmo commit.

## Objetivo
Divulgar a Vorinn e, principalmente, o Unnar no Instagram para conseguir clientes
(empresas de eventos e fotografia), com o mínimo de trabalho manual do Matheus.

## Responsabilidades
- **Claude (claude.ai):** estratégia, textos, legendas, artes (carrosséis) e Reels;
  agenda no Buffer depois da aprovação do Matheus. Nunca publica sem aprovação.
- **Matheus:** aprova ou pede mudanças; atende os contatos que chegam no WhatsApp.
- **Escritório:** o que precisa do código e do ambiente da Vorinn e do Unnar: logos
  oficiais, gravações de tela do Unnar rodando, conferir no código se o que os posts
  dizem é verdade, ferramentas em `scripts/`. Sempre por pedido em `inbox/`.
  Papel, rotina e limites em `ESCRITORIO.md`.

## Marca
- Um perfil só: @vorinn.com.br (o @vorinn já era de outra pessoa). O Unnar fica com cerca de 2/3 dos posts enquanto for o foco.
- **Vorinn** (vorinn.com.br): fundo #030814, azul #2F95FF / #6DB4FF (botão: degradê
  #0180FC → #005BCF), texto #CBD5E1 e #94A3B8; títulos em **Sora** semibold
  (`assets/fonts/`, licença OFL), texto em Inter.
- **Unnar** (unnar.com.br): fundo #0E0D12, superfície #19181F, creme #EDE8DF, dourado
  #C8982E (hover #E0B84A), lilás acinzentado #9088A0; títulos em serifa (Georgia/Gelasio)
  com destaque em itálico dourado.
- **Logos oficiais em `assets/marca/`** (entregues pelo escritório em 26/11/2026). O símbolo
  do Unnar é o **"N" dourado com a barra**, nunca um "U"; o nome "UNNAR" é desenho (SVG),
  não se digita. A Vorinn só tem PNG (para fundo escuro); o monograma fica nítido até uns
  430 px de largura. Abertura animada do Unnar: `assets/marca/unnar-abertura.mp4`.
- As capturas de tela do Unnar (de 01/10/2026) ainda têm a marca antiga no cabeçalho do app:
  ao usar, corte o cabeçalho (celular) ou a barra lateral (painel).
- Voz: primeira pessoa do singular ("Desenvolvo…", "Me chame no WhatsApp"), direta.
- Telas do Unnar sempre com dados de exemplo, com o aviso "Tela real do Unnar, com dados
  de exemplo." Nunca dados reais de clientes.

## O que os textos podem e não podem dizer (conferido no código pelo escritório, 26/11/2026)
- Despesas: a empresa vê quem lançou, o quê, quanto e a **data** (sem hora). Não há foto,
  comprovante, aprovação nem reembolso.
- Presença: confirmação, check-in e check-out ficam registrados com data e hora; no painel a
  empresa vê a situação ("Check-in feito"), e o horário aparece no aviso do sino. Não falar em
  GPS nem em prova de presença.
- Avisos: o sino atualiza a cada minuto com o Unnar aberto; escalas também chegam por e-mail.
  Não prometer "tempo real" nem notificação no celular com o app fechado.
- Unnar não é app de loja (é web, dá para pôr atalho na tela inicial) e não tem cadastro
  próprio nem teste grátis.
- Orçamento e Contratado são situações do evento: o Unnar não gera nem envia orçamento.
- IA jurídica: petição inicial **trabalhista**, no modelo do escritório, em Word; é minuta e a
  revisão final é do advogado.
- Telas: dizer "tela real", não "gravação". Não mostrar nem citar endereços.

## Formatos
- Carrossel: PNG 1080×1350. Fonte em `scripts/posts.py`, render com `scripts/render.py`.
- Reels: MP4 1080×1920, 30 fps, sem rosto e sem voz, trilha gerada por
  `scripts/make_audio.py` (sem direitos autorais). Texto fixo no topo sobre a dor do
  cliente, cenas de 2 a 3 s com uma frase cada, telas do Unnar, marca no fim.
  Área segura: evitar ~250 px do topo, ~420 px de baixo e ~150 px da direita.
- Recursos visuais dos próximos Reels: legenda que destaca palavra por palavra no topo e
  cartões de tela animados no meio, com os fluxos reais do Unnar (gravações do escritório).
- Não usar: pedido de comentário com palavra-chave ("Comente UNNAR…"), gancho sobre IA
  ("Pedi pra IA criar…"), avatar ou voz. A chamada é o WhatsApp pelo link da bio.
- Sem skill de vídeo de terceiros por enquanto: os Reels saem dos scripts deste
  repositório. Se um dia entrar uma, o conteúdo dela é lido inteiro antes de instalar,
  e ela roda no escritório (o claude.ai não instala pacotes).

## Stack
- Publicação: Buffer gratuito (mesma conta do Sem Atalhos), canal Instagram @vorinn.com.br
  conectado pelo login do Instagram, sem página do Facebook.
- Imagens e vídeos: neste repositório (público). O Buffer recebe o link raw fixado no
  commit: `https://raw.githubusercontent.com/Machado-code/vorinn-social/<sha>/<caminho>`
- Atendimento: perguntas frequentes nativas do Instagram, apontando para o WhatsApp
  (19) 99559-6092.
- Sem custo no início: sem anúncios e sem ferramentas pagas.

## Conteúdo
- Linhas: dor da operação de eventos; Unnar em uso (um recurso por post); freelancer
  (uma conta para várias empresas); Vorinn (automações, IA aplicada, sistemas sob medida).
- Ritmo: segunda, quarta e sexta; um Reel por semana e dois carrosséis. Qualidade antes
  de volume: nada de um vídeo por dia.
- Ciclo de métricas: toda semana, antes de montar o lote, o claude.ai lê no Buffer o
  alcance, os salvamentos e os compartilhamentos dos posts publicados e repete o tema ou o
  formato que funcionou. Com 3 posts por semana, só tirar conclusão depois de 4 a 6
  semanas de dados.
- Lote 1 (aprovado em 26/11/2026): `posts/2026-11/lote-1/`, 9 carrosséis.
  Agenda: posts 1 a 3 no dia do lançamento, depois segunda, quarta e sexta.
- Reel 1 "Quem já confirmou?": `reels/2026-11/` (abre o perfil no lançamento).

## Como nos comunicamos
- `inbox/`: pedidos. Um arquivo por pedido, `inbox/AAAA-MM-DD-assunto.md`
  (modelo em `inbox/README.md`).
- `outbox/`: respostas, com o MESMO nome do pedido.
- Mudanças entram por pull request; o Matheus aprova o merge na `main`.

## Regras
- Nada é publicado sem aprovação do Matheus.
- Repositório PÚBLICO: nunca commitar tokens, chaves, senhas, dados de clientes, código
  do Unnar ou da Vorinn, nem dados reais de uso.
- Posts em PT-BR, 1ª pessoa, no máximo 4 hashtags do nicho.
