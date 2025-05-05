import pandas as pd

renda = pd.Series([10, 20, 30, 40])
print(type(renda))
print(renda)

#Criando uma Serie com poucos dados
series_rendaIndice = pd.Series(["Bloco 1", "Bloco 2", "Bloco 3"], index=['Med', 'TI', 'Agro'])
print(series_rendaIndice)

#Criando uma biblioteca com os dados que seram usados dentro do dataFrame
dados = {
    "Nome" : ["Kaion", "Bruno", "Pedro", "Thiago"],
    "Idade" : [20, 21, 23, 50],
    "Cidade" : ["Brasilia", "Candango", "Samamba", "Aguas-Lindas"]
}
print(dados)

#Organizando dados dentro de um dataframe/tabela
df = pd.DataFrame((dados), index=["Pessoa1", "Pessoa2", "Pessoa3", "Pessoa4"])
print(df)

#Imprimindo apenas o que desejo ver através das chaves de uma biblioteca
print("\n\n", df[['Nome', 'Idade']])

print("\n\n Linha 0")
print(df.iloc[0])
print("\n Linha 1", df.iloc[-1])
print("\n","----" * 20)

#----------------------------------------------------------------

pessoais = {
    "Nome" : ["Gilmar", "Kaion", "Carlos"],
    "Idade" : [23, 20, 18],
    "Altura" : [1.80, 1.75, 1.77],
    "Tem-Cachorro" : ["Sim", "Não", "Sim"]
}

dtfm = pd.DataFrame((pessoais), index=["#1", "#2", "#3"])
print("\n",dtfm)

#FILTRANDO DADOS
indice = dtfm[dtfm["Nome"] == "Gilmar"]
print("\n", indice)
