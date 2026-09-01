# Diretrizes de geração de manuais

Esta nota define como os manuais do Docnuvem devem ser organizados no Obsidian e como devem ser gerados em PDF usando LaTeX.

## Estrutura no Obsidian

O manual deve ser organizado a partir da nota principal [[Docnuvem]].

A nota [[Docnuvem]] DEVE conter um sumário com os módulos da plataforma, **respeitando estritamente a ordem do menu do sistema**:
1. [[Acessando o Sistema]] / [[Dashboard]] (Página Inicial)
2. [[Meus documentos]]
3. [[Busca avançada]]
4. [[Notificações]]
5. [[Meus cadastros]]
6. [[Meus modelos]]
7. [[Tipos cadastrados]]
8. [[Relatórios]]
9. [[Módulo de Tarefas]]
10. [[Assistente IADoc]]
11. [[Auditoria]]
12. [[Lixeira]]

Cada módulo deve ter uma nota própria na raiz do manual e uma pasta com o mesmo nome para abrigar suas notas filhas.

## Notas de módulo e Curva de Aprendizado

A nota principal de cada módulo deve conter:
- Título do módulo.
- Texto curto de apresentação.
- Sumário com links internos do Obsidian para as telas e guias daquele módulo.

O sumário do módulo define a ordem em que as notas da pasta do módulo devem ser usadas na geração do PDF.

**Regra de Ordenação dos Sumários de Módulo**:
As notas de cada módulo devem ser organizadas seguindo uma **curva de aprendizado pedagógica** (do mais elementar/básico ao mais complexo e avançado):
1. Telas de acesso, navegação e visualização básica.
2. Procedimentos de gerenciamento, criação e importação.
3. Fluxos avançados (formulários, requisições, assinaturas, agendamentos recorrentes e configurações).

## Notas individuais

As notas dentro da pasta do módulo devem ser curtas e especializadas.

Cada nota deve tratar de uma tela, funcionalidade ou procedimento específico.

Exemplo:

- Uma nota para a tela de Agendamentos.
- Uma nota para criar um agendamento.
- Uma nota para editar um agendamento.
- Uma nota para excluir um agendamento.

## Geração do manual completo

Para gerar o manual completo da plataforma, usar a nota [[Docnuvem]] como ponto de partida.

Quando o pedido do usuário for algo como **"Gere um manual a partir da nota X"**, a nota informada deve ser usada como ponto de partida da geração.

Exemplos de comando:

- **Gere um manual a partir da nota Docnuvem**
- **Gere um manual a partir da nota Módulo de Tarefas**
- **Gere um manual a partir da nota Projetos**

Nesses casos, o conteúdo gerado deve respeitar o sumário da nota indicada. Se a nota indicada possuir links para outras notas, esses links devem orientar a ordem de leitura e inclusão do conteúdo no PDF.

O processo deve ser:

1. Identificar a nota indicada pelo usuário como ponto de partida.
2. Ler o sumário da nota indicada.
3. Processar os links na ordem em que aparecem nesse sumário.
4. Para cada módulo ou nota vinculada, ler o conteúdo correspondente.
5. Incorporar as notas relacionadas na ordem definida pelo sumário.
6. Converter o conteúdo consolidado para LaTeX.
7. Gerar o PDF usando o arquivo de configuração `C:\Users\breno\OneDrive\Documentos\GitHub\doc_manuals\Manual\settings.cls`.

## Geração de mini manual

Para gerar um mini manual de apenas uma parte da plataforma, usar a mesma lógica, mas restringir a leitura ao módulo, tela ou subtópico solicitado.

Mesmo em mini manuais, a estrutura e a ordem devem respeitar os links existentes em [[Docnuvem]] e no sumário do módulo correspondente, quando aplicável.

## Links no PDF

Todos os links internos do Obsidian devem ser convertidos em links internos no PDF.

Links no formato:

```markdown
[[Nome da nota]]
```

devem apontar para a seção correspondente no PDF.

Links para subtópicos no formato:

```markdown
[[Nome da nota#Título da seção]]
```

devem apontar para a âncora correspondente daquele item no PDF.

Quando uma nota do Obsidian for incorporada ao PDF, o título da nota deve gerar uma âncora de destino no LaTeX para permitir a navegação interna.

## LaTeX

Os PDFs devem ser gerados com LaTeX usando o estilo visual definido em:

```text
C:\Users\breno\OneDrive\Documentos\GitHub\doc_manuals\Manual\settings.cls
```

O arquivo `.tex` gerado deve preservar:

- Sumário do PDF.
- Hierarquia de seções.
- Títulos claros.
- Destaque de botões, campos e opções.
- Placeholders de prints quando os prints ainda não existirem.

### Paginação de imagens

Antes de finalizar um PDF, revisar a distribuição das imagens nas páginas. Usar uma largura única para os prints de cada manual e preservar suas proporções. Reservar espaço antes de títulos e instruções que possuem print, movendo o conjunto para a página seguinte quando necessário. Evitar grandes espaços em branco, instruções separadas da imagem correspondente e páginas com apenas uma imagem.

## Prints

Quando uma nota tiver instruções de print, essa instrução deve ser mantida como placeholder no PDF até que o print real seja adicionado.

Ao substituir por uma imagem real, os prints devem ser salvos no repositório `doc_manuals`, seguindo a estrutura de imagens do manual em LaTeX.

Os placeholders de prints devem indicar o caminho sugerido do arquivo de imagem. Isso permite que, no futuro, a geração do PDF substitua automaticamente o placeholder pela imagem real quando o arquivo existir.

Formato recomendado para placeholders:

```markdown
[Print sugerido: images/<modulo>/<nota>/<numero-descricao>.png | Instrução: descrever o que deve aparecer no print.]
```

Estrutura de pastas recomendada:

```text
images/<modulo>/<nota>/<numero-descricao>.png
```

Exemplo:

```text
images/modulo-de-tarefas/como-criar-um-agendamento/01-listagem-cadastrar-novo-agendamento.png
```

Regras de nomenclatura:

- Usar letras minúsculas.
- Remover acentos.
- Trocar espaços por hífen.
- Usar numeração com dois dígitos, como `01`, `02`, `03`.
- Usar nomes curtos e descritivos.
- Usar a extensão `.png`.

Também foi criado um documento para orientar a equipe de prints na Área de Trabalho:

```text
C:\Users\breno\OneDrive\Desktop\Instruções para prints - Manual Docnuvem.md
```

## Diretriz geral

A nota [[Docnuvem]] é a fonte principal de ordem e organização do manual.

As notas dos módulos e suas pastas são a fonte principal de conteúdo.

Ao gerar PDFs, não criar uma nota consolidada intermediária no Obsidian. A consolidação deve acontecer diretamente no arquivo `.tex` gerado.
