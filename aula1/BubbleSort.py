def ordenar(vetor):
    for i in range(1, 5):
        for j in range(0, 4):
            if vetor[j] > vetor[j + 1]:
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux
    return vetor

def exibir(vetor):
    for i in range(5):
        print(vetor[i])

vetor = [5, 4, 2, 1, 8]
ordenar(vetor)
exibir(vetor)