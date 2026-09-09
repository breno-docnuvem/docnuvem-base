---
tipo: processo
area: suporte
etapa: "4.4"
status: publicado
ultima_revisao: 2026-09-09
---

# 07 - Instalar o ícone de bandeja

## Quando se aplica

Depois de instalado e iniciado o serviço (ver [[06 - Instalar e iniciar o serviço]]). Passo **opcional**, mas recomendado — sem ele o serviço sincroniza normalmente, só não há um ícone visível para o usuário acompanhar o status.

## Passo a passo

Abrir o PowerShell **normal, sem ser Administrador**, na pasta do pacote, e rodar:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\instalar-tray.ps1
```

## O que esperar

O ícone aparece ao lado do relógio e passa a iniciar a cada login do Windows. O menu (botão direito) oferece: abrir a pasta sincronizada, pausar/retomar, sincronizar agora e sair — "Sair" fecha só o ícone, o serviço continua sincronizando em segundo plano.

> ⚠️ O ícone depende do serviço estar rodando. Serviço parado = ícone laranja (ver [[13 - Cores do ícone da bandeja]]).

## Se travar

Erro de política de execução ao rodar o `.ps1` — ver [[15 - Solução de problemas]].

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- Anterior: [[06 - Instalar e iniciar o serviço]] · Próxima etapa: [[08 - Testar a instalação]]
