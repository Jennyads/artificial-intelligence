import pandas as pd


#Abrir com o excel
dados = pd.read_excel('C:/Users/diego/OneDrive/Área de Trabalho/arquivoPandas.xlsx')

print(dados.head(7))



#Abrir um arquivo csv
dadosCsv = pd.read_csv('C:/Users/diego/OneDrive/Área de Trabalho/InteligenciaArtificial/athlete_events.csv')


print(dadosCsv.head(10))