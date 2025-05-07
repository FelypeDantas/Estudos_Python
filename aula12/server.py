import socket

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir o endereço e porta de escuta
host = '127.0.0.1'  # IP local
port = 12345  # Porta arbitrária

# Associar o socket a um endereço e porta
server_socket.bind((host, port))

# Escutar por conexões
server_socket.listen(1)
print(f"Servidor aguardando por conexões em {host}:{port}...")

# Aceitar a conexão
client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

# Receber dados do cliente e enviar uma resposta
while True:
    data = client_socket.recv(1024)  # Tamanho do buffer de recebimento
    if not data:
        break  # Se não houver dados, encerra a comunicação
    print(f"Recebido do cliente: {data.decode()}")
    client_socket.sendall(b'Obrigado pela mensagem!')  # Envia uma resposta

# Fechar a conexão
client_socket.close()
server_socket.close()
