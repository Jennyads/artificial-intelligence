
# Estudo Lista

import random

list1 = [1,2,3]
# type(list1)
# print(list1[2])

list2 = [[1,0,9], [2,3,5], [7,8,9]]
# print(list2[2][1])


cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
escolhida = random.choice(cidades)

print(escolhida)

## Método append para adicionar na lista
cidades.append('Acre')
#print(cidades)

## Adicionando varios item na lista
outrasCidades = ['Amazonas', 'teste', 'agua']

for item in outrasCidades: 
    cidades.append(item)
## print(cidades)


x = [2, 4, 10, 6]

y = []

for item in x:
    y.append(float(item))
print(y)   
