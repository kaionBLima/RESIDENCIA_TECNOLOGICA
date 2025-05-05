import pandas as pd 
 

# Ex.4

df = pd.read_csv('movies.csv')
# def receita(revenue):
#     if revenue > 100000000:
#         return 'Sim'
#     else:
#         return 'Não'

# print(df[['title', 'revenue','sucesso']])

# Ex.5
# df_media = df.groupby('year')['vote_average'].mean().reset_index(name='Nota_Media')

# df_MaiorMed = df_media.max()
# print("\n\n", df_MaiorMed.head())

# df_imp = df.groupby('year').agg(
#     NumFilmes = ('title', 'count'),
#     nota_media=('vote_average', 'mean')
# )
# print("\n\n", df_imp.head())

dfDiretores = pd.read_csv("directors.csv")
dfDiretores.rename(columns={"id": "director_id"}, inplace = True)

df_merged = pd.merge(
    df,
    dfDiretores,
    on = "director_id",
    how='left'
)

filtro = df_merged.groupby("director_name")["revenue"].sum().reset_index()

print(filtro.sort_values("revenue", ascending = False).head(5).reset_index(drop = True))
