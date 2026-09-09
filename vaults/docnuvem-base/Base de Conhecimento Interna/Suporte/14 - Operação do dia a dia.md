---
tipo: processo
area: suporte
etapa: "10"
status: publicado
ultima_revisao: 2026-09-09
---

# 14 - Operação do dia a dia

## Quando se aplica

Depois que o Sincronizador já está instalado e funcionando — comandos usados em manutenção, reinício após alterar configuração, ou remoção do programa.

## Comandos úteis

PowerShell **como Administrador**, na pasta do pacote:

```
.\docnuvem-sync.exe restart     # após editar o application.yml
.\docnuvem-sync.exe stop
.\docnuvem-sync.exe status
.\docnuvem-sync.exe uninstall   # remover o serviço
.\desinstalar-tray.ps1          # remover o início automático do ícone
```

## Observações

- A instalação do serviço exige PowerShell como Administrador; a instalação/remoção do ícone de bandeja é feita como usuário comum.
- A API local do status (porta 8765) fica restrita ao próprio computador (127.0.0.1), sem exposição na rede.

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas na operação do dia a dia do Sincronizador. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- [[08 - Testar a instalação]] · [[15 - Solução de problemas]]
