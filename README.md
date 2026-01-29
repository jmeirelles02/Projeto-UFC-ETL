# Pipeline de Dados Históricos do UFC

## Sobre o Projeto

Este projeto nasceu da curiosidade de unir duas paixões: a análise de dados e o MMA. O objetivo principal não foi apenas recolher estatísticas, mas sim construir um pipeline de ETL completo capaz de transformar informações brutas da web em um banco de dados estruturado e pronto para análises complexas.

Ao desenvolver esta ferramenta, foquei-me em criar um processo resiliente que capturasse a totalidade da história do UFC, desde o UFC 2 até o UFC 324, garantindo a integridade de dados cruciais como tempos de luta, categorias de peso e disputas de título.

## O Desafio de Engenharia

Durante o desenvolvimento, encontrei um desafio técnico que define a natureza deste projeto. Ao tentar extrair quais lutas valiam o cinturão, percebi que o dado sobre o cinturão não estava em texto.

Após uma investigação minuciosa da estrutura HTML e diagnósticos de falha, descobri que a informação estava "escondida" visualmente através de um ícone (imagem) de um cinturão. Para resolver isso, implementei uma lógica de extração que inspeciona não apenas o texto, mas os atributos das imagens dentro da tabela, permitindo identificar com precisão as 475 disputas de cinturão que ocorreram na história da organização.

## Como Funciona a Arquitetura (ETL)

O projeto segue o padrão clássico de pipeline de dados:

### 1. Extração (Extract)
Utilizando Python e a biblioteca BeautifulSoup, o script simula um navegador para percorrer o histórico de eventos. Ele captura metadados de cada evento (data, local) e navega para cada luta individualmente para extrair estatísticas granulares.

### 2. Transformação (Transform)
Os dados brutos chegam com muitas inconsistências (datas em texto, durações em minutos/segundos, nomes de categorias com formatação variada). A etapa de transformação, feita com Pandas, normaliza estes dados. Um destaque é a conversão de tempos para segundos totais e a limpeza das categorias de peso, mantendo a integridade da informação original.

### 3. Carga (Load)
Por fim, os dados limpos não são apenas deixados num arquivo de texto. Eles são modelados e carregados num banco de dados relacional (SQLite), simulando um ambiente de produção real.

## Stacks do Projeto

* Linguagem: Python
* Coleta de Dados: Requests e BeautifulSoup4
* Processamento: Pandas
* Banco de Dados: SQLite (SQL)

## Estrutura do Repositório

* /src - Contém os códigos fonte para cada etapa do pipeline.
* /data - Armazena os arquivos CSV gerados e o banco de dados final.
* requirements.txt - Lista de dependências do projeto.

## Como Executar o Projeto localmente

Para reproduzir este pipeline na sua máquina, siga os passos abaixo:

1. Clone este repositório.
2. Instale as bibliotecas necessárias listadas no arquivo requirements.txt.
3. Execute os scripts na ordem lógica do pipeline:
    * Primeiro, a extração dos eventos.
    * Segundo, a extração detalhada das lutas (este processo pode levar alguns minutos devido ao volume de dados).
    * Terceiro, a transformação e limpeza.
    * Por fim, a carga no banco de dados.

## Autor

Desenvolvido por *João Gabriel Guedes* como parte de um portfólio de Engenharia de Dados, demonstrando habilidades em Web Scraping, limpeza de dados e modelagem SQL.
