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

# Questao 11:
# print(df['nome'].duplicated())

# Questao 12:
df2 = pd.read_csv('dados2.csv')
# df_concat = pd.concat([df, df2], ignore_index=False)
# print(df_concat)

# Questao 13:
df_merger = pd.merge(
    df, 
    df2, 
    on=['id'],
    how='inner'
)
# print(df_merger)

# Questao 14:
dfcont = df['estado'].unique()
# print(dfcont)

# Questao 15:
def faixa_etaria(idade):
    if idade <= 18:
        return 'jovem'
    elif idade < 45:
        return 'adulto'
    else: 
        return 'idoso'
    
df['Faixa-etaria'] = df['idade'].apply(faixa_etaria)
print(df)

# Questao 16:
df = df.drop_duplicates(subset=['email', 'telefone'])
print(df)

