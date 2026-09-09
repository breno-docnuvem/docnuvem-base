# 04 - Configurar o default.properties

## Quando se aplica

Depois de baixar e alocar os arquivos do Agente na máquina do cliente (ver [03 - Baixar e alocar os arquivos](03-baixar-e-alocar-os-arquivos.md)) — igual para os dois modos de instalação.

## Onde configurar

Abrir o arquivo `default.properties` (localizado em `agente-docnuvem\bin`) com o Bloco de Notas ou outro editor de texto. O arquivo segue este modelo:

```
cliente=
diretorio=
excluiraposenviar=nao
token=
diretorioorigem=...;
diretoriodestino=/Meus documentos;
assinarpdf=nao
loginassinante=
```

## Campos

**`cliente=`** — a instância que o robô vai acessar ao fazer os envios. Preencher com o domínio/subdomínio do cliente, sem espaços. Exemplos: `cliente=exemplo`, `cliente=calcadosramarim`, `cliente=finanville-irineuimoveis`.

**`diretorio=`** — a pasta do computador que o Agente vai monitorar. TODOS os arquivos que estiverem nessa pasta serão enviados (ou pelo menos a tentativa será feita) ao Docnuvem. Arquivos que estiverem aqui mas não tiverem uma configuração de origem/destino correspondente (veja abaixo) são enviados ao Envio Inteligente. Preencher sem espaço, com o caminho do Windows usando `\\` (duas barras invertidas). Exemplo: `C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada`. Recomenda-se manter essa pasta dentro da pasta Documentos do Windows e, se necessário, criar um atalho para o cliente na Área de Trabalho — essa pasta não deve ser movida em hipótese alguma.

**`excluiraposenviar=`** — exclui o arquivo do computador do cliente depois de enviá-lo. Preencher com `sim` ou `nao`.

**`token=`** — o token da instância, emitido na plataforma.

!!! warning "Importante"
    **NÃO revogar um token que esteja em uso**, a não ser para retirar o acesso do cliente. Todas as instalações feitas com um token revogado param de funcionar imediatamente. Não esquecer de salvar o token depois de gerado.

![Geração do token da instância na plataforma.](images/04-configurar-o-default-properties/01-gerar-token.png)

**`diretorioorigem=`** e **`diretoriodestino=`** — devem ser preenchidos juntos, como um par de listas correspondentes:

- Cada campo aceita uma lista de caminhos separados por `;`.
- O 1º caminho de `diretorioorigem` envia para o 1º caminho de `diretoriodestino`, o 2º para o 2º, e assim por diante.
- Se o caminho de origem terminar com `...`, as subpastas dele também são enviadas.
- Caminhos de **origem** são caminhos do Windows e devem usar `\\` (duas barras invertidas), como em `C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada`.
- Caminhos de **destino** são caminhos dentro do Docnuvem e devem sempre começar com `/Meus documentos`.
- Não esquecer do `;` no final de cada caminho — sem ele, dá erro.
- Se ficarem em branco, os arquivos da pasta monitorada (`diretorio=`) são enviados ao Envio Inteligente (veja o terceiro exemplo abaixo).

**`assinarpdf=`** e **`loginassinante=`** — usados somente quando o cliente precisa de assinatura digital dos arquivos enviados (digitalização). Fora esse caso, deixar os dois campos em branco.

!!! warning "Pendente"
    Detalhar o que vai em `loginassinante=` (login de qual conta) e em que situação exatamente `assinarpdf=sim` deve ser usado.

## Exemplo — enviando para pastas específicas

```
cliente=exemplo
diretorio=C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada
excluiraposenviar=nao
token=TOKEN_DE_EXEMPLO
diretorioorigem=C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada\\origem A...;C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada\\origem B...;C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada\\origem C...;
diretoriodestino=/Meus documentos/destino A;/Meus documentos/destino B;/Meus documentos/destino C;
assinarpdf=nao
loginassinante=
```

## Exemplo — enviando tudo para a raiz de "Meus documentos"

Se o cliente quiser que todo o conteúdo da pasta monitorada vá direto para a raiz de "Meus documentos" (fora de qualquer subpasta), o arquivo de configuração pode ficar assim:

```
cliente=exemplo
diretorio=C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada
excluiraposenviar=nao
token=TOKEN_DE_EXEMPLO
diretorioorigem=C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada...;
diretoriodestino=/Meus documentos;
assinarpdf=nao
loginassinante=
```

## Exemplo — enviando tudo para o Envio Inteligente

Se o cliente quiser que todo o conteúdo da pasta monitorada vá para o Envio Inteligente, o arquivo pode ficar assim (campos `diretorioorigem=` e `diretoriodestino=` em branco):

```
cliente=exemplo
diretorio=C:\\Users\\cliente\\OneDrive\\Documentos\\Pasta sincronizada
excluiraposenviar=nao
token=TOKEN_DE_EXEMPLO
diretorioorigem=
diretoriodestino=
assinarpdf=nao
loginassinante=
```

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas de configuração do default.properties. -->

## Relacionados

- [Agente Docnuvem (robô)](index.md)
- Anterior: [03 - Baixar e alocar os arquivos](03-baixar-e-alocar-os-arquivos.md) · Próximas etapas: [05 - Rodar como programa convencional](05-rodar-como-programa-convencional.md) ou [06 - Instalar como serviço do Windows](06-instalar-como-servico-do-windows.md)
- Veja também no Manual do Sistema: [Arquivos — Como configurar regras de Envio Inteligente](../../../manual/10-arquivos.md#como-configurar-regras-de-envio-inteligente)
