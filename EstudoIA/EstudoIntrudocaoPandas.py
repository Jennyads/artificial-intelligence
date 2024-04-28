import pandas as pd


alunos = {'Nomes': ['Ricardo', 'Pedro', 'Carlos'], 'Nota': [4, 7, 5.5], 'Aprovado': ['Não', 'Sim', 'Não']}

dataframe = pd.DataFrame(alunos)

#print(dataframe)


obejeto1 = pd.Series([2, 4, 6, 8, 10])
#print(obejeto1)



alunosDic = {'Nomes': ['Ricardo', 'Pedro', 'Carlos'], 'Nota': [4, 7, 5.5], 'Aprovado': ['Não', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)
print(alunosDF)

alunosDF.head()

print(alunosDF.shape)# tamanho do dataframe ex: 3,3


print(alunosDF.describe())#descreve detalhado os dados numericos que existe no dataframe
