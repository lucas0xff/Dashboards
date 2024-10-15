import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Análise de Vendas")

# Carregando um conjunto de dados fictício
data = {
    "Produto": ["Produto A", "Produto B", "Produto C", "Produto D"],
    "Vendedores": [10, 15, 7, 20],
    "Receita": [200, 300, 150, 400]
}

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Exibindo as primeiras linhas do DataFrame
st.subheader("Primeiras linhas dos dados")
st.write(df)

# Exibindo estatísticas descritivas
st.subheader("Estatísticas Descritivas")
st.write(df.describe())

# Gráfico de barras da receita
st.subheader("Gráfico de Receita por Produto")
st.bar_chart(df.set_index("Produto")["Receita"])



# Opção para visualizar dados filtrados
st.subheader("Filtrar Dados")
produto_selecionado = st.selectbox("Selecione um Produto", df["Produto"])
dados_filtrados = df[df["Produto"] == produto_selecionado]

st.write("Dados filtrados para o produto selecionado:")
st.write(dados_filtrados)
