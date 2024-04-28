import pandas as pd

alunosDic = {'Nomes': ['Ricardo', 'Pedro', 'Carlos'], 'Nota': [4, 7, 5.5], 'Aprovado': ['Não', 'Sim', 'Não']}
alunosDF = pd.DataFrame(alunosDic)


primeirasLinhas = alunosDF.loc[0:2]
print(primeirasLinhas)


novoDF = alunosDF[alunosDF['Nota']!=5.5] # Vai todas as linhas menos a linha que tem a nota 5.5 (Excluir!!)
print(novoDF)



alunosReprovados = alunosDF[alunosDF['Aprovado'] == 'Não']# Vai todos os alunos reprovados
print(alunosReprovados)