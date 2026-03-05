def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

# Uso
escrever_arquivo("arqText.txt", "Curso Prático\nAula prática")
print(ler_arquivo("arqText.txt"))

def menu():
    print("1 - Escrever no arquivo")
    print("2 - Ler arquivo")
    print("3 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("Digite o conteúdo: ")
        escrever_arquivo("arqText.txt", texto)
        print("Conteúdo salvo com sucesso!")

    elif opcao == "2":
        print("Conteúdo do arquivo:")
        print(ler_arquivo("arqText.txt"))

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
