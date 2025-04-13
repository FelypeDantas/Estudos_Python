n = int(input("Digite um número inteiro: "))

def soma_n(n):
    if n == 0:
        return 0
    return n + soma_n(n - 1)

print(f"A soma dos números de 1 a {n} é: {soma_n(n)}")