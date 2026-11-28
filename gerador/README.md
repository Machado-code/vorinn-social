# Gerador de posts e Reels

A ideia vira uma **ficha YAML** curta e o código monta a peça no padrão aprovado: slides PNG
1080x1350 ou Reels MP4 1080x1920 com trilha. Ninguém escreve nem corrige HTML à mão. Isso
economiza tokens e mantém tudo igual entre as semanas.

```bash
python3 -m gerador <ficha.yaml> --previa   # só a prévia e as checagens (segundos)
python3 -m gerador <ficha.yaml>            # peça final (Reel de 15 s: cerca de 2 min)
```

Requisitos: Python 3 com `pyyaml`, `jinja2`, `playwright`, `Pillow` e `numpy`; Google
Chrome (`CHROME_PATH`, padrão `/usr/bin/google-chrome`); `ffmpeg`. Fontes Inter e Gelasio
instaladas no sistema (a Sora vem de `assets/fonts`).

## Como usar para gastar pouco
1. Escreva a ficha copiando um exemplo (`reels/2026-12/*.yaml` ou `gerador/exemplos/`).
2. Rode com `--previa`. Leia a saída: `OK` ou a lista de `REGRA` e `PROBLEMA`.
3. Olhe **só** a imagem `*-previa.jpg` (uma folha pequena com 5 quadros ou todos os slides),
   nunca o HTML gerado nem quadro por quadro.
4. Corrija a ficha, não o HTML. Quando sair `OK`, rode sem `--previa`.

A saída termina com `OK` (código 0) ou `REVISAR` (código 1). Ficha mal preenchida dá
`ERRO NA FICHA` (código 2).

## Reels "Mesa de controle" (`tipo: reel-mesa`)

```yaml
tipo: reel-mesa
saida: reels/2026-12/reel-03-escala        # opcional; padrão: mesmo nome da ficha
gancho: "Quem trabalha no *sábado*?"        # primeira frase, aparece no quadro 1
pecas:                                      # até 4 encaixes, na ordem 1 a 4
  - {nome: Escala, icone: calendario, frase: "Monte a *escala* do evento"}   # estado padrão: cai
  - {nome: Confirmação, icone: confirmado, estado: encaixada}               # já aparece no lugar
  - {nome: Check-in, icone: checkin, estado: vazia}                         # encaixe vazio
tela:
  arquivo: assets/unnar/gravacoes/portal-05-aviso-de-escala-no-sino.mp4    # PNG ou MP4
  formato: cartao              # vídeo: celular (padrão) ou cartao; imagem: sempre cartão
  corte: [120, 330, 840, 735]  # vídeo: x, y, largura, altura na tela original
  inicio: 0.9                  # vídeo: segundo em que o trecho começa
  console: assets/...png       # opcional: imagem pequena na tela do console
  frases: ["a equipe vê no *sino*", "e recebe por *e-mail*"]     # 2,3 s cada
  destaques:                   # em pixels da imagem ou do vídeo original
    - {x: 150, y: 465, w: 780, h: 150, raio: 24, aos: 1.1}       # aos = segundos depois da tela aparecer
  rotulo: Tela real do Unnar   # opcional
fecho: {linha1: "Gerencie menos.", linha2: "*Crie mais.*", botao: "Conheça o Unnar · link na bio"}  # opcional
legenda: |                     # texto do post (passa pelas regras também)
  ...
regras_aceitas: []             # nomes de regras aceitas de propósito (ver abaixo)
```

- `*palavra*` é a palavra-chave da frase: Gelasio itálico dourado, na caixa de seleção. Uma
  por frase. A pontuação colada nela (`*sábado*?`) fica fora do destaque.
- Ícones: `calendario`, `confirmado`, `checkin`, `despesa`, `sino`, `equipe`, `painel`,
  `agenda`, `camera`.
