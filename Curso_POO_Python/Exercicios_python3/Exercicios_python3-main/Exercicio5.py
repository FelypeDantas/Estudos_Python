multiplicador = int(input('Digite o valor: '))
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = 0

for valor in valores:
    resultado = multiplicador * valor
    print(f'{multiplicador} X {valor} = {resultado}')