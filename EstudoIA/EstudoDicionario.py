
#dicionario = {chave:valor}

dicionario = {'Curso': 'Python', 'Produtor': 'Diego', 'Preço': 'gratis'}

print(dicionario['Curso'])
print(dicionario['Preço'])


a = dicionario['Preço']

print(a)

dicionario['Preço'] = 'R$300.00'

print(dicionario)

dicionario['Pré-requisito'] = 'Python Básico' 

print(dicionario)


print(dicionario.keys())
print(dicionario.values())
print(dicionario.clear())