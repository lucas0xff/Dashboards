#streamlit run app.py

import streamlit as st
import plotly.express as px
from dataset import df 
from format import format_number
from graficos import grafico_mapa_estado, grafico_rec_mensal

st.title("Dashboard de teste do primeiro programa")

p_one, p_two, p_tree = st.tabs(['dataset', 'receita', 'vendedores']) # Esse comando define a criação de 3 abas

# ---------------------------------------------------------------------------------------
with p_one: # Esse comando define o que conterá na página 1
    st.dataframe(df)
# ---------------------------------------------------------------------------------------
with p_two:
    column_one, column_two = st.columns(2)

    with column_one:
        st.metric('Faturamento Total',format_number(df['Preço'].sum(), 'R$') )
        
        st.plotly_chart(grafico_mapa_estado, use_container_width = True)

    with column_two:
        st.metric('Total de vendas',format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)

