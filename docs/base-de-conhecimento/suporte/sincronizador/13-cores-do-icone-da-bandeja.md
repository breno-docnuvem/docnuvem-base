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

Roxo é sempre ligado ao controle de permissões por usuário — antes de investigar como um bug, conferir [11 - Como funciona o controle de permissões ativo](11-como-funciona-o-controle-de-permissoes-ativo.md) e [12 - Migrando máquinas aos poucos](12-migrando-maquinas-aos-poucos.md).

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para cores/estados não cobertos aqui. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- [15 - Solução de problemas](15-solucao-de-problemas.md)
