import pandas as pd

dados1 = pd.read_csv('dados.csv')
dados2 = pd.read_csv('dados2.csv')
dados1.head(10)

colum_name = dados1['nome']

dropColum = dados1.drop(columns='error404')
dados1.head()

filterYear = dados1[dados1['idade'] > 25]

OrderSalary = dados1.sort_values(by=['salario'], ascending=[True])

dados1['cidade'] = dados1['cidade'].fillna("Desconhecido")

dados1['dobro_idade'] = dados1['idade'] * 2

dados1_grouped = dados1.groupby(['departamento']).agg({
    'salario' : ['mean']
})

resetIndice = dados1.reset_index()

filterA = dados1[dados1['nome'].str.startswith('A')]

dados1_duplicate = dados1.drop_duplicates('nome')

dados3 = pd.concat([dados1, dados2], ignore_index=False)

df_merged = pd.merge(
    dados1,
    dados2,
    on=['id'],
    how='inner'
)
df_merged.head()

dados1_EstUnicos = dados1['estado'].unique()












