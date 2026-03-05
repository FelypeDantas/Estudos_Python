ARQUIVO = "arqText.txt"

def escrever_arquivo(nome_arquivo, conteudo, modo="w"):
    try:
        with open(nome_arquivo, modo, encoding="utf-8") as arquivo:
            arquivo.write(conteudo + "\n")
        print("✅ Conteúdo salvo com sucesso!")
    except Exception as erro:
        print(f"❌ Erro ao escrever no arquivo: {erro}")


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "⚠️ Arquivo ainda não existe."
    except Exception as erro:
        return f"❌ Erro ao ler arquivo: {erro}"


def menu():
    print("\n📂 GERENCIADOR DE ARQUIVO")
    print("1 - Escrever (substituir conteúdo)")
    print("2 - Adicionar texto ao arquivo")
    print("3 - Ler arquivo")
    print("4 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("Digite o conteúdo: ")
        escrever_arquivo(ARQUIVO, texto, "w")

    elif opcao == "2":
        texto = input("Digite o conteúdo a adicionar: ")
        escrever_arquivo(ARQUIVO, texto, "a")

    elif opcao == "3":
        print("\n📖 Conteúdo do arquivo:")
        print(ler_arquivo(ARQUIVO))

    elif opcao == "4":
        print("👋 Encerrando programa...")
        break

    else:
        print("⚠️ Opção inválida!")
