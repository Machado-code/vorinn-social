# Receita: Reels "Mesa de controle"

Aprovado pelo Matheus em 27/11/2026. Exemplo pronto: `reels/2026-12/reel-02-mesa-de-controle.mp4`.
Modelo para copiar: `reels/modelos/mesa-de-controle.html`.

## A ideia
O Unnar vira um objeto: um console numa mesa, com a marca na tampa e encaixes numerados.
Cada recurso é um cartucho que cai e encaixa. No fim, a tela do console liga e vira um
cartão com a tela real do Unnar. Explica o produto em segundos, sem voz.

## Estrutura (15 a 20 s)
1. **Gancho (0 a 2,5 s):** o console já aparece no primeiro quadro, com a legenda da dor.
   O primeiro quadro é a capa no feed, então nada de tela vazia.
2. **Peças (2 s cada):** o cartucho cai, encaixa, acende o slot, a luz da tampa e a
   etiqueta "N · Nome". Uma frase por peça.
3. **Tela real (2,5 a 5 s):** a tela do console liga e vira o cartão com a tela real, com
   destaque no que a legenda fala. Pode ser imagem ou um trecho das gravações do
   escritório (`assets/unnar/gravacoes/*.mp4`; para vídeo, use o `seek` do Reel 1, que
   também posiciona os `<video>`).
4. **Fechamento (2,7 s):** marca do Unnar, "Gerencie menos. *Crie mais.*", botão
   "Conheça o Unnar · link na bio" e "um produto Vorinn".

## Série de quarta
Um recurso por semana, sempre o mesmo console, para o público reconhecer. O episódio
começa com os cartuchos das semanas anteriores já encaixados e o da semana cai.
A fila de episódios fica em `pautas/fila.md`.

## Legenda na tela
- Inter 600 58 px, creme, centralizada em `top: 1300px` (fora da área do botão do Instagram).
- Uma palavra-chave por frase, em Gelasio itálico dourado, dentro da caixa de seleção.
- Palavras entram a cada 0,15 a 0,17 s; a frase some 0,2 s antes da próxima cena.
- Frase curta: precisa caber em uma linha (até ~28 caracteres) ou em duas no máximo.

## Regras técnicas (evitam os erros que já aconteceram)
- Nunca animar `transform` num elemento que já usa `transform` para se posicionar em 3D:
  a animação apaga a posição. Anime `opacity` ou a propriedade `translate`
  (ex.: `rise` das etiquetas), ou anime um filho.
- Elementos com `opacity` menor que 1 achatam o 3D dos filhos: não use opacidade em
  grupos `preserve-3d` (os cartuchos ficam fora da tela até cair, com `visibility`).
- Etiquetas e faíscas "de frente para a câmera": depois do `translate3d`, desfaça a câmera
  na ordem `rotateZ(-θ) rotateX(-φ)`, com θ e φ da câmera naquele instante.
- Marca na tampa: `rotate(-26deg) scaleY(1.8)` para o "N" ler de frente. O símbolo do
  Unnar é o "N" com a barra, nunca "U".
- Animação com `fill-mode: both` mostra o quadro 0% antes de começar: o 0% de anéis e
  brilhos tem que ser `opacity: 0`.
- Telas reais: recorte sem a barra lateral (logo antiga) e sem a coluna com endereço.
  Seguir "O que os textos podem e não podem dizer" do `PROJETO.md`.

## Como gerar
```bash
# conferir quadros nos momentos mais cheios antes do vídeo inteiro
CHROME_PATH=/usr/bin/google-chrome python3 scripts/render_reel.py <html> frames /tmp/q <dur> 0.9 3.4 7.4 12.2
# vídeo (cerca de 2 min para 15 s)
CHROME_PATH=/usr/bin/google-chrome python3 scripts/render_reel.py <html> video /tmp/video.mp4 <dur>
# trilha: um "tique" em cada encaixe e na troca de cena
python3 scripts/make_audio.py /tmp/audio.wav <dur> 0.1,3.0,5.0,7.0,9.0,10.45,10.95,12.95,13.9
ffmpeg -i /tmp/video.mp4 -i /tmp/audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -shortest -movflags +faststart <saida>.mp4
```

## Publicação
- Buffer: `type: reel`, `shouldShareToFeed: true`, quarta às 19h, link raw fixado no commit.
- Texto do post: a dor em uma frase, o que o Unnar resolve, chamada para o WhatsApp do
  link da bio, até 4 hashtags do nicho.
- Medir depois de 4 semanas contra o Reel 1 (tela gravada): alcance, retenção média,
  salvamentos e compartilhamentos.
