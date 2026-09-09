---
tipo: processo
area: suporte
etapa: "9"
status: publicado
ultima_revisao: 2026-09-09
---

# 13 - Cores do ícone da bandeja

## Quando se aplica

Referência rápida para qualquer atendimento onde o cliente descreve a cor do ícone do Sincronizador na bandeja do Windows.

## Tabela de cores

| Cor | Significado |
|---|---|
| Verde | Sincronizado |
| Azul | Sincronizando (há operações pendentes) |
| Cinza | Pausado pelo usuário |
| Vermelho | Há operações com erro (ver logs) |
| **Roxo** *(novo, do controle de permissões)* | O servidor recusou a credencial desta máquina — usuário vinculado bloqueado, ou a empresa exige usuário e esta máquina ainda não foi vinculada (`configurar-usuario.ps1`) |
| Laranja | Serviço parado ou inacessível |

## Na prática

Roxo é sempre ligado ao controle de permissões por usuário — antes de investigar como um bug, conferir [[11 - Como funciona o controle de permissões ativo]] e [[12 - Migrando máquinas aos poucos]].

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para cores/estados não cobertos aqui. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- [[15 - Solução de problemas]]
