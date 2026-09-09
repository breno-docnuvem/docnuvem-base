---
tipo: processo
area: suporte
etapa: "1"
status: publicado
ultima_revisao: 2026-09-09
---

# 01 - O que é o Sincronizador

## Quando se aplica

Antes de instalar ou explicar o Sincronizador para um cliente — para entender o que a ferramenta faz e como ela se diferencia do Agente Docnuvem.

## O que é

O Sincronizador é um programa instalado no computador do colaborador que mantém uma pasta local sincronizada com uma pasta do Docnuvem. Ao instalar, todos os arquivos que já estão na plataforma são baixados para a pasta selecionada, e qualquer alteração feita de um dos lados — Docnuvem Web ou pasta local — é refletida automaticamente no outro.

Roda como serviço do Windows (inicia sozinho com o computador, não depende de nenhum usuário Windows logado) e, opcionalmente, com um ícone na bandeja que mostra o status e dá acesso rápido a algumas ações.

## Diferença em relação ao Agente Docnuvem

| | Sincronizador | Agente Docnuvem |
|---|---|---|
| Sentido da sincronização | Mão dupla (computador ⇄ Docnuvem) | Mão única (computador → Docnuvem) |
| Uso | Módulo comercial, vendido normalmente | Uso interno, só em casos pontuais (ver [[Agente Docnuvem (robô)]]) |
| Roda como | Serviço do Windows | Programa convencional ou serviço, conforme o caso |

## Onde o programa fica disponível

O repositório com o instalador, versões e changelog fica em: https://drive.google.com/drive/folders/1nVb_sFIwXLARTo_iH96bG1mbHaNuXf_n?usp=sharing — ver [[02 - Como se localizar no repositório]] para a estrutura de pastas.

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para dúvidas gerais sobre o Sincronizador. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- Próxima etapa: [[02 - Como se localizar no repositório]]
