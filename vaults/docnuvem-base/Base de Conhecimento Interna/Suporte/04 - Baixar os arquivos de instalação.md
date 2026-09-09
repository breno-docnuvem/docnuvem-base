---
tipo: processo
area: suporte
etapa: "4.1"
status: publicado
ultima_revisao: 2026-09-09
---

# 04 - Baixar os arquivos de instalação

## Quando se aplica

Depois de ativado o módulo na empresa (ver [[03 - Antes de instalar (ativar o módulo na empresa)]]) — primeiro passo prático de uma instalação nova (máquina que nunca teve o Sincronizador instalado).

## Passo a passo

1. Dentro do repositório (ver [[02 - Como se localizar no repositório]]), abrir a pasta **"estrutura padrão"** e baixar a pasta `docnuvem-sincronizador` que fica lá dentro. Colocar em um local fixo da máquina, por exemplo `C:\docnuvem-sincronizador\`.

   ![[Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/01-pasta-estrutura-padrao-drive.png]]

2. Dentro da pasta **"versão atual"**, baixar o arquivo `configurar-usuario.ps1` e colocar na raiz da pasta `docnuvem-sincronizador` (mesmo nível de `docnuvem-sync.exe`, `instalar-tray.ps1` etc.), substituindo o que já estiver lá.

   ![[Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/02-configurar-usuario-ps1-na-raiz.png]]

3. Ainda dentro de **"versão atual"**, baixar o arquivo `docnuvem-sincronizador.jar` (o programa do Sincronizador em si) e colocar em `docnuvem-sincronizador\app\`.

   ![[Base de Conhecimento Interna/images/suporte/sincronizador/04-baixar-os-arquivos-de-instalacao/03-jar-na-pasta-app.png]]

## Na prática

"Estrutura padrão" já traz pronta a base da instalação: o executável `docnuvem-sync.exe`, o Java embutido (pasta `jre\`) e os scripts do ícone de bandeja — não precisa mexer nisso. Os dois arquivos que mudam a cada versão — o `.jar` do sincronizador e o `configurar-usuario.ps1` — sempre vêm de dentro de "versão atual" e são colocados por cima dessa base, sobrescrevendo o que já estiver lá.

> ⚠️ Isso vale para instalação **nova**. Para atualizar uma máquina que já tem o Sincronizador rodando, ver o passo "Atualizar o pacote" em [[09 - Vincular cada máquina a um usuário]].

O pacote já vem com o Java embutido — não é preciso instalar Java na máquina do cliente separadamente.

Vídeo (teste): https://youtu.be/Xc_ehR1XMdI

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas ao baixar ou montar os arquivos de instalação do Sincronizador. -->

## Relacionados

- [[Sincronizador Docnuvem]]
- Anterior: [[03 - Antes de instalar (ativar o módulo na empresa)]] · Próxima etapa: [[05 - Configurar o application.yml]]
