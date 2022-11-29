import pandas as pd

dataset = pd.read_csv('dados.csv', delimiter=';')
mostra = dataset.head()
shape = dataset.shape

print(mostra)
print(shape)

#LOCALIZANDO O VALOR DO MAIOR PIB NO BD
maior = dataset['PIB'].max()
idmaior = dataset['PIB'].idxmax()

print("\n", maior)
print(idmaior)

#MOSTRANDO AS INFORMAÇÔES DA CIDADE COM MAIOR PIB
muni = dataset.MUNICIPIO
pib = dataset.PIB
ve = dataset.VALOREMPENHO
cod = dataset.CODIGO

print("\nINFORMAÇÕES DA CIDADE COM MAIOR PIB: ")
print("CODIGO: ", cod[idmaior], "\nMUNICIPIO: ", muni[idmaior], "\nPIB: ", pib[idmaior], "\nVALOR EMPENHO:",
      ve[idmaior])
#----------------------------------------

#LOCALIZANDO O MENOR PIB NO BD
menor = dataset['PIB'].min()
idmenor = dataset['PIB'].idxmin()
print("\n", menor)
print(idmenor)

#MOSTRANDO AS INFOS DA CIDADE COM MENOR PIB:
print("\nINFORMAÇÕES DA CIDADE COM MENOR PIB: ")
print("CODIGO: ", cod[idmenor], "\nMUNICIPIO: ", muni[idmenor], "\nPIB: ", pib[idmenor], "\nVALOR EMPENHO:",
      ve[idmenor])

#MOSTRANDO A MÉDIA DO PIB ENTRE AS CIDADES
media = dataset['PIB'].mean()
print("\n A MÉDIA DO PIB ENTRE ESSAS CIDADES É:", media)

#------------------------------------------------- FIM PIB

# LOCALIZANDO O MAIOR E MENOR VALOR EMPENHO

vemaior = dataset['VALOREMPENHO'].max()
veIDmaior = dataset['VALOREMPENHO'].idxmax()

vemenor = dataset['VALOREMPENHO'].min()
veIDmenor = dataset['VALOREMPENHO'].idxmin()

print("\n", vemaior)
print(veIDmaior)

print("\n", vemenor)
print(veIDmenor)

# CIDADE COM MAIOR E MENOR VALOR EMPENHO

print("\nINFORMAÇÕES DA CIDADE COM MAIOR VALOR EMPENHO: ")
print("CODIGO: ", cod[veIDmaior], "\nMUNICIPIO: ", muni[veIDmaior], "\nPIB: ", pib[veIDmaior], "\nVALOR EMPENHO:",
      ve[veIDmaior])

print("\nINFORMAÇÕES DA CIDADE COM MENOR VALOR EMPENHO: ")
print("CODIGO: ", cod[veIDmenor], "\nMUNICIPIO: ", muni[veIDmenor], "\nPIB: ", pib[veIDmenor], "\nVALOR EMPENHO:",
      ve[veIDmenor])

# MOSTRANDO A MEDIA DO VALOR EMPENHO ENTRE AS CIDADES
mediaVE = dataset['VALOREMPENHO'].mean()
print("\n A MEDIA DO VALOR EMPENHO ENTRE AS CIDADES É:", mediaVE)
