import pandas as pd

dados1 = pd.read_csv('dados.cvs')
dados1.head(10)

colum_name = dados1['nome']

dropColum = dados1.drop(columns='error404')
dados1.head()

filterYear = dados1['idade'] > 25
OrderSalary = dados1.sort_values(by=['salario'], ascending=[True])
dados1.head()

dados1['cidade'].fillna("Desconhecido", inplace=True)

dados1['dobro_idade'] = dados1['idade'] * 2

dados1_grouped = dados1.groupby(['departamento', 'salario']).agg({
    'Media' : ['mean']
})




