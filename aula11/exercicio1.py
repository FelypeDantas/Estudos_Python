n = int(input("Insira o número para o fatorial: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(n))

# fibonnaci(4)          fibonacci(3) + fibonacci(2)
# fibonnaci(3)          fibonacci(2) + fibonacci(1)
# fibonnaci(2)          fibonacci(1) + fibonacci(0)
# fibonnaci(1)          1
# fibonnaci(0)          0