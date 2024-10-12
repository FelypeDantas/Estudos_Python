numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = ['Felype', 'José', 'Maria', 'Pascal']

datas = [2003, 2024]

print('1 - nomes')
print('2 - numeros')
print('3 - datas')

escolha = int(input('insira a sua escolha: \n'))

if escolha == 1:
    for nome in nomes:
        print(nome)
elif escolha == 2:
    for numero in numeros:
        print(numero)
elif escolha == 3:
    for data in datas:
        print(data)
else:
    print('valor inválido')