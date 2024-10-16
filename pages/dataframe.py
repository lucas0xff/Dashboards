import streamlit as st
from dataset import df
from format import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
)
with st.sidebar.expander('Categorias do Produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
)
    
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
        0, 5000,
        (0, 5000)
)

with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),
         df['Data da Compra'].max())
)
    
query = f'`Categoria do Produto` in @categorias and {preco[0]} <= Preço <= {preco[1]} and @data_compra[0] <= `Data da Compra` <= @data_compra[1]'

# Aplica o filtro
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] Colunas')

st.dataframe(filtro_dados)

st.markdown('Escreva um nome para o arquivo')

coluna1,coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_arquivo +='.csv'
with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click= mensagem_sucesso
    )