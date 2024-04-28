import pandas as pd


dadosCsv = pd.read_csv('C:/Users/diego/OneDrive/Área de Trabalho/InteligenciaArtificial/athlete_events.csv')
print(dadosCsv.head())



dadosCsv.rename(columns={'Name' : 'NOME', 'Sex': 'SEXO', 'Age': 'IDADE'}, inplace = True) #Alterar os nomes das colunas
print(dadosCsv.head())


altura = dadosCsv['Height']  #Mostra a culuna alturas
print(altura)


medalhas = dadosCsv['Medal'].value_counts() #Mostra quantas vezes aparece ex: Gold: 13372, Bronze: 13295, Silver: 13116
print(medalhas)



 #Excluir coluna 
dadosCsv.drop('ID', axis=1, inplace=True)
dadosCsv.drop('Season', axis=1, inplace=True)
dadosCsv.drop('City', axis=1, inplace=True)

print(dadosCsv.head())