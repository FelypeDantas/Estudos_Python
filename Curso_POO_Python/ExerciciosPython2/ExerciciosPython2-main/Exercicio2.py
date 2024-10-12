idade = int(input('entre com a sua idade: '))

if idade >= 0 and idade <= 12:
    print('Você está na categoria Criança')
elif idade >= 13 and idade <= 18:
    print('Você está na categoria Adolescente')
elif idade >= 18:
    print('Você está na categoria Adulto')
else:
    print('Idade inválida')