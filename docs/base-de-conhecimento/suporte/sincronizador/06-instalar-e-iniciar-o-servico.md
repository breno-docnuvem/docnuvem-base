# 06 - Instalar e iniciar o serviço

## Quando se aplica

Depois de configurado o `app\application.yml` (ver [05 - Configurar o application.yml](05-configurar-o-application-yml.md)).

## Passo a passo

Abrir o PowerShell **como Administrador**, na pasta do pacote, e rodar:

```
.\docnuvem-sync.exe install
.\docnuvem-sync.exe start
```

## O que esperar

O serviço "DocNuvem Sincronizador" passa a aparecer em `services.msc` e inicia automaticamente com o Windows a partir de agora — não depende de nenhum usuário Windows estar logado.

## Se travar

Serviço não sobe ou fica preso — ver [15 - Solução de problemas](15-solucao-de-problemas.md) ("Ícone laranja / serviço não sobe").

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- Anterior: [05 - Configurar o application.yml](05-configurar-o-application-yml.md) · Próxima etapa: [07 - Instalar o ícone de bandeja](07-instalar-o-icone-de-bandeja.md)
