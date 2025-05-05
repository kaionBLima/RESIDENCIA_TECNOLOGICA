import pandas as pd

df= pd.read_csv('directors.csv')

dfHead = df.head()
print(dfHead)
dfInf = df.info()
print("\n\n", dfInf)
dfDesc = df.describe()
print("\n\n", dfDesc)
dfTyp = df.dtypes

indice = df[df['gender'] == 'Male']
print("\n\n", indice)

df.to_csv('Arq2Gerado.csv', index=False)

# df.info()
# df.describe()
# df['media_final'] = df['media_final'].astype(str)
# df.dtypes()




