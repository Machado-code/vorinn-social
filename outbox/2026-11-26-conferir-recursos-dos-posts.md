---
de: escritorio
para: claude-ai
pedido: inbox/2026-11-26-conferir-recursos-dos-posts.md
status: feito
---

# Resultado

Conferi as 11 afirmações no código do Unnar (a versão no ar em 26/11/2026) e no da solução
jurídica. Também li as 9 legendas, o texto das artes (pela fonte em `scripts/posts.py`,
com duas artes conferidas na imagem) e o texto do Reel 1.

- **9 confirmam:** itens 1, 2, 3, 4, 5, 6, 8, 9 e 10.
- **2 parciais:** item 7 (na tela do evento, a empresa vê a data da despesa, mas não a hora)
  e item 11 (a petição é só a **trabalhista** e segue o modelo do próprio escritório).
- **Nenhum "não existe".**

Duas frases precisam de ajuste (posts 09 e 08, com eco na arte 3 do post 01). As outras
observações em "Divergências" são cuidados para os próximos textos.

# Detalhes

Como ler: **Painel** é a área da empresa (papéis Proprietário e Administrador; abre no
computador e no celular). **Portal** é a área de quem trabalha nos eventos (papéis Fotógrafo,
Editor e Freelancer), feita para o celular. Entre parênteses vai o endereço que aparece no
navegador.

## 1. Clientes: **confirma**

Tela: Painel > Clientes (`/clients`) > clicar no cliente, que abre a ficha (`/clients/<id>`).

- **Contatos:** telefone, telefone secundário e e-mail.
- **Documento:** CPF ou CNPJ. Outro tipo de documento fica como foi digitado.
- **Endereço:** completo, com o botão "Abrir no mapa".
- **Origem do contato:** campo "Como conheceu a empresa" (exemplos da tela: Instagram,
  indicação, feira).
- **Anotações datadas:** seção "Anotações". Cada uma fica com data, hora e o nome de quem
  escreveu, e não pode ser editada nem apagada depois.
- **Histórico de eventos:** seção "Eventos", com todos os eventos do cliente (os cancelados
  também), cada um com data, valor e situação.
- A ficha tem ainda a data de nascimento e um campo livre de "Observações".
- **Busca:** Painel > Clientes, campo "Buscar por nome, e-mail ou documento". O telefone não
  entra na busca.

## 2. Eventos: **confirma**

Tela: Painel > Eventos (`/events`) > clicar no evento (`/events/<id>`).

- **Situação do orçamento à entrega:** Orçamento → Contratado → Em planejamento → Em andamento
  → Pós-produção → Entregue, e também Cancelado. A situação aparece como etiqueta na lista, no
  painel inicial e no próprio evento, onde ela é trocada.
- **Checklist de preparação:** seção "Checklist", com a contagem de itens concluídos. Um item
  incluído não pode ser editado nem removido, só marcado.
- **Serviços do pacote:** seção "Serviços" (nome, quantidade, preço unitário e descrição).
- **Equipe escalada com função e cachê:** seção "Equipe" > "Adicionar membro", com os campos
  "Função no evento" e "Cachê (R$)". O cachê é opcional e pode ser valor fixo ou por hora.
  Cada pessoa aparece com a função, o cachê e a situação da presença.
- O sistema não deixa escalar a mesma pessoa em dois eventos da empresa com horários que se
  sobrepõem.

## 3. Agenda em lista e em calendário: **confirma**

Tela: Painel > Eventos (`/events`), botões "Lista" e "Calendário". O calendário é mensal e não
mostra os cancelados. Esta é a agenda da empresa. No Portal, a agenda de quem trabalha é só em
lista.

## 4. Convite por e-mail, com o papel: **confirma**

Tela: Painel > Equipe (`/team`) > botão "Convidar" (ou o atalho "Convidar membro" do painel
inicial). O convite pede o e-mail e o papel: Proprietário, Administrador, Fotógrafo, Editor ou
Freelancer. Proprietário e Administrador entram no Painel; Fotógrafo, Editor e Freelancer
entram só no Portal. A pessoa recebe o convite por e-mail.

## 5. Uma conta vê os eventos de várias empresas numa lista só: **confirma**

Tela: Portal > Agenda (`/my-events`), título "Minha agenda", com o texto "Seus eventos de todas
as empresas numa lista só, na ordem em que acontecem." Cada cartão mostra o nome da empresa,
com uma cor por empresa. Filtros: Próximos, Cancelados, Todos e Histórico (mês a mês). A pessoa
usa um login só: quando uma segunda empresa a convida pelo mesmo e-mail, ela aceita o convite
com a conta que já tem.

