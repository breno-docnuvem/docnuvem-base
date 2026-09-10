# Prompt para o Claude Code — publicar as notas do Sincronizador na GitHub Page

Copie e cole o texto abaixo numa sessão do Claude Code aberta na raiz do repositório `docnuvem-base`.

---

No vault do Obsidian (`vaults/docnuvem-base/Base de Conhecimento Interna/Suporte/`) eu já dividi a nota provisória do Sincronizador em notas atômicas, seguindo exatamente o mesmo padrão usado para o Agente Docnuvem (robô). Preciso que você espelhe esse conteúdo na documentação publicada (`docs/`), do mesmo jeito que já foi feito para `agente-docnuvem/`.

## 1. Arquivos novos no vault (fonte da verdade)

Dentro de `vaults/docnuvem-base/Base de Conhecimento Interna/Suporte/`:

- `Sincronizador Docnuvem.md` (índice do processo)
- `01 - O que é o Sincronizador.md`
- `02 - Como se localizar no repositório.md`
- `03 - Antes de instalar (ativar o módulo na empresa).md`
- `04 - Baixar os arquivos de instalação.md`
- `05 - Configurar o application.yml.md`
- `06 - Instalar e iniciar o serviço.md`
- `07 - Instalar o ícone de bandeja.md`
- `08 - Testar a instalação.md`
- `09 - Vincular cada máquina a um usuário.md`
- `10 - Ativar a exigência de usuário na empresa.md`
- `11 - Como funciona o controle de permissões ativo.md`
- `12 - Migrando máquinas aos poucos.md`
- `13 - Cores do ícone da bandeja.md`
- `14 - Operação do dia a dia.md`
- `15 - Solução de problemas.md`

E imagens novas em:
- `vaults/docnuvem-base/Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/01-pasta-estrutura-padrao-drive.png`
- `vaults/docnuvem-base/Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/02-configurar-usuario-ps1-na-raiz.png`
- `vaults/docnuvem-base/Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/03-jar-na-pasta-app.png`
- `vaults/docnuvem-base/Base de Conhecimento Interna/images/suporte/sincronizador/10-ativar-a-exigencia-de-usuario-na-empresa/01-tela-configuracoes-sincronizador.png`

A nota "05" reaproveita uma imagem que já existe do Agente Docnuvem, em `vaults/docnuvem-base/Base de Conhecimento Interna/images/suporte/agente-docnuvem/04-configurar-o-default-properties/01-gerar-token.png` — não duplicar, só referenciar via caminho relativo na versão publicada.

## 2. Criar `docs/base-de-conhecimento/suporte/sincronizador/`

Mesma estrutura de `docs/base-de-conhecimento/suporte/agente-docnuvem/`: um `index.md` + um `.md` por etapa + uma subpasta `images/`.

Regras de conversão (as mesmas já aplicadas ao Agente Docnuvem — comparar com os arquivos existentes em `agente-docnuvem/` se tiver dúvida de formatação):

- Remover o frontmatter (`tipo`, `area`, `etapa`, `status`, `ultima_revisao`) — a versão publicada não usa isso.
- Nomes de arquivo em kebab-case, sem acento, mantendo o número: `01 - O que é o Sincronizador.md` → `01-o-que-e-o-sincronizador.md`. Slugs completos, na ordem:
  1. `01-o-que-e-o-sincronizador.md`
  2. `02-como-se-localizar-no-repositorio.md`
  3. `03-antes-de-instalar-ativar-o-modulo-na-empresa.md`
  4. `04-baixar-os-arquivos-de-instalacao.md`
  5. `05-configurar-o-application-yml.md`
  6. `06-instalar-e-iniciar-o-servico.md`
  7. `07-instalar-o-icone-de-bandeja.md`
  8. `08-testar-a-instalacao.md`
  9. `09-vincular-cada-maquina-a-um-usuario.md`
  10. `10-ativar-a-exigencia-de-usuario-na-empresa.md`
  11. `11-como-funciona-o-controle-de-permissoes-ativo.md`
  12. `12-migrando-maquinas-aos-poucos.md`
  13. `13-cores-do-icone-da-bandeja.md`
  14. `14-operacao-do-dia-a-dia.md`
  15. `15-solucao-de-problemas.md`
  - `Sincronizador Docnuvem.md` → `index.md`
- Wikilinks `[[Nome da Nota]]` → link markdown relativo ao arquivo de destino, ex.: `[[09 - Vincular cada máquina a um usuário]]` → `[09 - Vincular cada máquina a um usuário](09-vincular-cada-maquina-a-um-usuario.md)`.
- Embeds de imagem `![[Base de Conhecimento Interna/images/suporte/sincronizador/<pasta>/<arquivo>.png]]` → `![<texto alternativo descritivo>](images/<pasta>/<arquivo>.png)`, copiando a imagem para `docs/base-de-conhecimento/suporte/sincronizador/images/<pasta>/<arquivo>.png`.
  - A imagem reaproveitada do Agente (na nota 05) vira `![Geração do token da instância na plataforma.](../agente-docnuvem/images/04-configurar-o-default-properties/01-gerar-token.png)` — sem copiar o arquivo, só apontando pra pasta que já existe.
