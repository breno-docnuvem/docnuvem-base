# 06 - Instalar como serviço do Windows

## Quando se aplica

Depois de configurado o `default.properties` (ver [04 - Configurar o default.properties](04-configurar-o-default-properties.md)), quando o Agente precisa rodar **sem depender de um usuário Windows logado** — por exemplo, em um servidor (caso RAMARIM, ver [02 - Quando instalar o Agente Docnuvem](02-quando-instalar-o-agente-docnuvem.md)). Para rodar como programa convencional, ver [05 - Rodar como programa convencional](05-rodar-como-programa-convencional.md) em vez desta.

## Passo a passo

1. Verificar se o sistema do cliente é de 32 bits (x86) ou 64 bits (x64) nas informações do sistema.

    ![Informações do sistema no Windows.](images/06-instalar-como-servico-do-windows/01-informacoes-do-sistema.png)
    ![Campo com o tipo do sistema (32 ou 64 bits).](images/06-instalar-como-servico-do-windows/02-tipo-do-sistema.png)

2. Dentro da pasta do Agente, acessar a subpasta do NSSM correspondente à versão do sistema:
    - 32 bits (x86): `agente-docnuvem\nssm-2.24\win32`
    - 64 bits (x64): `agente-docnuvem\nssm-2.24\win64`

3. Clicar com o botão direito nessa pasta e escolher "Abrir no terminal".

    ![Opção "Abrir no terminal" no menu de contexto da pasta.](images/06-instalar-como-servico-do-windows/03-abrir-no-terminal.png)

4. No terminal, executar o comando:

    ```
    .\nssm.exe install agente-docnuvem
    ```

    ![Comando nssm.exe install agente-docnuvem executado no terminal.](images/06-instalar-como-servico-do-windows/04-comando-nssm-install.png)

5. Na janela do instalador do NSSM ("Service name" já vem preenchido como `agente-docnuvem`), na aba **Application**, preencher o campo **Path** com o caminho até `agente-docnuvem\bin\docnuvem-agente.bat`.

    ![Aba Application do instalador NSSM com o campo Path preenchido.](images/06-instalar-como-servico-do-windows/05-aba-application-path.png)

6. Na aba **I/O**, redirecionar a saída (**Output (stdout)**) e os erros (**Error (stderr)**) para arquivos de log dentro da pasta do agente (ex.: `agente-docnuvem\logs\...`).

    ![Aba I/O do instalador NSSM com os campos de log.](images/06-instalar-como-servico-do-windows/06-aba-io-logs.png)

    !!! warning "Pendente"
        Confirmar com Breno o caminho exato usado nos campos Output/Error (a captura de tela está cortada) e se há mais alguma aba do NSSM que precise ser configurada além de Application e I/O.

7. Clicar em "Install service" para concluir a instalação e, no Gerenciador de Tarefas (aba Serviços), iniciar o serviço clicando com o botão direito nele.

    ![Iniciando o serviço pelo Gerenciador de Tarefas.](images/06-instalar-como-servico-do-windows/07-iniciar-servico.png)

Se todos os passos forem seguidos corretamente, o serviço deve ficar em execução.

**Vídeo**

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/0Ch2igptWNA" title="Instalar o Agente Docnuvem como serviço do Windows" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para problemas ao instalar o Agente como serviço do Windows. -->

## Relacionados

- [Agente Docnuvem (robô)](index.md)
- Anterior: [04 - Configurar o default.properties](04-configurar-o-default-properties.md)