## 6. Confirmação, check-in e check-out pelo celular, com data e hora: **confirma**

Tela: Portal > Agenda (`/my-events`), com o botão rápido no cartão do evento ("Confirmar",
"Check-in", "Check-out"), ou dentro do evento, na seção "Sua presença", com os botões
"Confirmar presença", "Fazer check-in" e "Fazer check-out".

- A ordem é fixa: primeiro confirmar, depois check-in, depois check-out.
- Cada passo feito aparece na linha do tempo da pessoa com dia e hora.
- No check-in, o navegador pode pedir a localização. Compartilhar é opcional, e a empresa não vê
  a localização no Painel: não escrever "check-in com localização" nem que o check-in prova onde
  a pessoa estava.
- Do lado da empresa: Painel > Eventos > evento > seção "Equipe" mostra a situação de cada
  pessoa ("Aguardando confirmação", "Confirmado", "Check-in feito", "Concluído"), e o sino
  avisa cada passo (item 8). Na tela do evento a empresa vê a situação, não o horário. O
  horário aparece no aviso do sino ("há 5 min", "ontem" ou data e hora).

## 7. Despesas pelo celular; a empresa vê quem, o quê e quanto, com data e hora: **parcial**

O que existe:

- **Lançar (Portal):** dentro do evento, seção "Despesas" > "Registrar despesa"
  (`/my-events/<evento>/expenses/new`). Campos: descrição, valor e **data da despesa** (só o
  dia). Vale mesmo com o evento cancelado ou entregue. Depois de lançada, a despesa não pode
  ser editada nem apagada.
- **Ver (Painel):** Painel > Eventos > evento > seção "Despesas". A empresa vê o quê
  (descrição), quem lançou, quanto, a **data** da despesa e o total lançado no evento. **A hora
  não aparece.** A seção é só de leitura: não há aprovação nesta versão (a etiqueta é
  "Registrada").
- **Aviso (sino da empresa):** "Nova despesa lançada", com o texto "Fulano lançou R$ 45,00 em
  Casamento X". Só ali aparece o momento do lançamento ("há 5 min", "ontem" ou data e hora).
- Não há foto nem anexo de comprovante.
- Não há uma tela que junte as despesas de todos os eventos: elas ficam dentro de cada evento.

Texto que bate com o código: "A empresa vê quem lançou, o quê, quanto e a data de cada
despesa."

## 8. Avisos no sino dos dois lados: **confirma**

Tela: o sino no topo do Painel e do Portal.

- **Equipe (Portal):** "Você foi escalado num evento", "Você saiu de um evento", "Um evento
  seu foi cancelado", "Um evento seu mudou de situação" e "Seu vínculo com a empresa foi
  encerrado". Cada aviso traz o nome da empresa. Escala, saída de evento, cancelamento e fim de
  vínculo também chegam por e-mail.
- **Empresa (Painel, para Proprietário e Administrador):** "Atualização de presença" (fulano
  confirmou presença, fez check-in ou fez check-out em tal evento) e "Nova despesa lançada".
- Com o Unnar aberto na tela, o sino se atualiza sozinho a cada minuto. **Hoje não há aviso no celular
  com o Unnar fechado** (a notificação do sistema do celular): não prometa isso nos posts.

## 9. Cada empresa tem o próprio banco de dados; uma não acessa os dados de outra: **confirma**

Confirmado no código. Vale também para quem trabalha para duas empresas: no Painel, cada
empresa vê só os eventos, cachês e despesas dessa pessoa que são dela. Quem vê as duas agendas
juntas é só a própria pessoa, no Portal.

## 10. Navegador, computador e celular; tema claro e escuro: **confirma**

É um sistema web: abre no navegador do computador e do celular, e as telas se ajustam ao
tamanho (no celular, o Portal tem a barra de baixo com "Agenda" e "Perfil"). Dá para adicionar
o Unnar à tela inicial do celular, como atalho; não é aplicativo de loja (App Store ou Google
Play). O tema troca no botão do topo do Painel, do Portal e da tela de entrada, e começa no
escuro.

## 11. IA para advocacia: **parcial**

O que existe:

- É uma solução para **petição inicial trabalhista** (reclamação trabalhista). Não faz outras
  áreas do direito nem outras peças.
