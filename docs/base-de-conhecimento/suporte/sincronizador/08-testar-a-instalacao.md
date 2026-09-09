# 08 - Testar a instalação

## Quando se aplica

Depois de instalados o serviço e (se aplicável) o ícone de bandeja — ver [06 - Instalar e iniciar o serviço](06-instalar-e-iniciar-o-servico.md) e [07 - Instalar o ícone de bandeja](07-instalar-o-icone-de-bandeja.md).

## Passo a passo

- **Sincronização inicial:** ao iniciar, a pasta local (`pasta-local-raiz`) deve ser preenchida com o conteúdo da pasta remota configurada. O ícone fica verde.
- **Remoto → local:** enviar um documento pela web na pasta sincronizada — em cerca de 30 segundos deve aparecer na pasta local.
- **Local → remoto:** colocar um arquivo novo na pasta local — em alguns segundos deve aparecer na web.
- **Renomear/mover:** renomear um arquivo localmente — deve refletir na web preservando o histórico, sem duplicar o documento.
- **Assinatura:** assinar um documento na web — a versão assinada deve descer para a pasta local no próximo ciclo.

## Consultando o estado e os logs

```
.\docnuvem-sync.exe status
```

Os logs ficam em `logs\docnuvem-sync.out.log` (linhas `[watcher]`, `[upload]` e `[status]`). O estado atual também pode ser consultado em `http://127.0.0.1:8765/status` — mais confiável que ler o histórico do log.

## Se travar

Ver [15 - Solução de problemas](15-solucao-de-problemas.md) para os problemas mais comuns encontrados nesse teste.

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- Anterior: [07 - Instalar o ícone de bandeja](07-instalar-o-icone-de-bandeja.md)
- Próximo (opcional): [09 - Vincular cada máquina a um usuário](09-vincular-cada-maquina-a-um-usuario.md), se o cliente quiser o controle de permissões por usuário