- Os tempos saem sozinhos: gancho de 2,4 a 3 s, 2 s por peça que cai, 2,3 s por frase da
  tela e 2,7 s de fechamento. A câmera, as etiquetas, as faíscas e a trilha seguem os tempos.
- Para a série de quarta: as peças das semanas anteriores entram com `estado: encaixada`.
- Corte padrão dos vídeos do portal: `[120, 330, 840, 1208]`, que esconde o cabeçalho com
  a logo antiga. Se aparecer endereço, corte menos altura (como no Reel 3).

## Carrosséis (`tipo: carrossel`)

```yaml
tipo: carrossel
marca: u                      # u = Unnar (Gelasio e dourado), v = Vorinn (Sora e azul)
saida: posts/2026-12/10-escala
slides:
  - selo: Para empresas de eventos e fotografia
    titulo: "Gerencie menos.\n*Crie mais.*"     # 1º slide vira h1; os outros, h2
    texto: Conheça o Unnar.
    tela: {arquivo: assets/capturas-do-site/unnar-painel-conteudo.png, formato: capa}
  - selo: Como funciona
    titulo: Clientes, eventos e equipe *num só lugar*.
    lado_a_lado: true
    cartoes:
      - {selo: Painel, titulo: "No computador, para a gestão", texto: "Clientes, eventos e equipe."}
      - {selo: Portal, titulo: "No celular, para a equipe", texto: "Agenda e check-in."}
legenda: |
  ...
```

Blocos de um slide, na ordem em que aparecem: `selo`, `titulo` (ou `h1`/`h2`), `texto`
(texto ou lista de parágrafos; `**negrito**`), `grande`, `lista` (itens com `titulo` e
`texto`, ou só frases), `cartoes` (com `lado_a_lado: true` ficam em 2 colunas), `passos`,
`tela` (`capa`, `larga`, `corte` ou `celular`, que põe o texto ao lado; `nota` opcional),
`cta` (`botao`, `sub`), `nota`, `monograma` (Vorinn, capa).

**Cuidado com o YAML:** dentro de `{ }` a vírgula separa campos. Texto com vírgula ou com
dois-pontos vai entre aspas.

Saída: `01.png`, `02.png`... + `legenda.md` + `previa.jpg` na pasta `saida`.

## Checagens automáticas
- **Layout:** legenda em mais de 2 linhas ou abaixo da área segura; etiqueta ou tela real
  fora do quadro; texto do slide passando da margem ou encostando no rodapé.
- **Arquivos e fontes:** imagem ou vídeo que não carregou; fonte que não está instalada.
- **Regras do PROJETO.md** (em todo texto da ficha, legenda incluída). Para aceitar uma de
  propósito, ponha o nome em `regras_aceitas`:
  `tempo-real`, `gps`, `prova-presenca`, `comprovante`, `reembolso`, `aprovacao-despesa`,
  `notificacao`, `app-de-loja`, `teste-gratis`, `orcamento`, `gravacao`, `endereco`,
  `gancho-proibido`. Se o PROJETO.md mudar, atualize a lista em `gerador/comum.py`.

As checagens não substituem o olho: a prévia ainda é conferida antes de pedir o "aprovo".

## Publicação
Depois do merge, o Buffer recebe o link raw fixado no commit:
`https://raw.githubusercontent.com/Machado-code/vorinn-social/<sha>/<caminho>`.

## Divisão do trabalho
- **Claude (claude.ai e tarefa de domingo):** escreve as fichas a partir da fila de pautas,
  roda o gerador, confere a prévia e manda para o "aprovo".
- **Escritório:** revisa e testa o código e cuida do que depende do Unnar rodando, como
  capturar telas e trechos reais por script com dados de demonstração (pedido em `inbox/`).
- **Matheus:** aprova as peças e os merges.

## Próximos passos
- Captura automática de telas do Unnar local (escritório).
- Novos tipos quando forem aprovados: Reel de tela gravada (o formato do Reel 1) e stories.
