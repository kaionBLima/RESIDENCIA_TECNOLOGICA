import pandas as pd 
 
# Ex.4
df = pd.read_csv('movies.csv')

# def receita(revenue):
#     if revenue > 1000000:
#         return 'Sim'
#     else:
#         return 'Não'
    
# df['sucesso'] = df['revenue'].apply(receita)

# print(df[['title', 'revenue','sucesso']])

# Ex.5

df_media = df.groupby('year')['vote_average'].mean().reset_index(name='Nota_Media')
print(df_media.head())

df_MaiorMed = df_media.max()
print("\n\n", df_MaiorMed.head())

df_imp = df.groupby('year').agg(
    NumFilmes = ('title', 'count'),
    nota_media=('vote_average', 'mean')
)

print("\n\n", df_imp.head())