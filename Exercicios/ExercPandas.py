import pandas as pd

# series_numbers = pd.Series([5, 10, 15, 20])
# print(series_numbers)

# series_numbers = pd.Series([100, 200, 300, 400], index=['x', 'y', 'z', 'w'])
# print(series_numbers)

dataFrame = {
    'Produto': ['Caderno', 'Lápis', 'Caneta'],
    'Preço': [10, 2, 4],
    'Estoque': [100, 200, 150]
}

df = pd.DataFrame((dataFrame), index=['Prod1', 'Prod2', 'Prod3'])
#print(df)
#indice = df[['Produto']]

indice = df[['Produto','Estoque']]
print(indice)
print("\n\n", df.iloc[0])
print("\n", df.iloc[1])

indice2 = df[df['Preço'] > 2]
print("\n", indice2)

df['Loja'] = ['Loja A', 'Loja B', 'Loja A']
groupBy = df.groupby('Loja')['Estoque'].sum()
print("\n\n Soma do Estoque, adição de loja e agrupamento: \n", groupBy)

df['Valor_Total'] = df['Preço'] *df['Estoque']
print("\n\n", df)