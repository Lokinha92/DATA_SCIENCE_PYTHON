import pandas as pd
#import seaborn as srn
import statistics  as sts

#importando dados
dataset = pd.read_csv('./DADOS/Churn.csv', sep=";")

#visualizando
#print(dataset.head())

#tamanho
#print(dataset.shape)

#Dando nome as colunas
dataset.columns =  ["Id","Score","Estado","Genero","Idade","Patrimonio",
                    "Saldo","Produtos","TemCartCredito","Ativo","Salario","Saiu"]

#Visualizando
#print(dataset.head())

#EXPLORANDO DADOS CATEGORICOS

#estado
#agrupadoEstado = dataset.groupby(['Estado']).size()
#print(agrupadoEstado)
#agrupadoEstado.plot.bar(color='green')

#genero
#agrupadoGenero = dataset.groupby(['Genero']).size()
#print(agrupadoGenero)
#agrupadoGenero.plot.bar(color='red')




#EXPLORANDO DADOS NUMERICOS

#score
#describe = dataset['Score'].describe()
#print(describe) #descreve os dados pra mim #pra descrever precisa printar

                                                    #count -> Quantos dados tem
                                                    #mean -> Media
                                                    #50% -> Mediana
                                                    #min -> valor minimo
                                                    #max -> valor maximo

#boxplotSCORE = srn.boxplot(dataset['Score']).set_title('SCORE')
#histogramaSCORE = srn.distplot(dataset['Score']).set_title('SCORE')

#pra plotar nao precisa printar
#------------------------------------------------------------------------------

#idade
#descreveIDADE = dataset['Idade'].describe()
#print(descreveIDADE)
#boxplotIDADE = srn.boxplot(dataset['Idade']).set_title('IDADE')
#histogramaIDADE = srn.distplot(dataset['Idade']).set_title('IDADE')

#------------------------------------------------------------------------------

#saldo
#descreveSALDO = dataset['Saldo'].describe()
#print(descreveSALDO)
#boxplotSALDO = srn.boxplot(dataset['Saldo']).set_title('SALDO')
#histogramaSALDO = srn.distplot(dataset['Saldo']).set_title('SALDO')

#------------------------------------------------------------------------------

#salario
#descreveSALARIO = dataset['Salario'].describe()
#print(descreveSALARIO)
#boxplotSALARIO = srn.boxplot(dataset['Salario']).set_title('SALARIO')
#histogramaSALARIO = srn.distplot(dataset['Salario']).set_title('SALARIO')

#------------------------------------------------------------------------------

#Tratando dados NAN
#print("NUMERO DE NAN NO DATASET ANTES DE TRATAR")
#print(dataset.isnull().sum(), "\n")
#TRATANDO SALARIO:

#print("DESCREVENDO OS DADOS DA COLUNA")
#descreveSALARIO = dataset['Salario'].describe()
#print(descreveSALARIO, "\n")
#mediana = sts.median(dataset['Salario'])
#dataset['Salario'].fillna(mediana, inplace=True)
#print("*** FIM DO TRATAMENTO ***\n")
#print("Numero de NAN da coluna salario depois de tratar --> ", dataset['Salario'].isnull().sum())

#TRATANDO GENERO
#descrevegenero = dataset['Genero'].describe()
#print(descrevegenero, "\n")
#dataset['Genero'].fillna('Masculino', inplace=True)
#print("NUMERO DE NAN DO GENERO DEPOIS DE TRATAR ---> ", dataset['Genero'].isnull().sum(), "\n")
#agrupagenero = dataset.groupby(['Genero']).size()
#print (agrupagenero, "\n")

#PROBLEMAS NO DOMINIO:
    #de genero: F, fem, feminino // M, masc, Masculino
#dataset.loc[dataset['Genero'] == 'M', 'Genero'] = "Masculino"
#dataset.loc[dataset['Genero'].isin(['F', 'Fem']), 'Genero'] = "Feminino"
#newagrupa = dataset.groupby(['Genero']).size()
#print(newagrupa)

#------------------------------------------------------------------------------

    #de idade: idade < 0 e idade > 120
#describeIDADE= dataset['Idade'].describe()
#print(describeIDADE)
#visualizaerros = dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120)]
#print(visualizaerros)
#mediana = sts.median(dataset['Idade'])
#print(mediana)
#dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120), 'Idade'] = mediana
#newvisu = dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120)]
#print(newvisu)

#------------------------------------------------------------------------------

    #Dados Duplicados:

#duplicado = dataset[dataset.duplicated(['Id'], keep=False)]
#print(duplicado)
#dataset.drop_duplicates(subset='Id', keep='first', inplace=True)
#temduplicado = dataset[dataset.duplicated(['Id'], keep=False)]
#print(temduplicado)

#------------------------------------------------------------------------------

       #Estados fora do dominio
    
#agrupadoESTADO = dataset.groupby(['Estado']).size()
#print(agrupadoESTADO)
#print(dataset['Estado'].describe())

#moda = 'RS'

#dataset.loc[dataset['Estado'].isin(['RP', 'SP', 'TD']), 'Estado'] = moda

#novoagrupa = dataset.groupby(['Estado']).size()
#print(novoagrupa)

#------------------------------------------------------------------------------

    #Outliers em salário (considerar 2 desvios padrao)
    
desvio = sts.pstdev(dataset['Salario'])
print(desvio)

condicao = dataset.loc[dataset['Salario'] >= 2*desvio]
print(condicao)
