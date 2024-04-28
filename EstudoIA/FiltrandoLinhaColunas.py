import pandas as pd

alunosDic = {'Nomes': ['Ricardo', 'Pedro', 'Carlos'], 'Nota': [4, 7, 5.5], 'Aprovado': ['Não', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)
print(alunosDF)

print(alunosDF['Aprovado']) # Por coluna


print(alunosDF.loc[[1]]) #Pega a linha de acordo com o indice
print(alunosDF.loc[[0,1,2]]) #Pega a linha de acordo com o indice
print(alunosDF.loc[0:2]) #Pega a linha de acordo com o indice



print(alunosDF.loc[alunosDF['Nomes'] == 'Pedro']) #Pega apenas a linha com nome Pedro (Nomes= coluna)