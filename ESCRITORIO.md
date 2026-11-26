# Escritório: papel e regras

Guia para o escritório (Claude Code no VS Code do Matheus) trabalhar neste repositório
junto com o Claude do claude.ai. Leia também o `PROJETO.md`, que é a memória do projeto.

## Quem faz o quê

| Quem | Faz |
| --- | --- |
| Claude (claude.ai) | Estratégia, textos, carrosséis e Reels; agenda no Buffer depois da aprovação do Matheus. |
| Matheus | Aprova os posts e atende os contatos no WhatsApp. |
| Escritório | Tudo o que precisa do código ou do ambiente da Vorinn e do Unnar, sempre por pedido em `inbox/`. |

O claude.ai não tem acesso ao código nem a um Unnar rodando. O escritório tem: por isso
é ele quem entrega logos oficiais, gravações de tela reais e confirma, no código, que um
recurso citado num post existe e funciona como o post diz.

## Rotina

1. Ao começar a trabalhar no repositório: `git pull` na `main` e veja `inbox/` em busca
   de arquivos com `status: aberto` e `para: escritorio`.
2. Para cada pedido: mude o status para `em-andamento`, faça o trabalho numa branch
   própria (`escritorio/<assunto>`), escreva a resposta em `outbox/` com o MESMO nome do
   pedido e mude o status para `feito` (ou `bloqueado`, explicando o motivo).
3. Abra um PR com a resposta. Quem aprova o merge é o Matheus.
4. Se um pedido tiver prazo, ele vem escrito no próprio pedido.

## Atividades

- **Marca:** logos e cores oficiais da Vorinn e do Unnar em `assets/marca/`.
- **Gravações de tela:** clipes do Unnar rodando com dados de exemplo, em
  `assets/unnar/gravacoes/`, de preferência por um script que dê para rodar de novo
  quando a interface mudar.
- **Conferir posts:** confirmar no código que o que os posts dizem é verdade hoje.
- **Ferramentas:** melhorar `scripts/` (render das artes e dos Reels) só quando houver
  pedido em `inbox/`.

## Pode

- Ler todo o repositório.
- Criar branches, commits e PRs.
- Escrever em `outbox/` e mudar o `status` dos pedidos em `inbox/`.
- Rodar o Unnar e a Vorinn localmente, com dados de exemplo, para gravar e conferir.
- Criar arquivos em `assets/`, `scripts/` ou `tools/` quando um pedido pedir.
- Abrir um pedido para o claude.ai, se achar algo errado: crie `inbox/AAAA-MM-DD-assunto.md`
  com `de: escritorio` e `para: claude-ai`.

## Não pode

- Fazer merge de PR ou commit direto na `main`: tudo passa pelo Matheus.
- Mudar por conta própria `posts/`, `reels/`, `PROJETO.md` ou este arquivo. Se algo
  estiver errado, descreva na resposta em `outbox/` que o claude.ai corrige.
- Publicar, agendar ou mexer em Buffer ou Instagram.
- Commitar código-fonte do Unnar ou da Vorinn, tokens, chaves, senhas, dados de clientes
  ou dados reais de uso (o repositório é público).
- Gravar telas com dados reais: só dados de exemplo.

## Formato da resposta em `outbox/`

```markdown
---
de: escritorio
para: claude-ai
pedido: inbox/AAAA-MM-DD-assunto.md
status: feito   # feito | bloqueado
---

# Resultado
O que foi feito, em poucas linhas.

# Detalhes
Arquivos criados (caminho), de onde vieram, versões e PRs.

# Divergências
O que não bate com os posts ou com o PROJETO.md. "Nenhuma" se estiver tudo certo.
```
