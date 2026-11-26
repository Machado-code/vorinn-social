---
de: claude-ai
para: escritorio
status: aberto
---

# Pedido
Conferir no código do Unnar (e da solução jurídica da Vorinn) se cada afirmação do
lote 1 é verdadeira hoje. Os textos saíram do site unnar.com.br e vorinn.com.br; o
claude.ai não tem como olhar o código.

Afirmações:
1. Clientes: ficha com contatos, documento, endereço, origem do contato, anotações
   datadas e histórico de eventos; busca por nome, e-mail ou documento.
2. Eventos: status do orçamento à entrega, checklist de preparação, serviços do pacote e
   equipe escalada com função e cachê.
3. Agenda de eventos em lista e em calendário.
4. Equipe: convite por e-mail, com o papel de cada um.
5. Portal: uma conta vê os eventos de várias empresas numa lista só, cada um com o nome
   da empresa.
6. Portal: confirmação de presença, check-in e check-out pelo celular, com data e hora.
7. Despesas lançadas pelo celular; a empresa vê quem lançou, o quê e quanto, com data e
   hora.
8. Avisos no sino dos dois lados: escalas para a equipe; presença e despesas para a
   empresa.
9. Cada empresa tem o próprio banco de dados; uma empresa não acessa os dados de outra.
10. Funciona no navegador, no computador e no celular; tema claro e escuro.
11. Vorinn, IA para advocacia: gera a petição inicial a partir dos documentos do cliente
    e entrega em Word; a revisão final é do advogado.

# Pronto quando
- A resposta em `outbox/` traz cada item como **confirma**, **parcial** ou **não
  existe**, com o arquivo ou a tela que comprova.
- Nos itens parciais, diz exatamente o que existe.
- Nenhuma mudança em `posts/` ou `reels/`: o claude.ai corrige o texto pela resposta.

# Contexto
- Posts em `posts/2026-11/lote-1/` (legenda em `legenda.md`, artes em PNG) e
  `reels/2026-11/`.
- Prazo: antes do lançamento do @vorinn (assim que o Matheus criar a conta).
