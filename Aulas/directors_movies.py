import pandas as pd 
 
# df = pd.read_csv('movies.csv')

# Ex.4
# def receita(revenue):
#     if revenue > 1000000:
#         return 'Sim'
#     else:
#         return 'Não'
    
# df['sucesso'] = df['revenue'].apply(receita)

# print(df[['title', 'revenue','sucesso']])

# Ex.5
# df_media = df.groupby('year')['vote_average'].mean().reset_index(name='Nota_Media')
# print(df_media.head())

# df_MaiorMed = df_media.max()
# print("\n\n", df_MaiorMed.head())

# df_imp = df.groupby('year').agg(
#     NumFilmes = ('title', 'count'),
#     nota_media=('vote_average', 'mean')
# )

# print("\n\n", df_imp.head())

df_left = pd.read_csv('movies.csv')
df_right = pd.read_csv('directors.csv')

df_merged = pd.merge(
    df_left,
    df_right,
    left_on='director_id',
    right_on='id',
    how='inner'
)

df_Fat = df_merged.groupby('director_name')['revenue'].max().reset_index(name='Ranking')
df_ranking = df_Fat.sort_values(by='Ranking', ascending=False).reset_index(drop=True)


print(df_ranking.head(5))


print(df_merged.head())