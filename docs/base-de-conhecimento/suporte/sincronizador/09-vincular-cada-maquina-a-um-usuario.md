# 09 - Vincular cada máquina a um usuário

## Quando se aplica

Só quando o cliente pediu o controle de permissões por usuário (funcionalidade opcional, ver [11 - Como funciona o controle de permissões ativo](11-como-funciona-o-controle-de-permissoes-ativo.md)) — feito **antes** de ativar a exigência na empresa (ver [10 - Ativar a exigência de usuário na empresa](10-ativar-a-exigencia-de-usuario-na-empresa.md)), em **todas** as máquinas que devem passar a respeitar as permissões.

Enquanto esse passo não é feito em nenhuma máquina e a exigência não está ativada na empresa, o Sincronizador continua no comportamento padrão: qualquer pessoa que usar a máquina sincroniza tudo o que está na pasta remota configurada, sem distinção por usuário.

## Atualizar o pacote (se a máquina for de antes de 28/08/2026)

Se a máquina já tinha o Sincronizador instalado com uma versão anterior a 28/08/2026, primeiro atualizar o pacote — o script usado no próximo passo só existe a partir dessa versão. Na pasta do pacote instalado, como **Administrador**:

```
# 1. parar o serviço
.\docnuvem-sync.exe stop

# 2. substituir apenas estes dois arquivos, vindos do pacote novo:
#    app\docnuvem-sincronizador.jar
#    configurar-usuario.ps1   (arquivo novo)

# 3. subir de novo
.\docnuvem-sync.exe start
```

!!! warning "Não apagar"
    `app\application.yml` (tem a configuração da empresa) e `app\data\` (tem o estado da sincronização). Apagar `data\` faz a máquina baixar tudo de novo do zero.

## Vincular a máquina

É este passo que liga o filtro por permissão naquela máquina:

```
.\configurar-usuario.ps1
```

Pede usuário e senha do Docnuvem (a senha não aparece na tela), vincula o serviço e reinicia sozinho. Para instalação em lote: `.\configurar-usuario.ps1 -Usuario fulano -Senha 'segredo'`.

!!! warning "Importante"
    Uma máquina = um usuário do Docnuvem — não é o usuário do Windows. Em computador compartilhado, qualquer pessoa que logar no Windows verá a pasta do usuário vinculado ali. Em máquina de uso comum, vincule um usuário cujo conteúdo possa ser visto por todos que usam aquele computador.

Repetir esse passo em toda máquina da empresa que deve passar a respeitar as permissões.

!!! warning "Importante"
    Não existe hoje um comando para desvincular uma máquina. Uma vez que `configurar-usuario.ps1` rodou, a única forma de remover o vínculo é parar o serviço e apagar a pasta `app\data\` — o que também apaga o estado da sincronização, forçando uma carga completa do zero ao subir de novo.

## Se travar

Ícone roxo depois de rodar o script — ver [13 - Cores do ícone da bandeja](13-cores-do-icone-da-bandeja.md) e [15 - Solução de problemas](15-solucao-de-problemas.md).

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas não cobertos ali. -->

## Relacionados

- [Sincronizador Docnuvem](index.md)
- Próxima etapa (só depois de vincular todas as máquinas): [10 - Ativar a exigência de usuário na empresa](10-ativar-a-exigencia-de-usuario-na-empresa.md)
