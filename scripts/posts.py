# Conteúdo dos 9 primeiros posts do @vorinn (lote 1)
# Cada post: id, marca ('v' = Vorinn, 'u' = Unnar), título interno, slides (HTML do miolo) e legenda.

import pathlib
A = (pathlib.Path(__file__).resolve().parent.parent / "assets" / "capturas-do-site").as_uri() + "/"

def shot_note(t="Tela real do Unnar, com dados de exemplo."):
    return f'<div class="note">{t}</div>'

POSTS = [
# ------------------------------------------------------------------ 1
{
 "id": "01-prazer-vorinn", "brand": "v", "title": "Prazer, Vorinn",
 "slides": [
  f'''<div class="pill">Tecnologia · Inovação · Soluções</div>
  <h1 class="mt40">Tecnologia que <span class="acc">conecta, organiza</span> e transforma.</h1>
  <p class="lead mt40">Sistemas, automações e IA sob medida para empresas e profissionais.</p>
  <img class="mono-hero" src="{A}vorinn-monograma-alpha.png">''',

  '''<div class="pill">O que eu faço</div>
  <h2 class="mt32">Tecnologia sob medida para o seu negócio <span class="acc">ir além</span>.</h2>
  <div class="list mt48">
   <div class="item"><div class="num">01</div><div><h3>Sistemas sob medida</h3><p>Sistemas web, aplicativos e painéis internos.</p></div></div>
   <div class="item"><div class="num">02</div><div><h3>Automação de processos</h3><p>Fluxos, relatórios e integração com WhatsApp e e-mail.</p></div></div>
   <div class="item"><div class="num">03</div><div><h3>Inteligência artificial</h3><p>Assistentes, agentes e geração de documentos.</p></div></div>
   <div class="item"><div class="num">04</div><div><h3>Sites que convertem</h3><p>Landing pages e sites institucionais com foco em SEO.</p></div></div>
  </div>''',

  '''<div class="pill">Produtos próprios</div>
  <h2 class="mt32">Soluções prontas para <span class="acc">acelerar</span> o seu negócio.</h2>
  <div class="card mt48"><div class="card-tag">Unnar</div><h3>Gestão operacional para empresas de eventos e fotografia</h3><p>Clientes, eventos e equipe num só lugar. unnar.com.br</p></div>
  <div class="card mt32"><div class="card-tag">IA jurídica</div><h3>Petições iniciais com IA para escritórios de advocacia</h3><p>Entregues em Word, com a revisão final feita pelo advogado.</p></div>''',

  '''<div class="pill">Como eu trabalho</div>
  <h2 class="mt32">Mais que código: uma <span class="acc">parceria</span>.</h2>
  <div class="steps mt48">
   <div class="step"><span>1</span>Diagnóstico</div>
   <div class="step"><span>2</span>Planejamento</div>
   <div class="step"><span>3</span>Desenvolvimento em ciclos curtos</div>
   <div class="step"><span>4</span>Entrega e evolução contínua</div>
  </div>
  <div class="cta mt56"><div class="btn">Fale direto com quem desenvolve</div><div class="cta-sub">Link do WhatsApp na bio</div></div>''',
 ],
 "caption": """Prazer, Vorinn. 👋

Eu desenvolvo sistemas, automações e soluções com IA sob medida para empresas e profissionais, do primeiro esboço ao sistema rodando.

Por aqui você vai ver:
→ o Unnar, o sistema de gestão que criei para empresas de eventos e fotografia
→ automações que tiram o trabalho repetitivo da rotina
→ IA aplicada a problemas reais

Tem uma ideia ou um processo que toma tempo demais? O link do WhatsApp está na bio, e você fala direto com quem desenvolve.

#desenvolvimentodesoftware #automacao #inteligenciaartificial #sistemasobmedida""",
},
# ------------------------------------------------------------------ 2
{
 "id": "02-conheca-o-unnar", "brand": "u", "title": "Conheça o Unnar",
 "slides": [
  f'''<div class="eyebrow">Para empresas de eventos e fotografia</div>
  <h1 class="mt32">Gerencie menos.<br><em>Crie mais.</em></h1>
  <p class="lead mt32">Conheça o Unnar.</p>
  <img class="shot shot-cover" src="{A}unnar-painel.png">''',

  '''<div class="eyebrow">Como funciona</div>
  <h2 class="mt32">Clientes, eventos e equipe <em>num só lugar</em>.</h2>
  <div class="two mt56">
   <div class="card"><div class="card-tag">Painel</div><h3>No computador, para a gestão</h3><p>Clientes, eventos, equipe, presença e despesas.</p></div>
   <div class="card"><div class="card-tag">Portal</div><h3>No celular, para a equipe</h3><p>Agenda, confirmação de presença, check-in e despesas.</p></div>
  </div>
  <p class="lead mt48">Funciona no navegador, no computador e no celular.</p>''',

  f'''<div class="eyebrow">O painel da empresa</div>
  <h2 class="mt32">Tudo o que importa <em>em uma tela</em>.</h2>
  <p class="lead mt32">Clientes, equipe e próximos eventos, com atalhos para criar evento, cliente ou convidar alguém.</p>
  <img class="shot shot-wide mt56" src="{A}unnar-painel.png">
  {shot_note()}''',

  f'''<div class="row">
   <div class="col-text">
    <div class="eyebrow">O portal da equipe</div>
    <h2 class="mt32">A agenda <em>no bolso</em> de quem trabalha no evento.</h2>
    <p class="lead mt32">Confirmar presença, fazer check-in e lançar despesas pelo celular.</p>
   </div>
   <div class="phone"><img src="{A}unnar-portal-celular.png"></div>
  </div>
  {shot_note()}''',

  '''<div class="eyebrow">Veja funcionando</div>
  <h2 class="mt32">Quer ver o Unnar <em>na prática</em>?</h2>
  <p class="lead mt40">Tem um vídeo de 90 segundos com as telas reais em <strong>unnar.com.br</strong>.</p>
  <p class="lead mt24">Para conhecer os planos, me chame no WhatsApp.</p>
  <div class="cta mt56"><div class="btn">Link do WhatsApp na bio</div></div>''',
 ],
 "caption": """Gerencie menos. Crie mais.

O Unnar é o sistema que eu criei para empresas de eventos e fotografia organizarem a operação:

📋 clientes com contatos, anotações e histórico de eventos
📅 eventos do orçamento à entrega, com checklist e serviços do pacote
👥 equipe escalada com função e cachê
📱 portal no celular para a equipe confirmar presença, fazer check-in e lançar despesas

Funciona no navegador, no computador e no celular. As telas do post são reais, com dados de exemplo.

Quer conhecer os planos? Me chame no WhatsApp pelo link da bio.

#gestaodeeventos #empresadeeventos #fotografiadeeventos #fotografodecasamento""",
},
# ------------------------------------------------------------------ 3
{
 "id": "03-quem-confirmou", "brand": "u", "title": "Quem já confirmou?",
 "slides": [
  '''<div class="eyebrow">Sábado, 15h</div>
  <h1 class="mt32">O casamento começa às 16h.<br><em>Quem da equipe já confirmou?</em></h1>''',

  '''<h2>Se a resposta está espalhada por aí…</h2>
  <div class="list mt56">
   <div class="item"><div class="num">i.</div><div><p class="big">A confirmação ficou perdida no grupo do WhatsApp.</p></div></div>
   <div class="item"><div class="num">ii.</div><div><p class="big">O cachê de cada um está numa planilha.</p></div></div>
   <div class="item"><div class="num">iii.</div><div><p class="big">A despesa do evento virou foto no celular de alguém.</p></div></div>
  </div>''',

  '''<h1>…a operação depende da <em>sua memória</em>.</h1>
  <p class="lead mt48">E memória não dá conta de vários eventos no mesmo fim de semana.</p>''',

  f'''<div class="row">
   <div class="col-text">
    <div class="eyebrow">No Unnar</div>
    <h2 class="mt32">Presença <em>registrada</em>, não cobrada.</h2>
    <p class="lead mt32">A equipe confirma e faz check-in pelo celular, cada registro com data e hora. No painel, você vê quem já chegou.</p>
   </div>
   <div class="phone"><img src="{A}unnar-portal-celular.png"></div>
  </div>
  {shot_note()}''',

  '''<h1>Menos mensagem cobrando.<br><em>Mais tempo para o evento.</em></h1>
  <div class="cta mt56"><div class="btn">Conheça o Unnar · link na bio</div></div>''',
 ],
 "caption": """Sábado, 15h. O evento começa às 16h e você ainda está rolando o grupo para descobrir quem confirmou. 😅

Quando confirmação, cachê e despesa ficam espalhados entre grupo, planilha e foto no celular, a operação passa a depender da memória de alguém.

No Unnar, cada profissional confirma presença e faz check-in pelo celular, com data e hora registradas. No painel, você vê quem já chegou, sem precisar perguntar.

Se isso parece a sua rotina, me chame no WhatsApp pelo link da bio.

#empresadeeventos #assessoriadeeventos #fotografiadeeventos #gestaodeeventos""",
},
# ------------------------------------------------------------------ 4
{
 "id": "04-do-orcamento-a-entrega", "brand": "u", "title": "Do orçamento à entrega",
 "slides": [
  '''<div class="eyebrow">Do orçamento à entrega</div>
  <h1 class="mt32">Cada evento com <em>tudo no mesmo lugar</em>.</h1>''',

  f'''<div class="eyebrow">Status à vista</div>
  <h2 class="mt32">Em que pé está <em>cada evento</em>?</h2>
  <p class="lead mt32">Orçamento, contratado, em planejamento, em andamento: dá para ver de relance.</p>
  <img class="shot shot-crop mt56" src="{A}unnar-painel-eventos.png">
  {shot_note()}''',

  '''<h2>Dentro de cada evento:</h2>
  <div class="list mt48">
   <div class="item"><div class="num">i.</div><div><h3>Status</h3><p>Do orçamento à entrega.</p></div></div>
   <div class="item"><div class="num">ii.</div><div><h3>Checklist de preparação</h3><p>Nada esquecido na véspera.</p></div></div>
   <div class="item"><div class="num">iii.</div><div><h3>Serviços do pacote</h3><p>O que foi vendido, registrado no evento.</p></div></div>
   <div class="item"><div class="num">iv.</div><div><h3>Equipe escalada</h3><p>Com a função e o cachê de cada um.</p></div></div>
  </div>''',

  '''<h1>Em lista ou <em>no calendário</em>.</h1>
  <p class="lead mt40">Do jeito que você prefere enxergar a sua agenda de eventos.</p>
  <div class="cta mt56"><div class="btn">Conheça o Unnar · link na bio</div></div>''',
 ],
 "caption": """Orçamento enviado, contrato fechado, equipe escalada, evento entregue. Cada etapa no mesmo lugar.

No Unnar, cada evento tem:
✔️ status do orçamento à entrega
✔️ checklist de preparação
✔️ serviços do pacote
✔️ equipe escalada, com função e cachê

E você escolhe ver a agenda em lista ou no calendário.

Quer ver como fica com os seus eventos? Me chame no WhatsApp pelo link da bio.

#gestaodeeventos #empresadeeventos #cerimonialista #fotografiadeeventos""",
},
# ------------------------------------------------------------------ 5
{
 "id": "05-automacao", "brand": "v", "title": "O que dá para automatizar",
 "slides": [
  '''<div class="pill">Automação de processos</div>
  <h1 class="mt40">Tarefas que <span class="acc">não deveriam</span> tomar o seu dia.</h1>
  <p class="lead mt40">4 exemplos do que dá para automatizar.</p>''',

  '''<div class="list">
   <div class="item"><div class="num">01</div><div><h3>Documentos no lugar certo</h3><p>O que chega pelo WhatsApp e pelo e-mail vai direto para a pasta do cliente.</p></div></div>
   <div class="item"><div class="num">02</div><div><h3>Relatórios que se montam sozinhos</h3><p>Planilhas e relatórios atualizados sem ninguém copiar dado.</p></div></div>
   <div class="item"><div class="num">03</div><div><h3>Sistemas que conversam</h3><p>Integração entre sistemas e APIs, sem retrabalho.</p></div></div>
   <div class="item"><div class="num">04</div><div><h3>IA no fluxo</h3><p>Leitura e geração de documentos dentro do processo que você já tem.</p></div></div>
  </div>''',

  '''<div class="pill">Por onde começar</div>
  <h2 class="mt32">Qual tarefa mais toma o tempo da sua equipe?</h2>
  <p class="lead mt40">Me conte. Eu analiso o processo e digo o que dá para automatizar.</p>
  <div class="cta mt56"><div class="btn">Fale direto com quem desenvolve</div><div class="cta-sub">Link do WhatsApp na bio</div></div>''',
 ],
 "caption": """Se alguém da sua equipe passa horas copiando, colando e procurando arquivo, essa tarefa provavelmente pode ser automatizada.

Alguns exemplos que eu desenvolvo:
→ documentos que chegam pelo WhatsApp e pelo e-mail indo direto para a pasta certa
→ relatórios e planilhas que se atualizam sozinhos
→ sistemas que conversam entre si
→ IA lendo e gerando documentos dentro do seu processo

Qual tarefa mais toma o tempo da sua equipe? Me conte no WhatsApp (link na bio).

#automacao #produtividade #automacaodeprocessos #inteligenciaartificial""",
},
# ------------------------------------------------------------------ 6
{
 "id": "06-freelancer-agenda-unica", "brand": "u", "title": "Uma agenda só",
 "slides": [
  '''<div class="eyebrow">Para fotógrafos e freelancers</div>
  <h1 class="mt32">Trabalha para várias empresas?<br><em>Sua agenda pode ser uma só.</em></h1>''',

  f'''<div class="row">
   <div class="col-text">
    <h2>Uma conta, <em>várias empresas</em>.</h2>
    <p class="lead mt32">Os eventos de todas as empresas que te contratam numa lista só, cada um com o nome da empresa.</p>
   </div>
   <div class="phone"><img src="{A}unnar-portal-celular.png"></div>
  </div>
  {shot_note()}''',

  '''<h2>Tudo pelo celular:</h2>
  <div class="list mt48">
   <div class="item"><div class="num">i.</div><div><h3>Confirmar presença</h3><p>Sem precisar responder no grupo.</p></div></div>
   <div class="item"><div class="num">ii.</div><div><h3>Check-in e check-out</h3><p>Com data e hora registradas.</p></div></div>
   <div class="item"><div class="num">iii.</div><div><h3>Lançar despesas</h3><p>O que você gastou no evento, direto no portal.</p></div></div>
   <div class="item"><div class="num">iv.</div><div><h3>Receber avisos</h3><p>Novas escalas chegam no sino.</p></div></div>
  </div>''',

  '''<h1>Conhece uma empresa que ainda escala a equipe pelo grupo?</h1>
  <p class="lead mt48"><strong>Mande este post para ela.</strong></p>''',
 ],
 "caption": """Fotógrafo, filmmaker, assistente: se você trabalha para mais de uma empresa, sabe como é ter uma agenda em cada grupo.

No Unnar, uma conta só mostra os eventos de todas as empresas que te contratam, numa lista, cada um com o nome da empresa. Pelo celular você confirma presença, faz check-in e check-out e lança despesas.

Conhece uma empresa que ainda escala a equipe pelo grupo do WhatsApp? Mande este post para ela. 😉

#fotografodecasamento #fotografodeeventos #freelancer #fotografiadeeventos""",
},
# ------------------------------------------------------------------ 7
{
 "id": "07-dados-separados", "brand": "u", "title": "Seus dados, só seus",
 "slides": [
  '''<div class="eyebrow">Segurança</div>
  <h1 class="mt32">Os dados da sua empresa são <em>só da sua empresa</em>.</h1>''',

  '''<h2>No Unnar, <em>cada empresa tem o próprio banco de dados</em>.</h2>
  <p class="lead mt40">Uma empresa não acessa os dados de outra. Seus clientes, valores e equipe ficam separados.</p>
  <div class="list mt48">
   <div class="item"><div class="num">i.</div><div><h3>Funciona no navegador</h3><p>No computador e no celular.</p></div></div>
   <div class="item"><div class="num">ii.</div><div><h3>Tema claro ou escuro</h3><p>Do jeito que for melhor para ler.</p></div></div>
  </div>''',

  '''<h1>Organização <em>com tranquilidade</em>.</h1>
  <div class="cta mt56"><div class="btn">Conheça o Unnar · link na bio</div></div>''',
 ],
 "caption": """Lista de clientes, valores de pacote, cachê da equipe: são dados que você não quer misturados com os de ninguém.

No Unnar, cada empresa tem o próprio banco de dados. Uma empresa não acessa os dados de outra, nem quando o mesmo profissional trabalha para as duas.

E funciona no navegador, no computador e no celular, com tema claro ou escuro.

Quer conhecer? Link do WhatsApp na bio.

#gestaodeeventos #empresadeeventos #segurancadedados #fotografiadeeventos""",
},
# ------------------------------------------------------------------ 8
{
 "id": "08-ia-advocacia", "brand": "v", "title": "IA para escritórios de advocacia",
 "slides": [
  '''<div class="pill">IA para escritórios de advocacia</div>
  <h1 class="mt40">Da pasta do cliente à <span class="acc">petição inicial</span>, com IA.</h1>''',

  '''<h2>Como funciona:</h2>
  <div class="list mt48">
   <div class="item"><div class="num">01</div><div><h3>Os documentos do cliente</h3><p>O escritório reúne o material do caso.</p></div></div>
   <div class="item"><div class="num">02</div><div><h3>A IA redige</h3><p>A petição inicial é gerada a partir dos documentos.</p></div></div>
   <div class="item"><div class="num">03</div><div><h3>Entregue em Word</h3><p>Pronta para revisar e ajustar.</p></div></div>
   <div class="item"><div class="num">04</div><div><h3>O advogado revisa</h3><p>A revisão final é sempre de quem assina.</p></div></div>
  </div>''',

  '''<h1>Menos tempo digitando. <span class="acc">Mais tempo para a estratégia.</span></h1>
  <div class="cta mt56"><div class="btn">Fale direto com quem desenvolve</div><div class="cta-sub">Link do WhatsApp na bio</div></div>''',
 ],
 "caption": """Montar a petição inicial a partir dos documentos do cliente toma horas que poderiam ir para a estratégia do caso.

Desenvolvi uma solução com IA para escritórios de advocacia: ela lê os documentos do cliente e gera a petição inicial, entregue em Word. A revisão final é sempre do advogado.

Tem um escritório e quer ver funcionando? Me chame no WhatsApp pelo link da bio.

#advocacia #direito #inteligenciaartificial #tecnologianodireito""",
},
# ------------------------------------------------------------------ 9
{
 "id": "09-despesas-e-avisos", "brand": "u", "title": "Quanto a equipe gastou?",
 "slides": [
  '''<div class="eyebrow">Depois do evento</div>
  <h1 class="mt32">Quanto a equipe <em>gastou</em> no evento?</h1>''',

  '''<h2>Depois do evento, <em>tudo registrado</em>.</h2>
  <div class="card mt56"><div class="card-tag">Despesas</div><h3>Lançou, apareceu no painel</h3><p>Quem gastou algo para o evento registra pelo celular. A empresa vê quem lançou, o quê e quanto, com data e hora.</p></div>
  <div class="card mt32"><div class="card-tag">Avisos</div><h3>Ninguém fica sem saber</h3><p>Avisos no sino, dos dois lados: a equipe recebe as escalas, a empresa recebe presença e despesas.</p></div>''',

  '''<h1>Gerencie menos.<br><em>Crie mais.</em></h1>
  <p class="lead mt40">unnar.com.br</p>
  <div class="cta mt48"><div class="btn">Conheça os planos · link na bio</div></div>''',
 ],
 "caption": """Estacionamento, almoço da equipe, um item que faltou no dia: despesa de evento costuma virar foto perdida no celular.

No Unnar, quem gastou registra pelo portal no celular. A empresa vê quem lançou, o quê e quanto, cada registro com data e hora.

E os avisos chegam no sino dos dois lados: a equipe recebe as escalas, a empresa recebe presença e despesas.

Quer conhecer os planos? Me chame no WhatsApp pelo link da bio.

#gestaodeeventos #empresadeeventos #fotografiadeeventos #gestaofinanceira""",
},
]
