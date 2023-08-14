# C-Means é parecido com K-Means, porem, não vai atribuir uma instancia de forma absoluta a um cluster. O c-means faz uma atribuição de forma percentual
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

iris = datasets.load_iris()

# iris.data.T -> matriz transposta, c=3 é a definição dos clusters, ou seja, quantos registros unicos tem a classe. Os outros parametros são padrão indicados pela documentação
r = skfuzzy.cmeans(data=iris.data.T, c=3, m = 2, error= 0.005, maxiter= 1000, init= None)

agrupamento_porcentagem = r[1] # A posição 1 do objeto contendo o C-Means contém a porcentagem de um registro pertencer a um cluster

# visualização da probabilidade

for x in range(150):
    print(agrupamento_porcentagem[0][x], agrupamento_porcentagem[1][x], agrupamento_porcentagem[2][x]) # cada parametro, é o quão associado o registro está ao cluster
    
associacoes = agrupamento_porcentagem.argmax(axis=0)
resultados = confusion_matrix(iris.target, associacoes)

print("\n\n", resultados)