# Inbox: pedidos

Um arquivo por pedido, com o nome `AAAA-MM-DD-assunto.md`. A resposta vai em
`outbox/` com o mesmo nome. Quando o pedido terminar, mude o status para `feito`.

## Modelo

```markdown
---
de: claude-ai
para: escritorio
status: aberto   # aberto | em-andamento | feito | bloqueado
---

# Pedido
O que precisa ser feito, em poucas linhas.

# Pronto quando
- Critério verificável 1
- Critério verificável 2

# Contexto
Links, arquivos do repositório ou decisões que importam.
```
