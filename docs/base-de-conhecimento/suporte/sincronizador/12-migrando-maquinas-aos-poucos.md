# 12 - Migrando máquinas aos poucos

## Quando se aplica

Quando uma empresa está migrando gradualmente para o controle de permissões por usuário, com algumas máquinas já vinculadas e outras ainda não — ou quando uma máquina aparece recusada e é preciso diferenciar um problema real de um comportamento esperado.

## Sem "Exigir usuário no sincronizador" marcada

Com a opção **desmarcada** na empresa, uma máquina que nunca rodou `configurar-usuario.ps1` continua funcionando exatamente como antes, espelhando a pasta inteira — é isso que permite migrar as máquinas de uma empresa aos poucos, sem prazo e sem parar ninguém.

## Se uma máquina não vinculada aparecer recusada

Se uma máquina assim aparecer recusada (ícone roxo, log dizendo que "a máquina exige login de usuário") mesmo sem nunca ter sido vinculada, é sinal de que a empresa já está com "Exigir usuário no sincronizador" **marcada** — nesse caso a recusa é o comportamento esperado (ver [10 - Ativar a exigência de usuário na empresa](10-ativar-a-exigencia-de-usuario-na-empresa.md) e [11 - Como funciona o controle de permissões ativo](11-como-funciona-o-controle-de-permissoes-ativo.md)), não um problema na máquina.

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para casos de migração que não se encaixem no que está descrito acima. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- [09 - Vincular cada máquina a um usuário](09-vincular-cada-maquina-a-um-usuario.md) · [10 - Ativar a exigência de usuário na empresa](10-ativar-a-exigencia-de-usuario-na-empresa.md) · [11 - Como funciona o controle de permissões ativo](11-como-funciona-o-controle-de-permissoes-ativo.md)
