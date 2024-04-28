kmh = [40, 50, 60, 70, 80, 90, 100, 120]

mph = []

for i in kmh:
    mph.append(i/1.61)
print(mph)


mph2 = list(map(lambda x: x/1.61, kmh))

print(mph2)

#List Comprehension
mph3 = [x/1.61 for x in kmh]
print(mph3)


caracteres = [i for i in 'Teste de informatica']
print(caracteres)