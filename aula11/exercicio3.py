n = int(input("Digite um número inteiro: "))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci de {n} é {fibonacci(n)}")