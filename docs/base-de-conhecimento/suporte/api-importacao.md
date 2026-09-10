# API Docnuvem — Importação

## O que é

API REST (OAS3) para integração externa com o Docnuvem: importar arquivos, gerar documentos a partir de modelo, solicitar assinatura eletrônica, consultar status e baixar documentos.

- Documentação interativa (Swagger UI): [swagger-ui/index.html](http://docnuvem-1325424578.sa-east-1.elb.amazonaws.com:8083/swagger-ui/index.html)
- Especificação OAS3: [/v3/api-docs/importacao](http://docnuvem-1325424578.sa-east-1.elb.amazonaws.com:8083/v3/api-docs/importacao)
- Server: `http://docnuvem-1325424578.sa-east-1.elb.amazonaws.com:8083`
- Autenticação: Bearer Token, no header `Authorization` da maioria dos endpoints.

> Esta página traz um resumo com as regras de negócio que não ficam óbvias só lendo o Swagger. Parâmetros, schemas e exemplos completos de request/response ficam sempre atualizados na documentação interativa acima — evite copiar isso aqui, porque desatualiza rápido.

## Importar arquivo

**POST `/importar`** — envia um arquivo para ser processado e armazenado em uma pasta específica. Retorna o link de visualização e o `documentoId`, usado nos demais endpoints.

Parâmetros principais: `instancia`, `nomeArquivo`, `nomePasta`, `nomePastaPai` (opcional), `Authorization`, e o arquivo (`multipart/form-data`).

**POST `/enviarParaEnvioInteligente`** — mesma ideia, mas envia o arquivo para o Envio Inteligente processar. Não retorna `diretorioId`: quem classifica a pasta do documento é o próprio Envio Inteligente, depois.

## Gerar documento a partir de modelo

**POST `/api/documento/from-template`** — preenche as variáveis de um modelo já cadastrado na instância e arquiva o PDF resultante, devolvendo o `documentoId` (usado depois em `POST /api/assinatura`).

O modelo é cadastrado pela interface do Docnuvem — esta API não cria nem edita modelo. Use `GET /api/modelos` para descobrir o código do modelo e as variáveis que ele espera.

Pontos que costumam derrubar a primeira integração:

- A **pasta precisa existir**. Diferente do `/importar`, este endpoint não cria pasta — criar uma árvore de pastas como efeito colateral de gerar um contrato é um problema grande para quem só errou o nome.
- A chave do mapa `variaveis` casa com o marcador do campo ignorando acento, pontuação e caixa: `nomeCliente` casa com `[NOMECLIENTE]`.
- O valor vai como texto, mas é convertido para o tipo do campo: **data** em `dd/MM/yyyy`, **numérico** como `1.234,56` (sem símbolo de moeda), **caixa de seleção** como `sim/não`, **lista de opções** com um dos valores cadastrados.
- Variável do modelo sem valor responde `400` com a lista em `variaveisFaltantes`. Chave a mais no payload é ignorada — o mesmo payload pode servir a modelos diferentes.
- Campo de **endereço** e de **seleção múltipla** ainda não são preenchidos por API — `GET /api/modelos` marca isso em `aceitaPorApi`.

Exemplo de payload:

```json
{
  "modelo": "contrato_locacao_v1",
  "nomeArquivo": "Contrato_ClienteX.pdf",
  "nomePasta": "Contratos",
  "nomePastaPai": "Clientes/Cliente Exemplo",
  "referenciaExterna": "card_98765",
  "variaveis": {
    "razaoSocial": "Cliente Exemplo LTDA",
    "dataInicio": "03/09/2026"
  }
}
```

**GET `/api/modelos`** — lista os modelos ativos da instância com código, nome e as variáveis esperadas (chave, rótulo, tipo, obrigatoriedade, opções). É por aqui que se descobre o que mandar no `from-template`: o identificador da variável é o marcador do template, não o rótulo mostrado na tela.

Dois campos merecem atenção: `aceitaPorApi` vem falso nos tipos que a API ainda não preenche (endereço e seleção múltipla), e `preenchidoPeloDestinatario` marca o campo que a outra ponta preenche depois pela página pública — esse não deve vir no payload.

## Solicitar assinatura

**POST `/api/assinatura`** — cria uma solicitação de assinatura para um documento já importado. Devolve o link de cada signatário, que o integrador envia pelo canal que quiser — **nenhum e-mail é enviado por este endpoint**.

Pontos que costumam derrubar a primeira integração:

- `cpf` é obrigatório por signatário e é validado (11 dígitos com dígitos verificadores corretos, com ou sem máscara). CPF ausente ou inválido responde `400` dizendo qual signatário e por quê — nunca é aceito para falhar depois, porque a página pública de assinatura mostra o CPF.
- Com `consideraOrdem: true`, a `ordem` precisa ser 0-based e contígua (0, 1, 2...), uma por signatário.
- `metodos` define o que a página oferece: `digital` e `birdid` exigem certificado do signatário; o padrão é `eletronica`, para signatário externo.
- Um documento só pode ter um fluxo de assinatura em andamento por vez — cancele o atual antes de abrir outro.
- `lembretes: [1, 7]` faz o Docnuvem cobrar por e-mail em D+1 e D+7 da solicitação, só quem ainda não assinou. Sem essa lista, nenhum lembrete sai. O envio ignora a configuração de "e-mail de pendência de assinatura" da instância, porque a cadência foi pedida explicitamente nessa chamada — e sai ao longo do dia pela rotina diária do Docnuvem, não na hora.
- `referenciaExterna` (até 64 caracteres) é gravado e devolvido intacto no status e na listagem, sem validação — serve para correlacionar o fluxo com o registro do lado do integrador por chave exata, em vez de por nome de arquivo.

**DELETE `/api/assinatura/{assinaturaId}`** — cancela uma solicitação de assinatura. Derruba o fluxo inteiro: a solicitação e **todos** os signatários (inclusive quem já assinou) passam a `cancelado`, e os links de assinatura param de funcionar. Vale tanto para solicitação em andamento quanto vencida.

Quando alguém já assinou, o arquivo volta à versão anterior às assinaturas (elas ficam dentro do PDF, não só no banco); nada é apagado, o bucket tem versionamento. Se não for possível identificar com segurança qual versão restaurar (fluxos antigos, sem vínculo entre versão e signatário), o cancelamento é recusado com `409` em vez de restaurar a versão errada — nesse caso, usar a tela do Docnuvem.

## Consultar e baixar documentos

**GET `/api/documentos`** — lista documentos da instância, do mais recente ao mais antigo, com filtros opcionais combináveis: `diretorioId` (+ `incluirSubpastas`), `status` (`pendente`, `assinado`, `expirado`, `cancelado`, `sem_assinatura` — sempre da solicitação mais recente do documento) e período (`dataInicio`/`dataFim`). Documentos na lixeira ficam de fora. Resposta paginada (até 200 por página, padrão 50) — usar `temMais` para saber se vale pedir a próxima página.

**GET `/api/documento/{documentoId}/status`** — situação da assinatura de um documento e o detalhe por signatário. `recusado` não existe no Docnuvem hoje — o signatário assina ou deixa vencer. Documentos reenviados para assinatura ganham um fluxo novo; o que volta é sempre o mais recente.

**GET `/api/documento/{documentoId}/download`** — gera um link de download temporário (S3), válido por 15 minutos e que não pode ser revogado depois de emitido — tratar como credencial, gerar só na hora de baixar. A trilha de auditoria já vem dentro do próprio PDF assinado, como página de relatório; quando o relatório também existe como documento separado, ele vem em `relatorioAssinatura` com sua própria URL.

## Se travar

Dúvidas técnicas sobre a API ou sobre uma integração específica de cliente: perguntar ao **Breno**. Se ele não estiver disponível, acionar o **Victor** — ver [Plano de Contingência](../contingencia.md).

## Relacionados

- [Plano de Contingência](../contingencia.md)
