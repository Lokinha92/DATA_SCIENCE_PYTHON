import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, skewnorm
import seaborn as sns

dadosNormais = norm.rvs(size=1000)

# Verificando normalidade através do histograma
histograma = sns.distplot(dadosNormais, hist=True, kde=True, bins=20, color='blue', hist_kws={'edgecolor': 'black'})

# QQ PLOT
fig, ax = plt.subplots()
stats.probplot(dadosNormais, fit=True, plot=ax)
plt.show()

# Teste de shapiro
shapiro = stats.shapiro(dadosNormais)

for i in shapiro:
    valores = [i]

for i in valores:
    if i <= 0.05:
        print("NÃO ESTÁ NORMALMENTE DISTRIBUÍDO")
    else:
        print("NORMALMENTE DISTRIBUIDO")

# DADOS NÃO NORMAIS

dadosNnormais = skewnorm.rvs(4, size=1000)

#Histograma
histograma2 = sns.distplot(dadosNnormais, hist=True, kde=True, bins=20, color='blue', hist_kws={'edgecolor': 'black'})

# QQ plot
fig1, ax1 = plt.subplots()
stats.probplot(dadosNnormais, fit=True, plot=ax1)
plt.show()

# TESTE DE SHAPIRO

shapiro2 = stats.shapiro(dadosNnormais)

for v in shapiro2:
    pvalue = [v]

for v in pvalue:
    if v <= 0.05:
        print("NÃO ESTÁ NORMALMENTE DISTRIBUIDO")
    else:
        print("NORMALMENTE DISTRIBUIDO")
