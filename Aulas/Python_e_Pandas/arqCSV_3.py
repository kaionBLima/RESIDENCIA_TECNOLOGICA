import pandas as pd

#FILTRANDO FILMES DO ARQUIVO CSV

# filme = pd.read_csv('movies.csv')
# print("\n",filme.head())
# filme0 = filme.sort_values(by=['vote_average', 'title'], ascending=[False, True])
# print(filme0)
# filme1 = filme.sort_values(by=['popularity','title'], ascending=[False, True])
# primeiros_filmes = filme1[["title","popularity"]].head(10)
# primeiros_filmes.head()


dados = {
    'Nome': ['Malvezzi', 'Bomvezzi', 'Kaion'],
    'Nota1' : [5.6, 7.0, 8.0],
    'Nota2' : [6.0, 7.0, 8.0]
}

dados1 = {
    'Nome': ['Joao', 'Miguel', 'Bruno'],
    'Nota1' : [5.6, 7.0, 8.0],
    'Nota2' : [6.0, None, None]
}

df_concat = pd.concat(['dados', 'dados1'])

df_concat.head()

# df = pd.DataFrame(dados)
# df['Media'] = (df['Nota1'] + df['Nota2']) / 2

# print(df)
# df.info()
# df.describe()
# df.head()

