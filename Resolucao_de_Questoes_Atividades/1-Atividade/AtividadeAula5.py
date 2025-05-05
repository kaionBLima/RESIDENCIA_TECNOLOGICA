import pandas as pd
# Questao 1:
# serie = pd.Series([5, 10, 15, 20], index = ['a', 'b', 'c', 'd'])
# print(serie)

# Questao 2:
# serie = pd.Series([100, 200, 300], index = ['x', 'y', 'z'])
# print(serie)

# Questao 3:
dict = {
    'Produto' : ['Maçã', 'Laranja', 'Lapis'],
    'Preco' : [10.50, 8.00, 1.98],
    'Estoque' : [100, 200, 300]
}

df = pd.DataFrame(dict)
print(df, "\n\n")

# Questao 4:
# print(df['Produto'])

# Questao 5:
# print(df[['Produto', 'Estoque']])

# Questao 6:
# print("Primeira linha do Dataframe: \n", df.iloc[0])

# Questao 7:
# print(f"Segunda linha: \n {df.iloc[1]}")

# Questao 8:
# filter = df[df['Preco'] > 2]
# print(filter)

# Questao 9:
df['Loja'] = ['LojaA', 'LojaB', 'LojaC']
# agrupam = df.groupby('Loja')['Estoque'].sum()
# print(agrupam)

# Questao 10:
df['Valor_total'] = df['Estoque'] * df['Preco']
print(df)