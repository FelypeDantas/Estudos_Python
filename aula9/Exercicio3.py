valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for valor in valores:
    if valor % 2 != 0:
        soma = soma + valor
print(soma)
