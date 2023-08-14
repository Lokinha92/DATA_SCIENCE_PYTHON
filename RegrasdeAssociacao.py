# Associadores
import pandas as pd
from apyori import apriori

dados = pd.read_csv("./DADOS/transacoes.txt", header= None)

# transformação pro formato de lista (apriori exige assim) - 6 é a quantidade de itens no dataset

transacoes = []

for i in range(0,6):
    transacoes.append([str(dados.values[i, j]) for j in range(0,3)])
    
# apriori para gerar as regras de associacao

regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5, min_length = 2)

# armazenando as regras
resultados = list(regras)

#print(resultados[0]) # -> fica mt complex0

# visualização: percorre os resultados para melhor visualiza-lo

resultados2 = [list(x) for x in resultados]

#print(resultados2) # melhor, mas ainda nao ideal

# criação de outra variavel para melhor visualização das regras

result_final = []

for j in range (0,7):
    result_final.append(list(x) for x in resultados2[j][2])

print(result_final)