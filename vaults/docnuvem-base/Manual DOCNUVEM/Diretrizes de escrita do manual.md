# Diretrizes de escrita do manual

Esta nota reúne as diretrizes definidas para a reescrita do manual do Docnuvem.

## Tratamento do Docnuvem

O Docnuvem deve sempre ser tratado no masculino, pois é apresentado como um GED.

Use formas como:

- **O Docnuvem**
- **do Docnuvem**
- **no Docnuvem**

Evite formas como:

- **A Docnuvem**
- **da Docnuvem**
- **na Docnuvem**

## Estilo dos textos

As notas devem ter linguagem clara, direta e natural, com foco no entendimento do usuário final.

Sempre que possível, os textos devem ser curtos e especializados. Cada nota deve tratar de um assunto específico, evitando reunir muitos procedimentos diferentes em um único arquivo.

O tom deve ser simples e objetivo, sem deixar o texto excessivamente técnico ou longo.

## Estrutura das notas

Cada tela principal do módulo deve ter uma nota própria, com uma apresentação curta sobre sua função.

Guias de uso, como criar, editar ou excluir registros, devem ser criados como notas separadas e vinculados como subtópicos da tela correspondente.

Exemplo:

- [[Agendamentos]]
- [[Como criar um agendamento]]
- [[Como editar um agendamento]]
- [[Como excluir um agendamento]]

## Sumário e Ordenação

A nota principal do manual ([[Docnuvem]]) e as notas principais de cada módulo devem conter um sumário com links internos do Obsidian.

### Ordem dos Módulos no Sumário Raiz ([[Docnuvem]])
A ordem dos módulos na nota [[Docnuvem]] DEVE respeitar rigorosamente a ordem do menu do sistema:

1. `[[Acessando o Sistema]]` / `[[Dashboard]]` (Página Inicial)
2. `[[Meus documentos]]`
3. `[[Busca avançada]]`
4. `[[Notificações]]`
5. `[[Meus cadastros]]`
6. `[[Meus modelos]]`
7. `[[Tipos cadastrados]]`
8. `[[Relatórios]]`
9. `[[Módulo de Tarefas]]`
10. `[[Assistente IADoc]]`
11. `[[Auditoria]]`
12. `[[Lixeira]]`

### Ordem das Notas nos Sumários dos Módulos (Curva de Aprendizado)
Dentro do sumário de cada módulo, as notas e guias DEVEM ser organizados seguindo uma **curva de aprendizado pedagógica**:
- Iniciar com o conteúdo **mais elementar e básico** (acesso, navegação, visualização).
- Progredir para o gerenciamento intermediário (criação, edição, importação).
- Finalizar com fluxos **mais complexos e avançados** que exigem maior conhecimento (formulários, assinaturas, agendamentos recorrentes e regras).

Quando houver guias diretos de uma tela (criação, edição, exclusão), manter a ordem lógica: criação, edição e exclusão.

## Links entre notas

As notas devem usar links internos do Obsidian sempre que fizer sentido relacionar telas, guias e conceitos.

Use o formato:

```markdown
[[Nome da nota]]
```

## Prints das telas

Quando uma etapa depender de uma ação visual, deve haver uma indicação clara para a equipe inserir um print.

A instrução do print deve explicar o que precisa aparecer na imagem e qual elemento deve ser destacado.

Exemplo:

```markdown
[Print sugerido: images/modulo-de-tarefas/como-editar-um-agendamento/01-listagem-acao-editar.png | Instrução: mostrar a tela de Agendamentos com a listagem aberta e destacar com uma seta vermelha a ação de editar do agendamento que será alterado.]
```

Quando necessário, orientar a equipe a usar seta vermelha para destacar botões, ações ou campos importantes.

Quando o print estiver disponível, copie-o para a pasta `images` do vault, usando o caminho indicado no placeholder. Substitua o placeholder pelo embed do Obsidian e mantenha uma legenda curta logo abaixo da imagem.

Quando o print ainda não estiver disponível, mantenha o placeholder completo, incluindo a instrução para a equipe. Sempre que houver qualquer alteração no manual, crie ou atualize também a pasta correspondente em `G:\Meu Drive\Atualização do Manual 2026\prints-manual-docnuvem\images` para que a equipe possa adicionar o arquivo no caminho esperado.

## Passo a passo

Notas de procedimento devem ser organizadas em etapas numeradas com títulos curtos.

Exemplo:

```markdown
## 1. Cadastrar novo agendamento

## 2. Informar os dados da tarefa

## 3. Definir o tipo de agendamento
```

Cada etapa deve explicar apenas o que o usuário precisa fazer naquele momento.

## Campos e opções

Campos do sistema, botões e nomes de opções devem ser destacados em negrito.

Exemplo:

- Clique em **Cadastrar novo agendamento**.
- Informe a hora no campo **Configurar hora**.
- Clique em **Salvar**.

## Organização dos arquivos

As notas relacionadas ao Módulo de Tarefas devem ficar dentro da pasta `Módulo de Tarefas`.

A nota principal `Módulo de Tarefas.md` deve permanecer na raiz do manual e funcionar como porta de entrada para o módulo.

## Diretriz geral

O objetivo do manual é orientar o usuário com clareza. Sempre que houver dúvida entre um texto mais completo e um texto mais simples, priorizar a versão mais simples, desde que a informação essencial esteja preservada.

## Sincronização entre Assistentes de IA (Codex / Antigravity)

Sempre que uma assistente de IA criar ou modificar notas, fluxos ou estruturas no manual:
- Deve registrar imediatamente o progresso no arquivo de histórico `G:\Meu Drive\Atualização do Manual 2026\historico-manual-docnuvem.txt`.
- Deve manter as diretrizes atualizadas para garantir continuidade total de trabalho entre o Codex e o Antigravity.

