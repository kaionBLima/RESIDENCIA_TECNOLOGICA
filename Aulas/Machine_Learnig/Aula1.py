from faker import Faker
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

fake = Faker('pt_BR')

def criar_dados_alunos(n_alunos = 100):
    dados = []
    for _ in range(n_alunos):
        dados.append({
            'nome' : fake.name(),
            'idade' : fake.random_int(min = 18, max = 120),
            'nota' : fake.random_int(min = 0, max = 10),
            'curso' : fake.random_element(['Engenharia', 'Medicina', 'Direito', 'Administração'])
        })
    return pd.DataFrame(dados) 

df_alunos = criar_dados_alunos(50)
print('=== Exemplo de Dataframe ===')
print(df_alunos.tail())

#################################################################
# Trabalhando com graficos:

plt.figure(figsize=(10, 6)) # Tamanho padrao de grafico (10, 6) 10 por 6
plt.hist(df_alunos['idade'], bins= 10, color='skyblue' , edgecolor = 'black') #Grafico Histograma
plt.title('Distribuição de idades dos alunos')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True, alpha = 0.3)
plt.show()
