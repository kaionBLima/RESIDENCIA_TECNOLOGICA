import pandas as pd

df = pd.read_csv('movies.csv')

def receita(revenue):
    if revenue > 1000000:
        return 'Sim'
    else:
        return 'Não'
    
df['sucesso'] = df['revenue'].apply(receita)

print(df[['title', 'revenue','sucesso']])