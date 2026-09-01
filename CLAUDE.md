# CLAUDE.md — Docnuvem Docs & Base de Conhecimento

Este arquivo dá contexto para qualquer sessão do Claude (Code ou Cowork) que continue este projeto. Leia inteiro antes de gerar conteúdo.

## O que é este projeto

Site estático (MkDocs Material, publicado via GitHub Pages) com dois conteúdos distintos, navegados separadamente mas publicados juntos:

1. **Manual do Sistema** (`docs/manual/`) — documentação de referência do produto Docnuvem (SaaS de GED). O que cada tela faz e como usá-la. Público: usuários do sistema, incluindo clientes.
2. **Base de Conhecimento Interna** (`docs/base-de-conhecimento/`) — processos operacionais do time de Suporte e do setor de Implantações. Não é "como usar o sistema", é "como fazer o nosso trabalho" (conduzir uma implantação, atender um chamado, decidir o que e quando escalar). Público: equipe interna.

**Regra inviolável: nunca misturar os dois dentro da mesma página.** Um card cruzado ("Veja também") entre um artigo da Base de Conhecimento e a seção correspondente do Manual é bem-vindo; fundir o conteúdo não.

Há uma terceira trilha, `docs/central-de-ajuda/`, decidida durante a montagem do site (ver "Decisões já tomadas" abaixo) — não confundir com a Base de Conhecimento Interna.

## Quem sou eu e por que isso existe agora

Breno é responsável pela gestão do time de Suporte e, sozinho, pelo setor de Implantações (apoio pontual do resto do time, mas execução e decisões do dia a dia são dele). **Ele sai de férias em 17/09/2026.** Este site é o material que permite o time continuar implantando clientes e resolvendo chamados sem depender dele durante esse período — e depois também, como material permanente da empresa.

**Prioridade #1, sempre que houver conflito de tempo: a Base de Conhecimento Interna vem antes do Manual do Sistema.** O Manual já tem bastante conteúdo-fonte disponível (vault do Obsidian); o que não existe em lugar nenhum ainda são os processos de Implantação e os fluxos de Suporte, que estão só na cabeça do Breno. Não avançar em polir o Manual enquanto houver processos críticos de Implantação sem documentar.

## Fontes de conteúdo

- `vaults/docnuvem-base/` — vault do Obsidian do Breno, é a fonte **prioritária e atual** do Manual (mais recente que qualquer PDF). Tratar como somente-leitura/referência — é o vault de trabalho dele no Obsidian, não mexer na estrutura interna dele.
  - `vaults/docnuvem-base/Manual DOCNUVEM/` — conteúdo do manual, organizado por módulo (uma nota-índice por módulo + pasta com as notas filhas). Mais completo que qualquer esboço anterior: inclui **Arquivos, Módulo de Tarefas, Auditoria, Lixeira, Relatórios e Assistente IADoc**, que não faziam parte de nenhuma listagem original do produto.
  - `vaults/docnuvem-base/Base de Conhecimento/` — **não é a Base de Conhecimento Interna do site.** É uma camada de referência/FAQ voltada a quem *usa* o sistema (visão geral, fluxos essenciais, troubleshooting de uso, FAQ, glossário), incluindo uma nota "Regras de resposta da IA" pensada para orientar um assistente de IA respondendo usuários finais. Decisão tomada: publicar esse conteúdo como seção própria `docs/central-de-ajuda/`, nunca misturado com `base-de-conhecimento/`.
  - Duas notas dessa pasta são **internas ao processo de manutenção do vault, não devem virar página do site**: `06 - Regras de resposta da IA.md` e `07 - Fila de atualização.md` (esta última é um backlog de lacunas, útil para nós consultarmos, não para publicar).
  - `vaults/docnuvem-base/Roteiros de Vídeos/` — roteiros de vídeo, fora do escopo deste site. Ignorar para fins de conteúdo publicado.
  - O vault tem uma nota `Diretrizes de geração de manuais.md` descrevendo um **pipeline paralelo e ativo de geração de PDF via LaTeX** (repo separado `doc_manuals`, sincronizado com `G:\Meu Drive\Atualização do Manual 2026\...`, mencionando outras IAs "Codex"/"Antigravity" trabalhando nisso). **Decisão do Breno: ignorar completamente.** Não tocar no repo `doc_manuals`, não seguir essas diretrizes de LaTeX/print, não tentar sincronizar as duas coisas. Só usamos as notas de conteúdo do vault como fonte de texto.
