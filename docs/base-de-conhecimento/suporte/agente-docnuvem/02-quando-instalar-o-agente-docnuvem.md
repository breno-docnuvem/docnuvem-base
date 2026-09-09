# 02 - Quando instalar o Agente Docnuvem

## Quando se aplica

Sempre que estiver avaliando se um cliente (novo ou existente) precisa do Agente instalado, em vez do Sincronizador.

## 1. Envio de grande volume de arquivos (backup inicial)

O Docnuvem Web tem limitação na quantidade de arquivos que podem ser enviados de uma vez, o que costuma gerar erros em envios grandes — situação comum em clientes novos que precisam subir um backup extenso antes de começar a usar o sistema. Nesses casos, o Agente pode ser instalado temporariamente para fazer esse envio.

Procedimento:

- Após a instalação, acompanhar o envio até confirmar que todos os arquivos foram enviados com sucesso.
- Desinstalar o Agente da máquina do cliente ao final — o módulo é um adicional e deve ser usado apenas para esse backup pontual, não para uso contínuo.
- Se o cliente não responder para agendar a instalação, revogar o token.

## 2. Envio direto para o Envio Inteligente

O Sincronizador não tem uma função que envie arquivos diretamente para o Envio Inteligente. Quando o cliente precisa desse fluxo, o Agente deve ser instalado.

Clientes que utilizam o Agente dessa forma: CAPOL, COOPERPRATA e RAMARIM.

## 3. Detalhe do caso RAMARIM

Na RAMARIM (um dos clientes do caso 2, acima), o Agente fica instalado no servidor enviando arquivos diretamente para o Envio Inteligente. Nesse cliente, ele deve ficar instalado **exclusivamente como serviço do Windows**, pois nem sempre há um usuário Windows logado no servidor — e isso não pode interferir no envio dos arquivos.

## Se travar

<!-- TODO: confirmar com Breno qual é o canal/responsável de escalonamento para dúvidas sobre quando instalar o Agente Docnuvem. -->

## Relacionados

- [Agente Docnuvem (robô)](index.md)
- Anterior: [01 - O que é o Agente Docnuvem](01-o-que-e-o-agente-docnuvem.md) · Próxima etapa: [03 - Baixar e alocar os arquivos](03-baixar-e-alocar-os-arquivos.md)
- Veja também no Manual do Sistema: [Arquivos — Como configurar regras de Envio Inteligente](../../../manual/10-arquivos.md#como-configurar-regras-de-envio-inteligente)
