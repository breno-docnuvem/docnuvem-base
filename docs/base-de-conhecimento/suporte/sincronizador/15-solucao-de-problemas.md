# 15 - Solução de problemas

## Quando se aplica

Referência para os problemas mais comuns encontrados na instalação e operação do Sincronizador.

## "não pode ser carregado porque a execução de scripts foi desabilitada"

A política de execução do Windows está bloqueando os `.ps1`. Rodar antes, na mesma janela: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. Vale só para a janela atual. Alternativa em um comando só: `powershell -ExecutionPolicy Bypass -File .\instalar-tray.ps1`.

## Ícone laranja / serviço não sobe

Confirmar que o serviço está rodando (`.\docnuvem-sync.exe status`), conferir os dados em `app\application.yml` (endereço da API, token e instância) e o acesso de rede da máquina ao servidor. Se a porta 8765 já estiver em uso, alterar `server.port` no `application.yml` e reinstalar o tray com `.\instalar-tray.ps1 -Porta NOVA_PORTA`.

## Ícone roxo

Ver [10 - Ativar a exigência de usuário na empresa](10-ativar-a-exigencia-de-usuario-na-empresa.md) e [12 - Migrando máquinas aos poucos](12-migrando-maquinas-aos-poucos.md): normalmente é o usuário vinculado bloqueado, ou a máquina não vinculada numa empresa que já exige usuário.

## Mudanças feitas na web não aparecem no cliente

Confirmar que o tenant tem `empresa.sincronizador = true` e que o schema de sincronização foi aplicado no banco do tenant (isso é responsabilidade do desenvolvimento, não do suporte).

## Erro de tamanho de arquivo no upload

Indica que a API não está com o build atualizado (limite de 1 GB). Escalar para o desenvolvimento atualizar o servidor.

## Erro ao criar pasta sem permissão *(bug conhecido, identificado nos testes do controle de permissões)*

Numa máquina com o controle de permissões ativo, ao tentar criar uma pasta em um diretório sem permissão, ocorre falha e o ícone fica vermelho. Excluir a pasta criada indevidamente **não corrige** o problema — foi preciso desinstalar e reinstalar o programa. Acontece principalmente quando a raiz sincronizada é "Meus documentos", já que usuários não administradores normalmente não têm permissão para criar pastas na raiz do sistema.

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos aqui. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- [13 - Cores do ícone da bandeja](13-cores-do-icone-da-bandeja.md) · [11 - Como funciona o controle de permissões ativo](11-como-funciona-o-controle-de-permissoes-ativo.md)
