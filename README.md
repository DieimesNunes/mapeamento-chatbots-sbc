# Mapeamento de Chatbots na SBC OpenLib

Repositório de apoio à pesquisa sobre chatbots, Inteligência Artificial e ensino de programação, desenvolvida no contexto do mestrado.

## Objetivo

Este repositório reúne os dados, scripts e documentos utilizados durante a investigação de chatbots e ferramentas relacionadas à educação e ao ensino de programação presentes na literatura da SBC OpenLib.

A estratégia de busca e o recorte da pesquisa ainda estão em processo de definição e refinamento.

## Ferramenta de coleta

A coleta de registros na SBC OpenLib foi realizada com o
[pySol](https://gitlab.com/nszchagas/pySol), ferramenta de terceiros destinada à automação de buscas na SBC OpenLib.

O código-fonte original do pySol não faz parte deste repositório.

Durante a execução foram necessárias adaptações locais no pySol para tratamento de codificação UTF-8 e aumento do tempo limite das requisições. Essas alterações serão documentadas separadamente.

## Busca exploratória

Em 15/09/2026 foi realizada uma busca exploratória na SBC OpenLib.

Parâmetros utilizados:

- Termo: `chatbot`
- Campo: `query`
- Tipo de publicação: `anais`
- Ferramenta: pySol

Comando utilizado:

```powershell
python pySol --query_string "chatbot" --field query --publication_type anais --bib_dest chatbot_anais.bib