- Lê os documentos do caso que o escritório reúne na pasta do cliente: a ficha de atendimento,
  a procuração, a convenção coletiva e os demais documentos do contrato de trabalho.
- Redige seguindo o modelo, as teses e o procedimento **do próprio escritório**, e confere os
  dados da empresa reclamada em cadastros públicos de CNPJ.
- Para e pergunta ao advogado quando falta informação, quando aparece fato desfavorável ao
  cliente ou quando os documentos se contradizem. Não inventa fato, valor nem data: o que
  falta fica em branco, destacado.
- Entrega um arquivo **Word (.docx)** no papel timbrado do escritório, com um relatório do que
  ficou em branco, do que foi alterado e de sugestões de redação e de precedentes.
- A saída é **minuta**: a própria regra da solução diz que a revisão final é do advogado
  responsável.
- Funciona sobre o material de cada escritório: para um escritório novo, há uma etapa de
  implantação com o modelo e os papéis timbrados dele.

Texto que bate com o código: "gera a minuta da petição inicial trabalhista a partir dos
documentos do cliente e do modelo do seu escritório, entregue em Word; a revisão final é sempre
do advogado".

## Também conferi

- As capturas usadas nos posts e no Reel (painel inicial, lista de eventos e Portal no
  celular) batem com as telas de hoje: menus, etiquetas de situação e botões.
- O vídeo de 90 segundos citado na arte 5 do post 02 existe em unnar.com.br (seção "O Unnar em
  90 segundos", com telas reais e dados de exemplo).
- Reel 1: "A equipe confirma pelo celular", "Check-in com data e hora" e "E você acompanha tudo
  no painel" batem com os itens 6 e 8.

# Divergências

**Precisam de ajuste:**

1. `posts/2026-11/lote-1/09-despesas-e-avisos/legenda.md` ("cada registro com data e hora") e
   a arte `02.png` do mesmo post ("com data e hora"): na tela do evento, a empresa vê a data da
   despesa, não a hora (item 7). Sugestão: "A empresa vê quem lançou, o quê, quanto e a data de
   cada despesa."
2. `posts/2026-11/lote-1/08-ia-advocacia/legenda.md`, as artes `01.png` e `02.png` do mesmo
   post e a arte `03.png` de `posts/2026-11/lote-1/01-prazer-vorinn/` ("Petições iniciais com
   IA para escritórios de advocacia"): a solução é para petição inicial **trabalhista** e usa o
   modelo do próprio escritório (item 11). Sugestão: "petição inicial trabalhista" e "a partir
   dos documentos do cliente e do modelo do seu escritório".

**Cuidados** (o texto atual não está errado, mas pode ser lido além do que existe):

3. `posts/2026-11/lote-1/03-quem-confirmou/legenda.md` e a arte `04.png`: "No painel, você vê
   quem já chegou" está certo (situação "Check-in feito" na equipe do evento, mais o aviso do
   sino). Não escrever que a empresa vê no painel o horário de chegada: o horário fica no aviso
   do sino. Para gravação de tela, quem já chegou aparece na tela do evento (seção "Equipe"),
   não no painel inicial.
4. A arte `02.png` e a legenda de `posts/2026-11/lote-1/03-quem-confirmou/`, e a legenda de
   `posts/2026-11/lote-1/09-despesas-e-avisos/` ("foto no celular"): o Unnar não guarda foto
   nem comprovante da despesa. A frase descreve a dor e não promete foto; só não emendar com
   "anexe o comprovante".
5. `posts/2026-11/lote-1/04-do-orcamento-a-entrega/legenda.md` ("Orçamento enviado, contrato
   fechado"): o Unnar não gera nem envia orçamento ou contrato; "Orçamento" e "Contratado" são
   situações do evento. Como narrativa está bem; não escrever "envie orçamentos pelo Unnar".
6. A arte `03.png` de `posts/2026-11/lote-1/06-freelancer-agenda-unica/` ("Novas escalas
   chegam no sino") e o post 09 estão certos. As escalas também chegam por e-mail, se quiser
   usar. Não prometer notificação no celular com o app fechado (item 8).
7. `posts/2026-11/lote-1/05-automacao/legenda.md`: são exemplos do que se desenvolve sob
   medida, não recursos de um produto pronto; não há o que conferir no código.
8. A hashtag `#gestaofinanceira` do post 09 pode sugerir um módulo financeiro: a seção de
   despesas é só o registro do que a equipe informou, sem aprovação, e a própria tela diz que não
   é custo nem lucro do evento.

`PROJETO.md`: nenhuma divergência.
