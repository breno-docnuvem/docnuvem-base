---
tipo: processo
area: suporte
etapa: "7"
status: publicado
ultima_revisao: 2026-09-09
---

# 11 - Como funciona o controle de permissões ativo

## Quando se aplica

Funcionalidade opcional, disponível desde 28/08/2026, estabilizada em 04/09/2026. Estas regras só valem depois que a empresa tiver marcado "Exigir usuário no sincronizador" (ver [[10 - Ativar a exigência de usuário na empresa]]) **e** a máquina estiver vinculada a um usuário (ver [[09 - Vincular cada máquina a um usuário]]). Fora isso, vale sempre o comportamento padrão (sincroniza tudo, para qualquer usuário da máquina).

## Regras de comportamento

- O espelho na máquina passa a vir **filtrado pelas permissões daquele usuário** — pastas sem permissão simplesmente não aparecem no computador.
- **A permissão de leitura na própria pasta raiz sincronizada é obrigatória.** Sem ela, o Sincronizador é recusado logo no arranque e não sincroniza nada, mesmo que o usuário tenha permissão em pastas de dentro.
- **Grupo sem permissão de pasta zera o acesso do usuário**, mesmo que ele tenha permissão individual — no Docnuvem, a permissão do grupo *substitui* a individual em vez de somar. Um grupo vazio derruba o acesso inteiro do usuário (a sincronização aborta por segurança, sem apagar nada; tirar o usuário do grupo volta ao normal sozinho).
- **Revogar** a permissão de uma pasta faz ela sumir do computador — mas os documentos continuam intactos no Docnuvem Web, fora da lixeira. Perder acesso nunca apaga o documento para os outros usuários.
- Um arquivo criado localmente e ainda não enviado quando a permissão é revogada não se perde: ele aparece em `<pasta sincronizada>-removidos`, com o conteúdo intacto.
- **Usuário administrador** vinculado ignora as permissões — o espelho vem completo, como no comportamento padrão.
- O Sincronizador reconfere as permissões **de hora em hora**. Para aplicar uma mudança na hora, usar **"Atualizar pastas permitidas"** no menu do ícone da bandeja.

## Na prática — bloqueio de máquina

Bloqueio de máquina (ex.: notebook extraviado) se faz bloqueando o usuário vinculado àquela máquina no Docnuvem — não existe hoje uma tela separada para bloquear a máquina em si. Com o usuário bloqueado, o ícone fica roxo em até 30 segundos e a sincronização para sem perder nada; desbloqueando o usuário e clicando "Sincronizar agora" ela retoma do ponto onde parou.

## Se travar

Ícone roxo — ver [[13 - Cores do ícone da bandeja]] e [[15 - Solução de problemas]].

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- [[10 - Ativar a exigência de usuário na empresa]] · [[12 - Migrando máquinas aos poucos]]
