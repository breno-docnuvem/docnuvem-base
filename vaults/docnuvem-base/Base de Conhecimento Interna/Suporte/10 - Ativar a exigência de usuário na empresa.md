---
tipo: processo
area: suporte
etapa: "6.2"
status: publicado
ultima_revisao: 2026-09-09
---

# 10 - Ativar a exigência de usuário na empresa

## Quando se aplica

**Só depois** que todas as máquinas da empresa que devem respeitar as permissões já estiverem vinculadas a um usuário (ver [[09 - Vincular cada máquina a um usuário]]). Ativar antes disso derruba a sincronização das máquinas ainda não vinculadas.

## O que fazer

Nas configurações da empresa, dentro do módulo Sincronizador, marcar **"Exigir usuário no sincronizador (sincroniza apenas o que cada usuário pode ver)"**.

![[Base de Conhecimento Interna/images/suporte/sincronizador/10-ativar-a-exigencia-de-usuario-na-empresa/01-tela-configuracoes-sincronizador.png]]

> ⚠️ **Máquina não vinculada para de sincronizar assim que essa opção é marcada.** O próprio Docnuvem avisa, ao lado do checkbox: *"Só ative depois que todas as máquinas já tiverem sido vinculadas a um usuário (`configurar-usuario.ps1`). As que ainda usarem o token da empresa param de sincronizar."* Isso é intencional: com a opção marcada, qualquer máquina que tentar sincronizar sem estar vinculada a um usuário é recusada de propósito (ícone roxo, log indicando que a máquina exige login de usuário) — não é um bug, é a opção fazendo o que promete.

A partir daqui, as regras de [[11 - Como funciona o controle de permissões ativo]] passam a valer para as máquinas vinculadas dessa empresa.

## Se travar

Máquina recusada mesmo sem nunca ter sido vinculada — ver [[12 - Migrando máquinas aos poucos]] antes de tratar como bug.

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- Anterior: [[09 - Vincular cada máquina a um usuário]] · Depois de ativado: [[11 - Como funciona o controle de permissões ativo]]
