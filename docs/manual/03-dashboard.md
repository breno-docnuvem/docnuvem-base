# Dashboard

O Dashboard é a página inicial do Docnuvem: reúne quadros e gráficos com os principais indicadores da instância.

## Acessando o Dashboard

Ao fazer login no Docnuvem, o Dashboard é apresentado automaticamente como página inicial.

Também é possível acessá-lo a qualquer momento pelo menu lateral, clicando em **Página Inicial**.

!!! tip "Print sugerido"
    `images/dashboard/acessando-o-dashboard/01-menu-pagina-inicial.png` — mostrar o menu lateral do Docnuvem com a opção **Página Inicial** destacada por uma seta vermelha.

**Resultado esperado:** o sistema exibe o Dashboard com os quadros e gráficos disponíveis para o perfil do usuário.

!!! tip "Print sugerido"
    `images/dashboard/acessando-o-dashboard/02-tela-dashboard.png` — mostrar a tela principal do Dashboard aberta, com os gráficos e indicadores visíveis.

## Indicadores do Dashboard

O Dashboard organiza as informações em seções visuais. Cada seção apresenta dados consolidados da instância e pode variar conforme os módulos habilitados e as permissões do usuário.

### Seu gerenciamento

Gráficos de rosca com os principais indicadores operacionais: **Assinaturas** (realizadas, pendentes, canceladas e vencidas), **Checklists** (itens em aberto e concluídos), **Vencimentos** (documentos vencidos ou em aberto) e **Solicitações** (em aberto e concluídas).

!!! tip "Print sugerido"
    `images/dashboard/indicadores-do-dashboard/01-seu-gerenciamento.png` — mostrar a seção **Seu gerenciamento** com os gráficos de Assinaturas, Checklists, Vencimentos e Solicitações.

### Assinatura por tipo

Mostra a distribuição das assinaturas realizadas por categoria: os tipos antigos — **Digital**, **Nuvem (BirdID)** e **Eletrônica** — ou os tipos EasySign — **Simples**, **Qualificada** e **Avançada**.

!!! tip "Print sugerido"
    `images/dashboard/indicadores-do-dashboard/02-assinatura-por-tipo.png` — mostrar a seção **Assinatura por tipo** com o gráfico de colunas e os filtros de visualização destacados.

### Atividade

Gráfico de linha com a evolução dos registros ao longo do tempo, podendo exibir **Documentos enviados**, **Assinaturas realizadas**, **Checklists vinculados**, **Vencimentos criados** e **Solicitações de envio**.

!!! tip "Print sugerido"
    `images/dashboard/indicadores-do-dashboard/03-atividade.png` — mostrar a seção **Atividade** com o gráfico de linha e a legenda dos tipos de atividade.

!!! info "Importante"
    Os números apresentados no Dashboard dependem dos dados existentes na instância, dos módulos contratados e das permissões do usuário logado.

## Filtros do Dashboard

O Dashboard possui filtros de período e de visualização para ajustar os dados exibidos nos gráficos.

### Filtro de período em Seu gerenciamento

Opções disponíveis: **Data atual**, **Últimos 3 dias**, **Últimos 7 dias**, **Últimos 15 dias**, **Últimos 30 dias** e **Todo período**.

!!! tip "Print sugerido"
    `images/dashboard/filtros-do-dashboard/01-filtro-seu-gerenciamento.png` — mostrar o seletor de período da seção **Seu gerenciamento** aberto, com as opções disponíveis visíveis.

### Filtros de Assinatura por tipo

O usuário pode alterar a forma de visualização — **Antigo (Digital, BirdId e Eletrônica)** ou **EasySign (Simples, Qualificada e Avançada)** — e o período do gráfico: **Último mês**, **Últimos 2 meses**, **Últimos 3 meses**, **Últimos 4 meses**, **Últimos 5 meses**, **Últimos 6 meses** ou **Todo período**.

!!! tip "Print sugerido"
    `images/dashboard/filtros-do-dashboard/02-filtros-assinatura-por-tipo.png` — mostrar os filtros da seção **Assinatura por tipo**, destacando o seletor de tipo de assinatura e o seletor de período.

### Filtros de Atividade

O usuário pode escolher o tipo de atividade — **Documentos enviados**, **Assinaturas realizadas**, **Checklists vinculados**, **Vencimentos criados**, **Solicitações de envio** ou **Todos** — e o período: **Últimos 3 meses**, **Últimos 6 meses**, **Últimos 9 meses** ou **Últimos 12 meses**.

!!! tip "Print sugerido"
    `images/dashboard/filtros-do-dashboard/03-filtros-atividade.png` — mostrar os filtros da seção **Atividade**, destacando o seletor de tipo de atividade e o seletor de período.

**Resultado esperado:** após alterar um filtro, o Docnuvem atualiza o gráfico correspondente com os dados do período ou tipo selecionado.

## Análise detalhada (Drill-Down)

O Dashboard permite acessar informações detalhadas a partir dos próprios quadros e gráficos. Esse recurso é chamado de **Drill-Down**.

### 1. Clicar em um quadro ou gráfico

Clique em uma área do quadro, gráfico ou legenda desejada — por exemplo, os status de **Assinaturas**, **Checklists**, **Vencimentos** e **Solicitações**, as colunas de **Assinatura por tipo** ou os pontos do gráfico de **Atividade**.

!!! tip "Print sugerido"
    `images/dashboard/analise-detalhada-drill-down/01-indicador-clicavel.png` — mostrar um indicador do Dashboard com uma seta vermelha apontando para uma área clicável do gráfico ou legenda.

### 2. Abrir a listagem detalhada

Ao clicar no indicador, o Docnuvem abre uma nova aba com a listagem detalhada relacionada ao item selecionado, já filtrada conforme o quadro, tipo de informação e período selecionados no Dashboard.

!!! tip "Print sugerido"
    `images/dashboard/analise-detalhada-drill-down/02-listagem-detalhada.png` — mostrar a nova aba aberta com a listagem detalhada do indicador selecionado e os resultados filtrados.

### 3. Refinar a busca com filtros

Na listagem detalhada, clique em **Filtrar** para exibir os campos de busca disponíveis. Preencha as informações desejadas e clique novamente em **Filtrar** para aplicar a busca.

!!! tip "Print sugerido"
    `images/dashboard/analise-detalhada-drill-down/03-filtro-listagem.png` — mostrar a listagem detalhada com o botão **Filtrar** e os campos de filtro visíveis.

**Resultado esperado:** o sistema exibe apenas os registros que atendem ao indicador selecionado no Dashboard e aos filtros aplicados na listagem. Com esse recurso, o usuário transforma os gráficos em consultas práticas para análise e tomada de decisão.

## Veja também

- [Central de Ajuda: Visão geral do sistema](../central-de-ajuda/visao-geral.md) — modelo mental dos módulos do Docnuvem.
