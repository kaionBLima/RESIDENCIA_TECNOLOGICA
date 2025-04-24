import pandas as pd

df = pd.read_csv("./vendas.csv")

print(df)

df_vendas = pd.read_csv('vendas.csv')

print("\n\n", df_vendas.head())
print("\n\n", df_vendas['Total_Vendas'])

vendas_2023 = df_vendas[df_vendas['Ano'] == 2023]
total_vendas_2023 = vendas_2023['Total_Vendas'].sum()
print("Total de vendas em 2023:", total_vendas_2023)