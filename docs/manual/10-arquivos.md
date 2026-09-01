# Arquivos

O módulo **Arquivos** reúne telas de acompanhamento e automação sobre documentos: **Contratos**, **Certificados**, **IA Documental** e **Assinatura em massa**.

## Contratos

A tela **Contratos** permite acompanhar documentos contratuais com data de vencimento. Use-a para identificar contratos vencidos ou próximos do vencimento, visualizar documentos e agir antes que prazos importantes expirem.

### Como filtrar e visualizar Contratos

1. No menu principal, acesse **Arquivos** e clique em **Contratos**.
2. Use os filtros para visualizar contratos vencidos ou próximos do vencimento — eles ajudam a acompanhar prazos e priorizar renovações, renegociações ou outras ações necessárias.
3. Para acessar o documento, clique no botão disponível na coluna **Ações** do contrato desejado.
4. Acompanhe as notificações de vencimento: quando houver contratos próximos do vencimento, o sistema exibe um ícone de sino ao lado do usuário, indicando contratos que vencem nos próximos 7 dias.

!!! tip "Prints sugeridos"
    `images/arquivos/como-filtrar-e-visualizar-contratos/01-menu-contratos.png` a `04-sino-vencimento.png` — menu **Arquivos** → **Contratos**, filtros de vencimento, ação de visualizar documento e ícone de sino de vencimento.

**Resultado esperado:** o usuário consegue identificar contratos vencidos, acompanhar contratos próximos do vencimento e abrir o documento para consulta.

### Como configurar data de vencimento para Contratos

Para que um contrato apareça na tela Contratos com controle de validade, o modelo do documento precisa ter um item de data de vencimento.

