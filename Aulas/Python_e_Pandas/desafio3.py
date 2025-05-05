import pandas as pd

df = pd.read_csv('movies.csv')
dfDiretores = pd.read_csv('directors.csv')
dfDiretores.rename(columns={"id": "director_id"}, inplace=True)

df_merged = pd.merge(
    df, 
    dfDiretores, 
    on="director_id", 
    how='inner'
)

# df_merged['lucro'] = df_merged['revenue'] - df_merged['budget']
# print(df_merged.head())

# filtroLucro = df_merged.groupby('director_id')['lucro'].sum().reset_index()

# filtroMedia = filtroLucro.groupby('director_name').agg(
#     n_filmes=('titile', 'count'),
#     lucro_medio = ('lucro', 'mean'),
#     desvio_padrao = ('vote_avarage', 'std')
# ).reset_index

# filtro = df_merged[(df_merged['n_filmes'] >= 3) &
#                    (df_merged['lucro_medio'])]

