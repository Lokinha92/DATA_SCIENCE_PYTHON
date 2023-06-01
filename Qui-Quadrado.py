import numpy as np
from scipy.stats import chi2_contingency

# REPRODUZINDO UMA TABELA DE EXEMPLO
array = np.array([[30, 45], [17, 8]])


# REALIZANDO O TESTE

teste = chi2_contingency(array)

pvalue = teste[1]

if pvalue >= 0.05:
    print("NÃO HÁ DIFERENÇA SIGNIFICATIVA, HIPÓTESE NULA COMPROVADA")
else:
    print("HIPÓTESE NULA DISCARTADA!, HÁ DIFERENÇA SIGNIFICATIVA")