- `sources/manual-antigo.pdf` — **não foi adicionado e, por decisão do Breno, não vamos esperar por ele.** Seguir só com o vault do Obsidian para o Manual. Se ele aparecer futuramente em `sources/`, comparar e usar só para preencher lacunas (ex.: os módulos ainda vazios no vault).
- Ditados/rascunhos brutos que o Breno vai fornecer ao longo do trabalho, descrevendo processos de Implantação e Suporte ainda não escritos em lugar nenhum. Vão chegar desorganizados de propósito — a tarefa é estruturar, não só copiar.
- Site do produto: https://docnuvem.com.br/

**Atenção:** o vault descreve a versão atual do sistema. Uma nova versão do Docnuvem está em desenvolvimento e ainda não foi lançada. Documentar o sistema como ele é hoje; se o Breno sinalizar que algo é específico da versão atual e pode mudar em breve, marcar a página com aviso curto, não excluir.

## Decisões já tomadas (não reabrir sem o Breno pedir)

1. Conteúdo da pasta "Base de Conhecimento" do vault → publicado como seção própria **Central de Ajuda** (`docs/central-de-ajuda/`), separada do Manual e da Base de Conhecimento Interna.
2. Pipeline paralelo de PDF/LaTeX (`doc_manuals`, Codex/Antigravity) → ignorar completamente.
3. `manual-antigo.pdf` → não vamos esperar por ele; seguir só com o vault.
4. `sources/obsidian-vault/` do esboço original de estrutura virou `vaults/docnuvem-base/` (caminho real onde o Breno colocou o vault) — não mover/renomear essa pasta, é o vault ativo dele no Obsidian.

## Estrutura do repositório (já criada)

```
docnuvem-base/
├── CLAUDE.md                      # este arquivo
├── mkdocs.yml
├── requirements.txt                # mkdocs-material
├── .github/workflows/gh-pages.yml  # publica no GitHub Pages a cada push em main
├── .gitignore                      # ignora site/, estado local do Obsidian
├── docs/
│   ├── index.md
│   ├── manual/
│   │   ├── index.md
│   │   ├── 01-antes-de-comecar.md
│   │   ├── 02-acessando-o-sistema.md
│   │   ├── 03-dashboard.md
│   │   ├── 04-meus-documentos.md
│   │   ├── 05-busca-avancada.md
│   │   ├── 06-notificacoes.md          # SEM conteúdo-fonte no vault ainda
│   │   ├── 07-meus-cadastros.md
│   │   ├── 08-meus-modelos.md
│   │   ├── 09-tipos-cadastrados.md
│   │   ├── 10-arquivos.md
│   │   ├── 11-modulo-de-tarefas.md
│   │   ├── 12-auditoria.md
│   │   ├── 13-lixeira.md
│   │   ├── 14-relatorios.md            # SEM conteúdo-fonte no vault ainda
│   │   ├── 15-assistente-iadoc.md      # SEM conteúdo-fonte no vault ainda
│   │   └── 16-perguntas-frequentes.md
│   ├── central-de-ajuda/
│   │   ├── index.md
│   │   ├── visao-geral.md
│   │   ├── fluxos-essenciais.md
│   │   ├── diagnostico-troubleshooting.md
│   │   ├── faq.md
│   │   └── glossario.md
│   └── base-de-conhecimento/
│       ├── index.md
│       ├── contingencia.md         # PLACEHOLDER — falta conteúdo real, ver abaixo
│       ├── implantacao/index.md    # PLACEHOLDER — aguardando ditados do Breno
│       └── suporte/index.md        # PLACEHOLDER — aguardando ditados do Breno
└── vaults/docnuvem-base/           # vault do Obsidian do Breno (fonte, não editar a estrutura)
```

Todas as páginas fora de `docs/index.md` que ainda não têm conteúdo real estão marcadas com `> Página em construção.` + comentário `<!-- TODO: ... -->` explicando o que falta.

## Diretrizes de conteúdo

