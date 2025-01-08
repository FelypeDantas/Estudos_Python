valores = []
continuar = input('Deseja adicionar um número? ')
soma = 0

try:
    while(continuar == 'sim'):

        numero = int(input('Digite um número inteiro: '))
        valores.append(numero)

        continuar = input('Deseja acrescentar mais um valor? ')
except:
    print('tipo de entrada inválida')

for valor in valores:
    print(valor)
    soma = soma + valor
    print(f'a soma é {soma}')