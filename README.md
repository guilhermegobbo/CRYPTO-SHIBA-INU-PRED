# Previsão de Preços da Criptomoeda Shiba Inu

## Visão Geral

Este projeto tem como objetivo prever os preços futuros da criptomoeda Shiba Inu com base em dados históricos. Ele é composto por três partes principais:

- Um modelo de previsão baseado no Prophet.
- Uma API em Flask que calcula as previsões do modelo.
- Uma página web interativa para visualizar os resultados das previsões.

## Uso

- Python version: 3.11.3
- Flask version: 2.3.3

Para usar este projeto, siga estas etapas:

1. **Iniciando a API**:

   Execute o arquivo `flask code.py` para iniciar a API Flask. A API estará disponível em `http://localhost:5000`. Você pode acessar os endpoints da API para obter previsões de preços da Shiba Inu.

2. **Executando a Página Web**:

   Abra o arquivo `html.html` em seu navegador para acessar a página web interativa. A página permite que você visualize os resultados das previsões em gráficos intuitivos.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

- `web page`: Arquivos da página web (HTMl, CSS, JavaScript).
- `api`: Pasta com a solicitação http de exemplo e o código Flask.
- `SHIB-USD.csv`: Contém os dados históricos da Shiba Inu.
- `model.pkl`: Modelo Prophet treinado.
- `notebook.ipynb`: Jupyter Notebook

## Layout da página web

![image](https://github.com/guilhermegobbo/Shiba-Inu-Prediction/assets/136920721/7d2f4521-798f-43bd-86b1-c1f33395ebcc)