- Idioma: português do Brasil, em todas as páginas.
- Tom do Manual: instrucional, neutro, terceira pessoa ou imperativo ("Clique em...", "Acesse..."). Documentação de produto, não precisa soar pessoal.
- Tom da Central de Ajuda: direto, como referência rápida de apoio ao Manual.
- Tom da Base de Conhecimento Interna: direto e prático, como se estivesse orientando um colega novo na função. Frases curtas, listas numeradas em vez de parágrafos longos — quem consulta está no meio de um atendimento ou de uma implantação.
- **Todo processo da Base de Conhecimento Interna precisa responder: quando isso se aplica, o que fazer passo a passo, e o que fazer se travar (para quem escalar).** Um artigo sem a parte "se travar" está incompleto.
- Ao migrar conteúdo do vault, reescrever, não só copiar — simplificar frases longas, mas sem inventar nada que não esteja na fonte.
- Sempre que uma página do Manual for relevante para um processo da Base de Conhecimento Interna, adicionar link cruzado ao final ("Veja também: ...").
- Não inventar funcionalidades, campos ou comportamentos do sistema que não estejam nas fontes. Sem informação suficiente → deixar `<!-- TODO: confirmar com Breno -->` em vez de supor.
- Não presumir estrutura de permissões, cargos ou nomes de pessoas da equipe que o Breno não tenha informado explicitamente.

## Plano de contingência — ALTA PRIORIDADE, ainda incompleto

`docs/base-de-conhecimento/contingencia.md` existe como placeholder (exigência do projeto: deve existir desde o primeiro commit publicado), mas falta conteúdo real. Precisa, assim que o Breno tiver tempo:

1. O que a equipe faz diante de uma situação de implantação/suporte não coberta pela documentação.
2. Quem é o backup/responsável por decisões durante o período de férias.
3. Como e quando (se for o caso) acionar o Breno nas férias.

Manter esta página sempre visível/linkada com destaque na home (`docs/index.md`) — já está.

## Fluxo de trabalho (ordem de execução)

1. ✅ Ler fontes disponíveis e devolver sumário comparativo (feito).
2. ✅ Configurar `mkdocs.yml` e árvore de pastas vazia com placeholders (feito).
3. ⏳ **Em andamento — próximo passo real.** Priorizar a Base de Conhecimento Interna: gerar as páginas de Implantação e Suporte a partir dos ditados do Breno, uma de cada vez, pedindo confirmação antes de avançar quando houver dúvida de conteúdo.
4. Criar a página de Plano de Contingência com conteúdo real (ver seção acima).
5. Migrar o Manual do Sistema a partir do vault do Obsidian, seção por seção, na ordem do sumário (`vaults/docnuvem-base/Manual DOCNUVEM/Docnuvem.md`).
6. Ao final de cada seção concluída (Manual, Central de Ajuda ou Base de Conhecimento), fazer um commit isolado com mensagem descritiva — nunca gerar tudo em um commit único.
7. Publicar cedo: o site já está com Actions configurado para publicar a cada push em `main`; não esperar o Manual estar completo.

## O que evitar

- Não gerar todas as páginas de uma vez sem revisão intermediária.
- Não remover conteúdo do vault só porque parece desatualizado — marcar com aviso, perguntar antes de excluir.
- Não usar linguagem de marketing/institucional nas páginas de Base de Conhecimento Interna — é material operacional interno.
- Não misturar Manual e Base de Conhecimento Interna na mesma página.
- Não mexer no pipeline paralelo de PDF/LaTeX (`doc_manuals`) nem nos arquivos do Google Drive mencionados no vault.

## Notas técnicas

- `mkdocs build --strict` foi validado (sem erros) rodando num ambiente com rede disponível — a máquina do Breno, pelo menos via este bridge, não tem acesso à internet para instalar `mkdocs-material` via pip. Rodar `pip install -r requirements.txt` num terminal com rede normal antes de `mkdocs serve` localmente.
- GitHub Actions (`.github/workflows/gh-pages.yml`) publica automaticamente a cada push em `main` — não precisa rodar `mkdocs gh-deploy` manualmente.
- Identidade git configurada localmente neste repo: `breno-docnuvem <breno@docnuvem.com.br>` (mesma do commit inicial).
- Estado no último push conhecido: `main` sincronizado com `origin/main`, 3 commits (`Initial commit`, `docs: adiciona vault do Obsidian como material-fonte`, `chore: estrutura inicial do site`).
