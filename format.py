from dataset import df
import pandas 

def format_number(value, prefix=''):  # Converte os dados maiores que mil para notação científica
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

# 1. Receita por estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# 2. Dataframe Receita mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pandas.Grouper(freq='ME'))['Preço'].sum().reset_index()
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
#print(df_rec_mensal)

# 3. Receita por categoria

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
print(df_rec_categoria.head(5))

# 4. Dataframe dos vendedores

df_vendedores = pandas.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
print(df_vendedores)