- Blocos `> ⚠️ **Texto**` → admonition do MkDocs Material, escolhendo o título pelo contexto (`!!! warning "Importante"`, `!!! warning "Atenção"` etc.), do mesmo jeito que já foi feito em `agente-docnuvem/04-configurar-o-default-properties.md`.
- Comentários `<!-- TODO: ... -->` permanecem como estão (viram comentário HTML invisível no site publicado).
- Na nota-índice (`Sincronizador Docnuvem.md`), a seção `## Relacionados` vira `## Veja também` na versão publicada (mesmo padrão do índice do Agente Docnuvem). Nas demais notas, `## Relacionados` continua se chamando `## Relacionados`.
- Links cruzados para o Agente Docnuvem (ex.: no índice e na nota 01) devem apontar para `../agente-docnuvem/index.md`.

## 3. Atualizar `docs/base-de-conhecimento/suporte/index.md`

Adicionar um item na lista de "## Processos", ao lado do Agente Docnuvem:

```
- [Sincronizador Docnuvem](sincronizador/index.md) — passo a passo de instalação do Sincronizador e do controle de permissões por usuário.
```

## 4. Atualizar `mkdocs.yml`

Dentro do bloco `Suporte:` (mesmo nível de `Agente Docnuvem (robô):`), acrescentar:

```yaml
          - Sincronizador Docnuvem:
              - Visão geral do processo: base-de-conhecimento/suporte/sincronizador/index.md
              - 1. O que é o Sincronizador: base-de-conhecimento/suporte/sincronizador/01-o-que-e-o-sincronizador.md
              - 2. Como se localizar no repositório: base-de-conhecimento/suporte/sincronizador/02-como-se-localizar-no-repositorio.md
              - 3. Antes de instalar (ativar o módulo na empresa): base-de-conhecimento/suporte/sincronizador/03-antes-de-instalar-ativar-o-modulo-na-empresa.md
              - Instalação na máquina do cliente:
                  - 4. Baixar os arquivos de instalação: base-de-conhecimento/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao.md
                  - 5. Configurar o application.yml: base-de-conhecimento/suporte/sincronizador/05-configurar-o-application-yml.md
                  - 6. Instalar e iniciar o serviço: base-de-conhecimento/suporte/sincronizador/06-instalar-e-iniciar-o-servico.md
                  - 7. Instalar o ícone de bandeja: base-de-conhecimento/suporte/sincronizador/07-instalar-o-icone-de-bandeja.md
              - 8. Testar a instalação: base-de-conhecimento/suporte/sincronizador/08-testar-a-instalacao.md
              - Controle de permissões por usuário (opcional):
                  - 9. Vincular cada máquina a um usuário: base-de-conhecimento/suporte/sincronizador/09-vincular-cada-maquina-a-um-usuario.md
                  - 10. Ativar a exigência de usuário na empresa: base-de-conhecimento/suporte/sincronizador/10-ativar-a-exigencia-de-usuario-na-empresa.md
              - 11. Como funciona o controle de permissões ativo: base-de-conhecimento/suporte/sincronizador/11-como-funciona-o-controle-de-permissoes-ativo.md
              - 12. Migrando máquinas aos poucos: base-de-conhecimento/suporte/sincronizador/12-migrando-maquinas-aos-poucos.md
              - 13. Cores do ícone da bandeja: base-de-conhecimento/suporte/sincronizador/13-cores-do-icone-da-bandeja.md
              - 14. Operação do dia a dia: base-de-conhecimento/suporte/sincronizador/14-operacao-do-dia-a-dia.md
              - 15. Solução de problemas: base-de-conhecimento/suporte/sincronizador/15-solucao-de-problemas.md
```

## 5. Limpeza pendente (arquivos que eu não consegui apagar)

Não tenho permissão de exclusão de arquivos no seu computador nesta sessão, então deixei três coisas para você resolver com `git rm` / `rm`:

1. `vaults/docnuvem-base/Sincronizador Docnuvem(nota provisória).md` — já foi totalmente dividido nas notas atômicas acima, pode ser removido do vault.
2. `_to_delete/Sincronizador Docnuvem(nota provisória).md` (raiz do repositório) — cópia de segurança da nota provisória que eu deixei lá antes de conseguir dividir; pode remover junto com o item 1.
3. `vaults/docnuvem-base/captura-ativar-modulo-sincronizador.png` (raiz do vault) — a screenshot já foi copiada para o lugar certo em `Base de Conhecimento Interna/images/suporte/sincronizador/10-ativar-a-exigencia-de-usuario-na-empresa/01-tela-configuracoes-sincronizador.png`; esse arquivo solto na raiz do vault ficou duplicado e pode ser removido.
4. `vaults/docnuvem-base/Base de Conhecimento Interna/Suporte/04 - Baixar e descompactar o pacote.md` — versão antiga da etapa 4, substituída por `04 - Baixar os arquivos de instalação.md` (o processo de instalação mudou: agora baixa a pasta `docnuvem-sincronizador` de dentro de "estrutura padrão" e depois sobrepõe `configurar-usuario.ps1` e o `.jar` vindos de "versão atual", em vez de baixar um pacote único já pronto). Pode remover o arquivo antigo.

## 6. Build e commit

Rodar o build do MkDocs localmente para conferir que não há link quebrado nem imagem faltando, depois commitar tudo (vault + docs + mkdocs.yml + as remoções do item 5) com uma mensagem descrevendo a criação da página do Sincronizador Docnuvem na Base de Conhecimento Interna, seguindo o padrão de commit já usado para o Agente Docnuvem.
