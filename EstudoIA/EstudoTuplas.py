

list = [2,4,5]

list[0] = 1
del list[0]
print(list)

# Não é possivel alterar uma tupla é imutavel

tupla = (6, 7, 8)

tupla[0] = 1

del tupla[0] 

tupla.append(10)

print(tupla)


teste = tuple(list)
print(teste)