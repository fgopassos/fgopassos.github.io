from socket import *
import struct
import marshal

serverPort = 12000
serverName = "localhost"

try:
	# Criacao do socket
	clientSocket = socket(AF_INET, SOCK_STREAM)
	# Conexao com o servidor
	clientSocket.connect((serverName,serverPort))
except Exception as m:
	print("Erro ao conectar!")
    print(str(m))
	quit()

num_ok = False
N = 0

while not num_ok:
    try:
        N = int(input("Entre com o número: "))
        num_ok = True
    except:
        print("Erro! Valor digitado não corresponde a um número!")


clientSocket.send(struct.pack("i", N))
data = clientSocket.recv(1024)
lista = marshal.loads(data)
print(lista)

clientSocket.close()

