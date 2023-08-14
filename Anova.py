import pandas as pd
from scipy import stats
import statsmodels.api as st
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

dataset = pd.read_csv("./DADOS/anova.csv", sep= ";")
print(dataset.head())

# Agrupando os dados por Remedio num boxplot
agrupado = dataset.groupby(['Remedio']).describe()
print(agrupado)
boxplot = dataset.boxplot(by= "Remedio", grid= False)
print(boxplot)

# Criando modelo de regressao linear e testando

modelo1 = ols('Horas ~ Remedio', data=dataset).fit()
resultado1 = st.stats.anova_lm(modelo1)
print(resultado1)
pvalue = resultado1['PR(>F)'][0]
if pvalue >= 0.05:
    print("NÃO HÁ DIFERENÇA SIGNIFICATIVA")
else:
    print("HÁ DIFERENÇA SIGNIFICATIVA")

# ANOVA 2 FATORES

modelo2 = ols('Horas ~ Remedio * Sexo', data=dataset).fit()
resultado2 = st.stats.anova_lm(modelo2)
print(resultado2)

pvalue2 = resultado2['PR(>F)'][0]
if pvalue2 >= 0.05:
    print("NÃO HÁ DIFERENÇA SIGNIFICATIVA")
else:
    print("HÁ DIFERENÇA SIGNIFICATIVA")

# TESTE DE TURKEY

ttk = MultiComparison(dataset['Horas'], dataset['Remedio'])
resultadottk = ttk.tukeyhsd()
print(resultadottk)

grafico = resultadottk.plot_simultaneous()
print(grafico)