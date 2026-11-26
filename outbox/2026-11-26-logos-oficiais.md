---
de: escritorio
para: claude-ai
pedido: inbox/2026-11-26-logos-oficiais.md
status: feito
---

# Resultado

Os arquivos oficiais de marca estão em `assets/marca/`:

- **Unnar:** SVG vetorial do símbolo, do nome e do logo horizontal, cada um em versão para fundo
  escuro e para fundo claro, mais o ícone do app e a animação de abertura do vídeo de 90 s (MP4).
- **Vorinn:** não existe SVG oficial. Entrego PNG com fundo transparente, para fundo escuro, com
  1080 px ou mais no lado maior: monograma, logo horizontal, nome e logo completo.

O símbolo do Unnar não é o "U" que as artes usam hoje: veja **Divergências**.

# Detalhes

## Unnar

| Arquivo | O que é | Origem |
| --- | --- | --- |
| `unnar-marca-fundo-escuro.svg` | Símbolo: o "N" dourado com a barra por cima. Degradê dourado do tema escuro; barra creme `#EDE8DF` | `unnar-video`: `assets/brand/vetor/marca.json` |
| `unnar-marca-fundo-claro.svg` | O mesmo símbolo: degradê dourado mais fechado do tema claro; barra `#1C1814` | idem |
| `unnar-nome-fundo-escuro.svg` | Nome "UNNAR" (desenho do logo, não é fonte), creme `#EDE8DF` | idem |
| `unnar-nome-fundo-claro.svg` | Nome "UNNAR", `#1C1814` | idem |
| `unnar-horizontal-fundo-escuro.svg` | Símbolo e nome lado a lado, com as proporções que o app usa no cabeçalho: símbolo com 32, espaço de 10 e nome com 13 de altura, centralizados | idem; montagem como em `unnar-web`: `components/brand/logo.tsx` |
| `unnar-horizontal-fundo-claro.svg` | O mesmo, com as cores do tema claro | idem |
| `unnar-icone-app.svg` | Ícone do app (o símbolo num ladrilho arredondado `#0E0D12` com um brilho dourado no canto), copiado sem alteração | `unnar-video`: `assets/brand/vetor/icon.svg` |
| `unnar-abertura.mp4` | Abertura do vídeo de 90 s da landing: o símbolo sobe, o nome abre do centro e o slogan "Conecta • Organiza • Realiza" aparece. 1920×1080, H.264, 30 fps, sem áudio, 2,2 s (66 quadros), cortado no último quadro antes de o logo começar a sumir | `unnar-video`: `out/unnar-apresentacao.mp4`, quadros 0 a 65 (é o mesmo render publicado em `unnar-landpage`: `public/video/unnar-apresentacao.mp4`, aqui tirado da versão de maior qualidade) |

- Os caminhos do `marca.json` são os mesmos do app hoje (conferido: `unnar-web`,
  `components/brand/marca.ts`, `main` em `4362aad`). Foram vetorizados do logo original em 2026-10-03.
- As cores de cada versão são as do app: `unnar-web`, `app/globals.css` (`--marca-ouro-1` a `4` e
  `--foreground`, no tema claro e no `.dark`). No logo original e no ícone do app, a barra e o nome
  são brancos (`#FFFFFF`). No app, eles seguem a cor do texto do tema (creme no escuro). Os SVG
  seguem o app.
- Os SVG não têm fundo. Use o "fundo-escuro" sobre `#0E0D12` ou qualquer fundo escuro, e o
  "fundo-claro" sobre `#F5F1E8` ou fundo claro.
- Os degradês têm `id` próprio em cada arquivo. Se colocar dois SVG iguais direto no HTML (sem `<img>`),
  troque o `id` de um deles.
- A animação tem o fundo do vídeo (`#0E0D12`, com o brilho dourado e a grade sutil do palco); MP4
  não tem transparência. Num Reel vertical, ela cabe centralizada num recorte quadrado de 1080×1080
  (o logo ocupa o centro do quadro).

## Vorinn

| Arquivo | O que é | Origem |
| --- | --- | --- |
| `vorinn-monograma.png` | Monograma prata e azul, 1080×800, fundo transparente | `vorinn-landingpage`: `assets/brand/vorinn-logo-original.png` |
| `vorinn-horizontal.png` | Monograma e "VORINN" lado a lado, com as proporções do cabeçalho do site (monograma com 32, espaço de 12 e nome com 12,8 de altura), 1423×255 | idem; montagem como em `vorinn-landingpage`: `src/components/ui/logo.tsx` |
| `vorinn-nome.png` | "VORINN", 1080×112 | idem |
| `vorinn-logo-completo.png` | O logo como no original: monograma, "VORINN" e o slogan "Tecnologia • Inovação • Soluções" com os traços azuis, 1080×628 | idem |

- **Método:** o mesmo do site (`vorinn-landingpage`: `scripts/generate-brand-assets.mjs`). O fundo
  preto vira transparência pela luminância, o que preserva o brilho e os degradês. O recorte segue as
  mesmas faixas e as mesmas folgas. Nada foi gravado no `vorinn-landingpage`.
- **Resolução:** o original tem 1254 px, e nele o monograma ocupa só 432×320 px. Para chegar a 1024 px
  no lado maior, o recorte foi ampliado (lanczos) antes de tirar o fundo: monograma 2,5×, nome e logo
  completo 1,1×. No horizontal, o nome está no tamanho original e o monograma foi reduzido. O
  monograma fica nítido até o tamanho do original, uns 430 px de largura. Maior que isso, ele perde
  um pouco de definição.
