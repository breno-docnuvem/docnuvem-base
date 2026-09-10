---
tipo: processo
area: suporte
etapa: "4.1"
status: publicado
ultima_revisao: 2026-09-10
---

# 05 - Rodar como programa convencional

## Quando se aplica

Depois de configurado o `default.properties` (ver [[04 - Configurar o default.properties]]), quando o Agente vai rodar como **programa convencional** — ou seja, só enquanto o usuário Windows responsável estiver logado (ver [[01 - O que é o Agente Docnuvem]]). Para rodar como serviço do Windows, ver [[06 - Instalar como serviço do Windows]] em vez desta nota.

A pasta `agente-docnuvem\bin` contém os arquivos usados nesta etapa:

![[Base de Conhecimento Interna/images/suporte/agente-docnuvem/05-rodar-como-programa-convencional/03-conteudo-pasta-bin.png]]

## Com log na tela (útil para testes)

Executar o arquivo `agente-docnuvem\bin\docnuvem-agente.bat`.

![[Base de Conhecimento Interna/images/suporte/agente-docnuvem/05-rodar-como-programa-convencional/01-executar-bat-log.png]]

Se as configurações foram feitas corretamente, o prompt abre e mostra a mensagem "Propriedades carregadas com sucesso!". Ao colocar um arquivo na pasta monitorada, o log deve mostrar que o envio foi feito com sucesso.

![[Base de Conhecimento Interna/images/suporte/agente-docnuvem/05-rodar-como-programa-convencional/02-log-envio-sucesso.png]]

> ⚠️ **Ao fechar o prompt, o programa deixa de funcionar.** Ele precisa permanecer aberto — pode ser minimizado, mas não fechado.

## Em segundo plano (uso do dia a dia)

Para abrir o programa sem que o log apareça na tela, executar o script `agente-docnuvem\bin\iniciar_agente_docnuvem.vbs`. A única evidência de que o programa está em execução é o ícone na bandeja do Windows.

![[Base de Conhecimento Interna/images/suporte/agente-docnuvem/05-rodar-como-programa-convencional/04-icone-bandeja.png]]

Para finalizar o programa, clicar com o botão direito no ícone da bandeja e escolher "Encerrar".

![[Base de Conhecimento Interna/images/suporte/agente-docnuvem/05-rodar-como-programa-convencional/05-encerrar-pelo-icone.png]]

## Iniciar junto com o Windows

Para o Agente iniciar sozinho sempre que o Windows for ligado, sem precisar executar o `.vbs` manualmente:

1. Criar um atalho do arquivo `agente-docnuvem\bin\iniciar_agente_docnuvem.vbs` (botão direito sobre o arquivo → **Criar atalho**).
2. Abrir a pasta de inicialização do Windows: `Win + R`, digitar `shell:startup` e pressionar Enter.
3. Copiar o atalho criado para dentro dessa pasta.

A partir daí, a cada login do usuário Windows responsável, o Agente inicia sozinho em segundo plano — o mesmo comportamento de quando se executa o `.vbs` manualmente (ícone na bandeja, sem log na tela).

> Isso só vale para o modo **programa convencional** (depende do usuário estar logado). Para não depender de usuário logado, ver [[06 - Instalar como serviço do Windows]].

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas ao rodar o Agente como programa convencional. -->

## Relacionados

- [[Agente Docnuvem (robô)]]
- Anterior: [[04 - Configurar o default.properties]]
