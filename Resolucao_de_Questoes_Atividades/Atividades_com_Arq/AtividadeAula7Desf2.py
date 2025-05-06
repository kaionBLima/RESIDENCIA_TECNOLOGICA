import pandas as pd
df = pd.read_csv('movies.csv')
# Questao 1:

def receita(revenue):
    if revenue > 100000000:
        return 'Sim'
    else:
        return 'Nao'
    
df['Sucesso'] = df['revenue'].apply(receita)
# print(df)

# Questao 2:
df_filter = df.groupby('year').agg(
    num_Media = ('title', 'count'),
    media = ('vote_average', 'mean')
)

# print(df_filter)

# Questao 3:

dfDirect = pd.read_csv('directors.csv')

dfDirect.rename(columns={'id' : 'director_id'}, inplace = True)
df_merge = pd.merge(
    df,
    dfDirect,
    on = 'director_id',
    how= 'left'
)

df_filter = df_merge.groupby('director_name')['revenue'].sum().reset_index()
print(df_filter.sort_values('revenue', ascending=False).head(5).reset_index(drop= True))