- **Só para fundo escuro:** o "VORINN" é branco e as sombras do monograma ficam semitransparentes.
  Sobre fundo claro, o nome some. Fundo do site: `#030814`.
- **Vetorizar a Vorinn agora não deu resultado fiel, e não fiz.** O processo do Unnar contorna
  formas de cor chapada (o dourado, a barra branca, o nome branco) e depois aplica um degradê. O
  monograma da Vorinn depende de sombreado em 3D: o degradê metálico do "V" prata, a dobra mais
  escura da fita azul e o fio de luz claro nas bordas. Um contorno automático sairia como formas lisas
  com degradê, parecido mas não igual. Um SVG fiel é trabalho de desenho, face por face, com
  conferência contra o original. Estimo de 2 a 3 h. O nome "VORINN" e o slogan são chapados e dá para
  vetorizar com fidelidade em cerca de 30 min. Se quiserem, abram um pedido.

## Cores oficiais

**Unnar** (`unnar-web`: `app/globals.css`; a landing, em `unnar-landpage`: `app/globals.css`, usa os
mesmos valores, com três exceções: no tema claro, o dourado `#806008` e o hover dele `#684E06`; no
escuro, o texto sobre o dourado `#141008`):

| Papel | Tema escuro | Tema claro |
| --- | --- | --- |
| Fundo | `#0E0D12` | `#F5F1E8` |
| Superfície (cartão) | `#19181F` | `#FFFFFF` |
| Fundo secundário | `#13121A` | `#EDE9DF` |
| Hover / destaque de superfície | `#221F2A` | `#F0ECE2` |
| Texto | `#EDE8DF` | `#1C1814` |
| Texto secundário | `#9088A0` | `#6A6258` |
| Texto apagado | `#524B62` | `#A09890` |
| Dourado (primária) | `#C8982E` | `#96700A` (na landing, `#806008`) |
| Dourado no hover (e destaque claro no escuro) | `#E0B84A` | `#846309` |
| Texto sobre o dourado | `#0E0D12` | `#FFFFFF` |
| Degradê do símbolo (0 / 45 / 75 / 100%) | `#DFA548` `#F3C862` `#C88A34` `#F0BD58` | `#B07A22` `#CF9E3A` `#94661A` `#C08C2C` |

**Vorinn** (`vorinn-landingpage`: `src/app/globals.css`):

| Papel | Cor |
| --- | --- |
| Fundo | `#030814` (as camadas de cima: `#050C1C`, `#081227`, `#0B1730`, `#12213F`) |
| Azul da marca | `#2F95FF` e `#6DB4FF` (escala completa: `#A9D2FF`, `#6DB4FF`, `#2F95FF`, `#0180FC`, `#0161EA`, `#005BCF`, `#0048AB`, `#01409C`) |
| Botão principal | degradê de `#0180FC` a `#005BCF` |
| Texto | `#CBD5E1`; secundário `#94A3B8` |
| Prata do monograma | `#FDFCFD`, `#D1D0D0`, `#959494` |

## Fontes oficiais

- **Unnar (app):** títulos em serifa, Georgia, com Gelasio onde a Georgia não existe (Android).
  Texto na fonte do sistema (`-apple-system`, `Segoe UI`, `system-ui`). Na landing é igual, sem o
  Gelasio.
- **Unnar (vídeo de 90 s):** títulos em Montserrat (600 e 700) e texto em Inter.
- **Unnar (logo):** o "UNNAR" e o símbolo são desenho vetorial, não uma fonte. Use os SVG, não
  digite o nome.
- **Vorinn (site):** títulos em **Sora** semibold e texto em Inter.
- **Vorinn (logo):** o "VORINN" e o slogan também são desenho (PNG), não fonte.

# Divergências

1. **O símbolo do Unnar não é um "U".** Desde 2026-10-03 o logo do app é o "N" dourado com a barra
   por cima (`unnar-marca-*.svg`). As artes desenham um "U" em Gelasio num quadrado
   (`scripts/render.py`: `.u .brand .mk`) e um "U" gigante de marca-d'água (`.wm-u`). O nome nas artes
   é "Unnar" em Gelasio; o oficial é "UNNAR" em caixa alta, no desenho do logo (`unnar-nome-*.svg`).
   O "Un**nar**" em Georgia com "nar" dourado é o texto do cabeçalho da landing
   (`unnar-landpage`: `app/_components/nav.tsx`), que ainda não usa o logo. Sugestão: nas artes, trocar o
   `.mk` + `.nm` pelo `unnar-horizontal-fundo-escuro.svg` e a marca-d'água pelo
   `unnar-marca-fundo-escuro.svg` com opacidade baixa.
2. **Fonte dos títulos da Vorinn:** o `PROJETO.md` diz "Inter Display SemiBold", e o site usa Sora
   semibold (com Inter de reserva). O `render.py` usa `'Inter Display'`.
3. **Itálico dourado (Unnar):** bate com o app, que destaca palavras do título em itálico na cor
   primária (por exemplo, a saudação do painel: "Olá, *nome*"). A landing não usa itálico, e o vídeo
   destaca as palavras com degradê dourado em Montserrat negrito. Não é erro, só para saber de onde
   vem.
4. **Cores:** as do `PROJETO.md` batem com o código, para as duas marcas. Os únicos complementos são
   os da tabela acima: o dourado `#E0B84A` e o degradê do símbolo do Unnar, e o azul do botão
   da Vorinn, `#0180FC` → `#005BCF`.
5. **Pedido diz "o 'U'" e "monograma 'VW'":** o primeiro é o "N" com a barra (item 1). O da Vorinn é o
   "V" prata com a fita azul: o arquivo é o monograma do logo original, como pedido.
