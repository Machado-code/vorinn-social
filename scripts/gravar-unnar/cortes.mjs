// Refaz os clipes e as telas paradas de assets/unnar/gravacoes/ a partir de arquivos locais:
//   - o vídeo de apresentação do Unnar (90 s, 1920×1080) → cortes 16:9 do painel da empresa;
//   - as capturas das telas (PNG) e o meta.js delas → clipes verticais 1080×1920 do portal e os PNG.
// Não abre o sistema, não usa rede nem senha: só ffmpeg sobre arquivos que já existem na máquina.
//
// Uso (Node 18+, sem dependências):
//   node scripts/gravar-unnar/cortes.mjs --video <mp4 de 90 s> --capturas <pasta com os PNG e o meta.js>
//        [--ffmpeg <executável do ffmpeg>] [--saida <pasta>] [--so <nome,nome>]
// Também por variável: UNNAR_VIDEO, UNNAR_CAPTURAS, FFMPEG. A saída padrão é assets/unnar/gravacoes.
import { spawnSync } from "node:child_process"
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs"
import { dirname, join, resolve } from "node:path"
import { fileURLToPath } from "node:url"

// ── Argumentos ────────────────────────────────────────────────────────────────────────────────
const args = process.argv.slice(2)
const arg = (nome, env) => {
  const i = args.indexOf(`--${nome}`)
  return i >= 0 ? args[i + 1] : process.env[env]
}
const VIDEO = arg("video", "UNNAR_VIDEO")
const CAPTURAS = arg("capturas", "UNNAR_CAPTURAS")
const FFMPEG = arg("ffmpeg", "FFMPEG") ?? "ffmpeg"
const RAIZ = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..")
const SAIDA = resolve(arg("saida", "UNNAR_SAIDA") ?? join(RAIZ, "assets", "unnar", "gravacoes"))
const SO = (arg("so", "UNNAR_SO") ?? "").split(",").filter(Boolean)
if (!VIDEO || !CAPTURAS) {
  console.error("Informe --video <mp4 de 90 s> e --capturas <pasta das capturas> (ou UNNAR_VIDEO e UNNAR_CAPTURAS).")
  process.exit(2)
}
for (const p of [VIDEO, join(CAPTURAS, "meta.js")]) if (!existsSync(p)) { console.error(`Não encontrado: ${p}`); process.exit(2) }
mkdirSync(SAIDA, { recursive: true })

// meta.js: window.SHOTS = { "<captura>": { w, h, dpr, boxes: { nome: { x, y, w, h } }, rolagem? } }
const metaTxt = readFileSync(join(CAPTURAS, "meta.js"), "utf8")
const META = JSON.parse(metaTxt.slice(metaTxt.indexOf("{"), metaTxt.lastIndexOf("}") + 1))
const cap = id => join(CAPTURAS, `${id}.png`)
const caixa = (id, nome) => {
  const b = META[id]?.boxes?.[nome]
  if (!b) throw new Error(`caixa ${id}/${nome} não está no meta.js`)
  return b
}

// ── Celular: 390×844 CSS @3x. Cabeçalho (0–56) e barra de baixo (772–844) ficam parados, como no
// aparelho; o conteúdo entre eles é o que rola ou muda de uma captura para outra.
const DPR = META["m-agenda"].dpr
const CW = 390 * DPR, CH = 844 * DPR
const TOPO = 56 * DPR, BARRA = 772 * DPR
const px = v => Math.round(v * DPR)
const FUNDO = "0x0E0D12" // fundo do tema escuro do app

