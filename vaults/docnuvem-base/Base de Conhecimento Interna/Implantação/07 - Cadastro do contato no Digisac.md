---
tipo: processo
area: implantacao
etapa: "3.1"
status: publicado
ultima_revisao: 2026-09-01
---

# 07 - Cadastro do contato no Digisac

## Quando se aplica

Antes do primeiro contato com o cliente, depois de concluída a configuração inicial da instância (ver [[06 - Cadastro do primeiro usuário]]).

## Padrão de nome do contato

O nome do contato no número da implantação **deve sempre** seguir esta estrutura:

```
[IMP] (nome do cliente) - NOMEDAINSTÂNCIA(REVENDEDOR)
```

- **[IMP]** — prefixo que indica que a conexão usada é a da implantação. Todas as mensagens enviadas a esse contato usam o WhatsApp da implantação. Manter essa conexão só para contatos de implantação e SLA; assuntos de suporte devem usar outra conexão.
- **(nome do cliente)** — nome da pessoa responsável por conduzir a implantação do lado do cliente.
- **NOMEDAINSTÂNCIA(REVENDEDOR)** — nome da instância matriz do revendedor (ex.: DIGITALLIZA, CERTISEG).

![[Base de Conhecimento Interna/images/implantacao/07-cadastro-do-contato-no-digisac/01-exemplo-nome-contato-digisac.png]]

## Se travar

Reporte no grupo de Implantações.

## Relacionados

- [[Processo de Implantação]]
- Anterior: [[06 - Cadastro do primeiro usuário]] · Próxima etapa: [[08 - Script de primeiro contato]]
