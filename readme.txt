Como a aplicação funciona:

Arquivo dataset.py

Abre o arquivo json > Carrega os dados > Trata como matriz/planilha > exporta eles como variável.
1. Possuindo o arquivo .json que contém todas as nossas informações, precisamos manipulalo, carregamos usando a lib json e o método json.load
2. Utilizando a biblioteca pandas, usamos o método dataframe.fromdict para criar uma variável que organize eesse json que estava em um array/dicionário em 
formato de matriz com linhas e colunas correspondentes. Pois ele entende que as keys são a primeira linha, e a lista de value de cada key são os valores daquela coluna.

2. O Arquivo Format é responsável por utilizar a biblioteca do pandas e do streamlit para criar novos dataframes menores que contenham informações chaves 
para os insights da aplicação, ou seja separam alguns dados e podem criar novos dados a partir destes dados para criar um novo dataframe. Neste arquivo também está o salvamento em csv 
do arquivo dataframe, podendo baixar a planilha como for desejado.

3. O arquivo graficos.py recebe esses dataframes tratados e criar graficos com a biblioteca do plotly express.

4. O arquivo app.py que é a página principal apenas recebe o apanhado de insights de graficos para construir seu layout usando os comandos do streamlit
Assim ele organiza a criação de abas e páginas dentros dessas abas e com os comandos de colunas da pagina vai posiciando os graficos que serao exibidos

5. A outra pagina principal é o dataframe.py nela estão contidos as barras laterais de filtragem bem como a opção de baixar o csv que ela impoorta do format.py.


