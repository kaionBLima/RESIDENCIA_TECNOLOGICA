import pandas as pd
# Questao 1:
df = pd.read_csv('dados.csv')
# print(df.head(10))

# Questao 2:
# print(df['nome'])

# Questao 3:
df.drop(columns=['error404'], inplace=True)
# print(df)

# Questao 4:
# filter = df[df['idade'] > 25]
# print(filter)

# Questao 5:
# df = df.sort_values(by=['salario'], ascending=False)
# print(df)

# Questao 6:
df['cidade'].fillna('Desconhecido')
# print(df)

# Questao 7:
df['Dobro_idade'] = df['idade'] * 2
# print(df)

# Questao 8:
dfMediaSal = df.groupby('departamento')['salario'].mean()
# print(dfMediaSal)

# Questao 9:
# df.reset_index()
# print(df)

# Questao 10:
# filter = df[df['nome'].str.startswith('A')]
# print(filter)