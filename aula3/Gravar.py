arquivo = open("arqText.txt", "w")

arquivo.write("Curso Prático \n")
arquivo.write("Aula prática")
arquivo.close()

#Leitura do arquivo texto
leitura = open("arqText.txt", "r")
print(leitura.read())
leitura.close()