const ffmpeg = (lista, nome) => {
  const r = spawnSync(FFMPEG, ["-hide_banner", "-loglevel", "error", "-y", "-filter_complex_threads", "2", ...lista], { stdio: "inherit" })
  if (r.status !== 0) throw new Error(`ffmpeg falhou em ${nome}`)
  console.log("✓", nome)
}
const H264 = ["-an", "-r", "30", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-threads", "2"]
const VERTICAL = `scale=888:1920:flags=lanczos,pad=1080:1920:96:0:color=${FUNDO},setsar=1,format=yuv420p`

// Toque: um círculo claro que aparece e some sobre o ponto tocado (o mesmo recurso do vídeo de 90 s).
function toque(rotulo, { x, y }, ini, fim, dur) {
  const R = 132
  const d = `hypot(X-${R},Y-${R})`
  return [
    `color=c=white@0:s=${2 * R}x${2 * R}:r=30:d=${dur},format=rgba,` +
      `geq=r=255:g=255:b=255:a='70*clip(66.5-${d},0,1)+210*clip(78.5-${d},0,1)*clip(${d}-65.5,0,1)',` +
      `fade=t=in:st=${ini}:d=0.12:alpha=1,fade=t=out:st=${fim - 0.3}:d=0.3:alpha=1[${rotulo}]`,
    { x: Math.round(x - R), y: Math.round(y - R) },
  ]
}
const centro = b => ({ x: px(b.x + b.w / 2), y: px(b.y + b.h / 2) })

// Sequência de telas inteiras com fusão entre elas (e toques opcionais).
// telas: [{ entrada: <rótulo de filtro ou índice de input>, dur }]; a fusão come FUSAO s de cada troca.
function sequencia(nome, inputs, preparo, telas, toques = [], FUSAO = 0.35) {
  const total = telas.reduce((s, t) => s + t.dur, 0) - FUSAO * (telas.length - 1)
  const f = [...preparo]
  // o xfade exige o mesmo formato, tamanho e base de tempo nas duas entradas
  telas.forEach((t, i) => f.push(`[${t.entrada}]format=yuv444p,setsar=1,settb=AVTB[s${i}]`))
  let atual = "s0", acc = telas[0].dur
  telas.slice(1).forEach((t, i) => {
    const sai = `x${i}`
    f.push(`[${atual}][s${i + 1}]xfade=transition=fade:duration=${FUSAO}:offset=${(acc - FUSAO).toFixed(3)}[${sai}]`)
    atual = sai
    acc += t.dur - FUSAO
  })
  toques.forEach(([alvo, ini, fim], i) => {
    const [src, pos] = toque(`t${i}`, alvo, ini, fim, total)
    f.push(src, `[${atual}][t${i}]overlay=${pos.x}:${pos.y}:eof_action=pass[o${i}]`)
    atual = `o${i}`
  })
  f.push(`[${atual}]${VERTICAL}[v]`)
  const entradas = inputs.flatMap(i => ["-loop", "1", "-framerate", "30", "-t", String(total + 1), "-i", i])
  ffmpeg([...entradas, "-filter_complex", f.join(";"), "-map", "[v]", "-t", total.toFixed(3), ...H264, join(SAIDA, `${nome}.mp4`)], `${nome}.mp4 (${total.toFixed(1)} s)`)
}

// Presença: as capturas estão em rolagens diferentes. Alinha a seguinte pela lista de etapas (como no
// vídeo): o conteúdo desce DY px e a faixa que sobra no topo vem da captura anterior, que é a mesma página.
const DY1 = px(caixa("m-presenca-0", "etapas").y - caixa("m-presenca-1", "etapas").y)
const DY2 = px(caixa("m-presenca-0", "etapas").y - caixa("m-presenca-2", "etapas").y)
// O recorte começa 2 px CSS abaixo do cabeçalho, para a borda dele não virar uma linha no meio da tela.
const MARGEM = 2 * DPR
const alinhada = (base, cima, dy, rotulo) => {
  if (dy < 0) throw new Error("rolagem negativa não prevista")
  return [
    `[${cima}]split=3[${rotulo}c][${rotulo}h][${rotulo}n]`,
    `[${rotulo}c]crop=${CW}:${BARRA - TOPO - MARGEM - dy}:0:${TOPO + MARGEM}[${rotulo}cc]`,
    `[${rotulo}h]crop=${CW}:${TOPO}:0:0[${rotulo}hh]`,
    `[${rotulo}n]crop=${CW}:${CH - BARRA}:0:${BARRA}[${rotulo}nn]`,
    `[${base}][${rotulo}cc]overlay=0:${TOPO + MARGEM + dy}[${rotulo}a]`,
    `[${rotulo}a][${rotulo}hh]overlay=0:0[${rotulo}b]`,
    `[${rotulo}b][${rotulo}nn]overlay=0:${BARRA}[${rotulo}]`,
  ]
}

const CLIPES = {
  // 1. Agenda: rolagem real da lista (eventos da Aurora Fotografia e da Bruma Eventos).
  "portal-01-agenda-duas-empresas": () => {
    const ROL = px(META["m-agenda-baixo"].rolagem) // quanto a lista rola até o fim
    const barraNaPagina = px(Math.floor(caixa("m-agenda-full", "barra").y)) // a barra fixa ficou "impressa" no meio da captura de página inteira
    const conteudo = BARRA - TOPO
    const ease = `(0.5-0.5*cos(PI*clip((t-1.0)/2.6,0,1)))`
    const total = 6.0
    const f = [
      `[0]split[ag1][ag2]`,
      `[ag1]crop=${CW}:${TOPO}:0:0[cab]`,
      `[ag2]crop=${CW}:${CH - BARRA}:0:${BARRA}[bar]`,
      // tapa a barra impressa com o mesmo trecho da captura rolada (mesma página, mesmo estado)
      `[2]crop=${CW}:${CH - BARRA}:0:${barraNaPagina - ROL}[remendo]`,
      `[1][remendo]overlay=0:${barraNaPagina}[pagina]`,
      `[pagina]crop=${CW}:${conteudo}:0:'${TOPO}+${ROL}*${ease}',pad=${CW}:${CH}:0:${TOPO}:color=${FUNDO}[rola]`,
      `[rola][cab]overlay=0:0[r1]`,
      `[r1][bar]overlay=0:${BARRA},${VERTICAL}[v]`,
    ]
    const entradas = [cap("m-agenda"), cap("m-agenda-full"), cap("m-agenda-baixo")]
      .flatMap(i => ["-loop", "1", "-framerate", "30", "-t", String(total + 1), "-i", i])
    ffmpeg([...entradas, "-filter_complex", f.join(";"), "-map", "[v]", "-t", String(total), ...H264, join(SAIDA, "portal-01-agenda-duas-empresas.mp4")], `portal-01-agenda-duas-empresas.mp4 (${total} s)`)
  },
  // 2. Confirmar presença: toque em "Confirmar presença" → etapa "Confirmado" com data e hora.
  "portal-02-confirmar-presenca": () =>
    sequencia("portal-02-confirmar-presenca", [cap("m-presenca-0"), cap("m-presenca-1")],
      [`[0]split[p0a][p0b]`, ...alinhada("p0b", "1", DY1, "p1")],
      [{ entrada: "p0a", dur: 1.9 }, { entrada: "p1", dur: 3.3 }],
      [[centro(caixa("m-presenca-0", "botao")), 0.9, 1.75]]),
  // 3. Check-in: toque em "Fazer check-in" → etapa "Check-in" com data e hora; o próximo passo é o check-out.
  "portal-03-check-in": () =>
    sequencia("portal-03-check-in", [cap("m-presenca-0"), cap("m-presenca-1"), cap("m-presenca-2")],
      [...alinhada("0", "1", DY1, "p1"), ...(DY2 === 0 ? [`[2]null[p2]`] : alinhada("0", "2", DY2, "p2"))],
      [{ entrada: "p1", dur: 1.9 }, { entrada: "p2", dur: 3.3 }],
      [[{ ...centro(caixa("m-presenca-1", "botao")), y: centro(caixa("m-presenca-1", "botao")).y + DY1 }, 0.9, 1.75]]),
  // 4. Despesa: formulário vazio → preenchido → a despesa na lista do evento.
  "portal-04-lancar-despesa": () =>
    sequencia("portal-04-lancar-despesa", [cap("m-despesa-vazia"), cap("m-despesa"), cap("m-despesas")], [],
      [{ entrada: "0", dur: 1.4 }, { entrada: "1", dur: 2.2 }, { entrada: "2", dur: 2.8 }]),
  // 5. Sino: toque no sino da agenda → avisos de escala, com o nome de cada empresa.
  "portal-05-aviso-de-escala-no-sino": () =>
    sequencia("portal-05-aviso-de-escala-no-sino", [cap("m-agenda"), cap("m-sino")], [],
      [{ entrada: "0", dur: 1.6 }, { entrada: "1", dur: 3.4 }],
      [[centro(caixa("m-agenda", "sino")), 0.8, 1.5]], 0.3),
}

// Cortes 16:9 do vídeo de 90 s (início e duração em segundos; ver o roteiro do vídeo).
const CORTES = {
  "painel-06-dashboard": [11.0, 7.5],
  "painel-07-evento-aberto": [30.4, 8.0],
  "painel-08-presenca-e-despesa": [61.8, 8.0],
  "painel-09-agenda-calendario": [27.6, 4.2],
}

// Telas paradas: a captura original, tema escuro (celular 1170×2532; painel 2880×1800 ou página inteira).
const TELAS = {
  "portal-01-agenda-duas-empresas": "m-agenda-baixo",
  "portal-02-confirmar-presenca": "m-presenca-0",
  "portal-03-check-in": "m-presenca-2",
  "portal-04-lancar-despesa": "m-despesa",
  "portal-05-aviso-de-escala-no-sino": "m-sino",
  "painel-06-dashboard": "d-dashboard",
  "painel-07-evento-aberto": "d-evento",
  "painel-08-presenca-no-painel": "d-hoje",
  "painel-08-despesas-no-painel": "d-despesas",
  "painel-09-agenda-calendario": "d-calendario",
}

const quer = n => SO.length === 0 || SO.some(s => n.startsWith(s))
for (const [nome, fazer] of Object.entries(CLIPES)) if (quer(nome)) fazer()
for (const [nome, [ini, dur]] of Object.entries(CORTES)) {
  if (!quer(nome)) continue
  ffmpeg(["-ss", String(ini), "-t", String(dur), "-i", VIDEO, ...H264, join(SAIDA, `${nome}.mp4`)], `${nome}.mp4 (${dur} s)`)
}
for (const [nome, id] of Object.entries(TELAS)) {
  if (!quer(nome)) continue
  copyFileSync(cap(id), join(SAIDA, `${nome}.png`))
  console.log("✓", `${nome}.png`)
}
