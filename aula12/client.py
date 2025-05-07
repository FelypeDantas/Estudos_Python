import socket

# Criação do socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir o endereço e porta do servidor
host = '127.0.0.1'  # IP do servidor
port = 12345  # Mesma porta do servidor

# Conectar ao servidor
client_socket.connect((host, port))
print(f"Conectado ao servidor {host}:{port}")

# Enviar dados para o servidor
message = "Olá, servidor! Como você está?"
client_socket.sendall(message.encode())

# Receber a resposta do servidor
data = client_socket.recv(1024)
print(f"Recebido do servidor: {data.decode()}")

# Fechar a conexão
client_socket.close()
