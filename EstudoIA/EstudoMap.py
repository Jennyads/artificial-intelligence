
kmh = [40, 50, 60, 70, 80, 90, 100, 120]

mph = []

for i in kmh:
    mph.append(i/1.61)
print(mph)


mph2 = list(map(lambda x: x/1.61, kmh))

print(mph2)