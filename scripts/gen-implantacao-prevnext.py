#!/usr/bin/env python3
"""Insere/atualiza a navegação de passo anterior / próximo passo nas
páginas de etapa de docs/base-de-conhecimento/implantacao/.

Idempotente: usa marcadores HTML (<!-- prevnext:top --> / :bottom -->)
para poder ser executado de novo sem duplicar a navegação.

Ver a convenção documentada em docs/base-de-conhecimento/implantacao/index.md.

Uso: python3 scripts/gen-implantacao-prevnext.py   (a partir da raiz do repo)
"""
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "docs" / "base-de-conhecimento" / "implantacao"

STEPS = [
    ("01-inicio-do-processo.md", "1. Início do processo"),
    ("02-configuracoes-da-empresa.md", "2. Configurações da empresa"),
    ("03-outras-configuracoes.md", "3. Outras configurações"),
    ("04-configuracoes-avancado.md", "4. Configurações avançado"),
    ("05-funcionalidades-enterprise.md", "5. Funcionalidades Enterprise"),
    ("06-cadastro-do-primeiro-usuario.md", "6. Cadastro do primeiro usuário"),
    ("07-cadastro-do-contato-no-digisac.md", "7. Cadastro do contato no Digisac"),
    ("08-script-de-primeiro-contato.md", "8. Script de primeiro contato"),
    ("09-identidade-visual.md", "9. Identidade visual"),
    ("10-envio-da-playlist-standard.md", "10. Envio da playlist (Standard)"),
    ("11-solicitacao-modelos-documentos.md", "11. Solicitação de modelos de documentos"),
    ("12-cadastro-de-empresas-e-diretorios.md", "12. Cadastro de empresas e diretórios"),
    ("13-agendamento-do-treinamento.md", "13. Agendamento do treinamento"),
    ("14-envio-da-gravacao-do-treinamento.md", "14. Envio da gravação do treinamento"),
    ("15-solicitacao-do-envio-inteligente.md", "15. Solicitação do envio inteligente"),
    ("16-finalizacao-da-implantacao.md", "16. Finalização da implantação"),
]

TOP_START = "<!-- prevnext:top -->"
TOP_END = "<!-- /prevnext:top -->"
BOTTOM_START = "<!-- prevnext:bottom -->"
BOTTOM_END = "<!-- /prevnext:bottom -->"


def nav_line(i):
    is_first = i == 0
    is_last = i == len(STEPS) - 1

    if is_first:
        left = "[↑ Visão geral do processo](index.md)"
    else:
        prev_file, prev_label = STEPS[i - 1]
        left = f"← [Passo anterior: {prev_label}]({prev_file})"

    if is_last:
        right = "[Visão geral do processo ↑](index.md)"
    else:
        next_file, next_label = STEPS[i + 1]
        right = f"[Próximo passo: {next_label} →]({next_file})"

    return f"{left} · {right}"


def block(marker_start, marker_end, line):
    return f"{marker_start}\n{line}\n{marker_end}"


def strip_existing(text, start, end):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end) + r"\n?", re.DOTALL)
    return pattern.sub("", text)


def main():
    for i, (fname, _label) in enumerate(STEPS):
        path = DIR / fname
        text = path.read_text(encoding="utf-8")

        # Remove blocos antigos (se o script já rodou antes) para não duplicar.
        text = strip_existing(text, TOP_START, TOP_END)
        text = strip_existing(text, BOTTOM_START, BOTTOM_END)

        line = nav_line(i)
        top_block = block(TOP_START, TOP_END, line)
        bottom_block = block(BOTTOM_START, BOTTOM_END, line)

        # Inserir o bloco do topo logo após o H1 (primeira linha "# ...").
        lines = text.split("\n")
        h1_idx = next(idx for idx, l in enumerate(lines) if l.startswith("# "))
        # Remove linhas em branco extras logo após o H1 que possam ter sobrado.
        insert_at = h1_idx + 1
        while insert_at < len(lines) and lines[insert_at].strip() == "":
            del lines[insert_at]
        lines[insert_at:insert_at] = ["", top_block, ""]
        text = "\n".join(lines)

        # Inserir o bloco do fim ao final do arquivo.
        text = text.rstrip("\n") + "\n\n" + bottom_block + "\n"

        path.write_text(text, encoding="utf-8")
        print(f"ok: {fname}")


if __name__ == "__main__":
    main()
