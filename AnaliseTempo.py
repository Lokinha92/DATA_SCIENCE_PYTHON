import statistics as sts
import pandas as pd

dataset = pd.read_csv('./tempo.csv', sep=';')
show = dataset.head()

print(show, "\n\n")
NAs = dataset.isnull().sum()
print("NA's: \n", NAs)

umidadedesc = dataset['Umidade'].describe()
print("Descrevendo a umidade....... \n", umidadedesc)

mediana = sts.median(dataset['Umidade'])
#print(mediana)
dataset['Umidade'].fillna(mediana, inplace=True)

verifica = dataset.isnull().sum()
print("VERIFICANDO...... \n", verifica)

#tratando NAN VENTO

describeVENTO = dataset['Vento'].describe()
print("DESCREVENDO DADOS.........\n",describeVENTO)
moda = "FALSO"
dataset['Vento'].fillna(moda, inplace=True)

verificaATT = dataset.isnull().sum()
print("VERIFICANDO TRATAMENTO.............\n",verificaATT)

showATT = dataset.head()
print("\n", showATT, '\n\n')
#______________________________________________________________________________

#TRATANDO APARENCIA - DOMINIO

agrupaAPARENCIA = dataset.groupby(['Aparencia']).size()
print(agrupaAPARENCIA)

describeAPARENCIA = dataset['Aparencia'].describe()
print("\n", describeAPARENCIA)

dataset.loc[dataset['Aparencia'] == "menos", 'Aparencia'] = 'sol'
verificaAPARENCIA =  dataset.groupby(['Aparencia']).size()
print("\n", verificaAPARENCIA, "\n\n")

#__________________________________________________________________________

#TRATANDO TEMPERATURA:

describeTEMP = dataset['Temperatura'].describe()
print("DESCREVENDO TEMPERATURA......... \n", describeTEMP,"\n")

condicao = dataset.loc[(dataset['Temperatura'] < (-130)) | (dataset['Temperatura'] > 130)]
print("DADOS FORA DA CONDICAO: \n", condicao, '\n')

mediana = sts.median(dataset['Temperatura'])
dataset.loc[(dataset['Temperatura'] < (-130)) | (dataset['Temperatura'] > 130)] = mediana

newcond = dataset.loc[(dataset['Temperatura'] < (-130)) | (dataset['Temperatura'] > 130)]
print("VERIFICANDO SE AINDA EXISTEM DADOS FORA DA CONDICAO..........\n",newcond, "\n\n")

#------------------------------------------------------

#TRATANDO UMIDADE:

describeUMIDADE = dataset['Umidade'].describe()
print("DESCREVENDO DADOS UMIDADE........\n", describeUMIDADE)

foradominio = dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)]
print("DADOS DORA DO DOMINIO: \n", foradominio)

mediana = sts.median(dataset['Umidade'])
dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)] = mediana

verificadomUMIDADE = dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)]
print("VERIFICANDO SE AINDA EXISTEM DADOS FORA DA CONDICAO..........\n",verificadomUMIDADE)

#---------------------------------------------------------------------

#TRATANDO COLUNA JOGAR

agrupaJOGAR = dataset.groupby(['Jogar']).size()
print("DADOS AGRUPADOS: JOGAR.........\n", agrupaJOGAR)

dataset.loc[dataset['Jogar'] == 73.5, 'Jogar'] = 'sim'
dataset.loc[dataset['Jogar'] == 82.5, 'Jogar'] = 'nao'

verificaJOGAR = dataset.groupby(['Jogar']).size()
print("VERIFICANDO SE AINDA EXISTEM DADOS FORA DA CONDICAO..........\n", verificaJOGAR)