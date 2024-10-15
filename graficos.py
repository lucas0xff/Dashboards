import plotly.express as px
from format import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# Verifique se o DataFrame está carregado corretamente
print(df_rec_mensal.head())  # Confirmação básica dos dados
print(df_rec_mensal.columns) # Confirmação de colunas

grafico_mapa_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)
grafico_rec_mensal.update_layout(yaxis_title='Receita')

grafico_rec_estado = px.bar(

    df_rec_estado.head(10),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top receita por Estados'
)


grafico_rec_categoria = px.bar(

    df_rec_categoria.head(5),
    text_auto= True,
    title= 'Top 7 categorias com maior receita',
)

#grafico_vendedores = 