"""
 O intuito deste programa é manipular um arquivo json com os comando de sua biblioteca e depois formatar sua estrutura via 
pandas
"""


import streamlit as st
import json # Biblioteca para usar as funções de manipular os arquivos .json
import pandas # Biblioteca que permite organizar como linhas e colunas
st.title('Dataset de Vendas')

file = open('vendas.json')
dados = json.load(file)
# print(dados)

df = pandas.DataFrame.from_dict(dados)
tf = pandas.DataFrame.from_records(dados)

#print(df)

df['Data da Compra'] = pandas.to_datetime(df['Data da Compra'], format ='%d/%m/%Y')
print(df['Data da Compra'])

file.close()
