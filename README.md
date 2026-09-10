# Docnuvem — Documentação

Repositório fonte da documentação do Docnuvem, publicada como site estático em [GitHub Pages](https://breno-docnuvem.github.io/docnuvem-base/) com [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

O site reúne três conteúdos separados, para públicos diferentes, que nunca se misturam:

- **Manual do Sistema** — referência de cada tela do produto, para qualquer pessoa que usa o sistema (inclusive clientes).
- **Central de Ajuda** — visão geral, fluxos essenciais, diagnóstico rápido e FAQ, um complemento mais direto ao Manual.
- **Base de Conhecimento Interna** — processos operacionais dos times de Suporte e Implantação. Uso interno.

## Estrutura do repositório

```
docs/                     # site publicado (fonte do MkDocs)
  manual/                   → Manual do Sistema
  central-de-ajuda/         → Central de Ajuda
  base-de-conhecimento/     → Base de Conhecimento Interna
vaults/docnuvem-base/      # vault do Obsidian — onde o conteúdo é escrito e revisado
mkdocs.yml                 # configuração do site e navegação
requirements.txt           # dependências Python (mkdocs-material)
.github/workflows/         # publicação automática no GitHub Pages
CLAUDE.md                  # convenções do repositório para colaboração com IA
```

## Fluxo de trabalho

O conteúdo é escrito e revisado primeiro no vault do Obsidian (`vaults/docnuvem-base/`), em notas atômicas, e só depois espelhado para `docs/` no formato publicado (sem front matter, wikilinks convertidos em links relativos, avisos como admonitions do MkDocs). Ver `CLAUDE.md` para as convenções completas.

## Rodando localmente

```bash
pip install -r requirements.txt
mkdocs serve      # site local em http://127.0.0.1:8000
mkdocs build      # gera a pasta site/ (mesmo conteúdo publicado no Pages)
```

## Publicação

Todo push em `main` dispara `.github/workflows/gh-pages.yml`, que builda o site com MkDocs e publica no GitHub Pages automaticamente.