1. No menu principal, acesse **Meus modelos** → **Modelo de documento** e crie ou edite o modelo utilizado para gerar contratos.
2. Na configuração de itens do modelo, adicione um item com o tipo **Data de vencimento** (veja [Como configurar itens no Modelo de documento](08-meus-modelos.md#como-configurar-itens-no-modelo-de-documento)).
3. Clique em **Salvar**.

**Resultado esperado:** os contratos criados a partir desse modelo passam a ter data de validade definida para acompanhamento na tela Contratos.

## Certificados

A tela **Certificados** permite visualizar os certificados inseridos no Docnuvem durante o [cadastro de Empresas, ARs e Agências](07-meus-cadastros.md#cadastro-de-empresas-ars-e-agencias). Lista os certificados cadastrados, indica se estão vigentes ou vencidos e mostra a empresa, AR ou agência à qual cada um pertence.

### Como visualizar Certificados

1. No menu principal, acesse **Arquivos** e clique em **Certificados**.
2. A tela exibe a lista de certificados cadastrados. Use as informações da listagem para verificar o status atual do certificado e o registro de empresa, AR ou agência ao qual ele pertence.

**Resultado esperado:** o usuário consegue acompanhar certificados vigentes e vencidos, facilitando a manutenção dos registros.

## IA Documental

A **IA Documental** permite enviar documentos para processamento automático. Com base em regras configuradas, a IA pode identificar o tipo do documento, extrair metadados e direcionar arquivos para pastas específicas, reduzindo tarefas manuais e melhorando a organização.

### Como enviar arquivos pela IA Documental

1. No menu principal, acesse **Arquivos** e clique em **IA Documental**.
2. Arraste os documentos do computador para a área indicada, ou clique na área de envio para selecioná-los.

**Resultado esperado:** os documentos são enviados para processamento pela IA Documental.

### Como acompanhar o status na IA Documental

1. Abaixo dos filtros e da área de envio de arquivos, localize a listagem de documentos carregados.
2. Verifique o status de cada documento — pode indicar etapas como identificação do tipo de documento, extração de metadados e direcionamento para diretórios.

**Resultado esperado:** o usuário consegue acompanhar o processamento dos documentos enviados pela IA Documental.

### Como filtrar documentos na IA Documental

1. Na tela IA Documental, clique no balão **Filtrar**.
2. Preencha os filtros disponíveis, como status, data, responsável, tipo, nome ou outros critérios exibidos na tela.
3. Clique em **Filtrar** para atualizar a listagem.

**Resultado esperado:** a listagem exibe apenas os documentos que correspondem aos critérios informados.

### Como configurar regras de Envio Inteligente

As regras de **Envio Inteligente** definem como documentos processados pela IA Documental serão direcionados para pastas.

1. No menu principal, acesse **Meus modelos** → **Modelo de diretório**.
2. Na listagem, selecione o modelo de diretório que receberá as regras.
3. Clique em **Configurar Regras de Envio Inteligente**.
4. Configure os critérios que a IA utilizará para direcionar os documentos às pastas do modelo.

**Resultado esperado:** os documentos processados pela IA Documental podem ser direcionados automaticamente conforme as regras configuradas.

## Assinatura em massa

A tela **Assinatura em massa** permite assinar múltiplos documentos de uma só vez, reduzindo o tempo gasto em assinaturas repetitivas e facilitando o gerenciamento de documentos que exigem assinatura em lote.

### Como filtrar e assinar documentos em massa

1. No menu principal, acesse **Arquivos** e clique em **Assinatura em massa**.
2. Aplique os filtros necessários para localizar os documentos desejados, ou selecione todos os documentos listados quando essa for a ação desejada.
3. Clique em **Ações em massa** e marque a opção correspondente à ação desejada.

**Resultado esperado:** o usuário consegue executar a assinatura ou outra ação em lote sobre os documentos selecionados.

### Como configurar posição das assinaturas para assinatura em massa

Para usar assinatura em massa com posicionamento correto, o tipo de documento precisa ter assinantes e posição de assinatura configurados.

1. No menu principal, acesse **Tipos cadastrados** → **Tipo de documento** e selecione o tipo a configurar.
2. No cadastro do tipo de documento, acesse a aba **Configurações de assinatura**.
3. Na seção **Assinantes**, clique em **Adicionar** e selecione os assinantes necessários.

    !!! info "Importante"
        A configuração de posição de assinatura só é habilitada quando há assinantes cadastrados no tipo de documento.

4. Clique em **Configurar posição das assinaturas** (ou **Reconfigurar posição das assinaturas**, se o documento já tiver sido configurado antes).
5. Posicione os campos de assinatura no documento conforme necessário.

**Resultado esperado:** o tipo de documento fica configurado para uso em fluxos de assinatura em massa.

### Múltiplos assinadores via IA Documental

A IA Documental pode apoiar fluxos com múltiplos assinadores no mesmo documento, quando a parametrização estiver configurada.

Quando o documento possui dados de **CPF** ou **CNPJ**, a IA pode identificar os signatários e posicionar automaticamente os campos de assinatura — útil em processos que exigem anuência simultânea de vários envolvidos. O recurso pode ser combinado com a Assinatura em massa, ampliando a automação em documentos que exigem múltiplas assinaturas.

!!! info "Importante"
    Para novos modelos de documento ou ajustes em regras existentes, a equipe de suporte deve configurar a parametrização necessária para o funcionamento correto do processo.

**Resultado esperado:** documentos com múltiplos assinadores podem ser processados com menos configuração manual, desde que as regras estejam parametrizadas.

### Solicitação automática para diversos assinantes

O Docnuvem pode disparar solicitações automáticas de assinatura para vários assinantes em um único documento, quando o processo estiver parametrizado.

Em cenários configurados com apoio da IA, o sistema identifica participantes a partir de dados de CPF ou CNPJ presentes no arquivo e associa cada assinatura ao signatário correspondente. Use este recurso em fluxos que exigem a participação simultânea de vários responsáveis — a automação reduz a necessidade de configuração manual a cada envio.

!!! info "Importante"
    Para criar novos modelos ou alterar parametrizações existentes, a equipe de suporte deve ajustar a configuração antes do uso. Para preparar o tipo de documento, veja [Como configurar posição das assinaturas para assinatura em massa](#como-configurar-posicao-das-assinaturas-para-assinatura-em-massa).

**Resultado esperado:** as solicitações de assinatura podem ser disparadas automaticamente para diversos assinantes no mesmo documento, desde que a parametrização esteja configurada.

## Veja também

- [Meus Modelos](08-meus-modelos.md) — configuração de modelos de documento e diretório usados neste módulo.
- [Tipos Cadastrados](09-tipos-cadastrados.md) — configuração de assinatura no tipo de documento.
