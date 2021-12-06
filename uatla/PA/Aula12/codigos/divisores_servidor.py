from socket import *
import struct
import marshal
import threading

def divisores(N):
    lista = [1]
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            lista.append(i)
    if N != 1:
        lista.append(N)
    return(lista)

def trataRequisicao(connectionSocket):

    # Recebe requisição do cliente
    pacote = connectionSocket.recv(8)

    N, = struct.unpack('i', pacote)

    print(f"Servidor recebeu pacote com N = {N}")

    # Tratando a requisição do cliente
    print("Tratando requisição...")
    lista_div = divisores(N)

    # Envia mensagem de resposta para o cliente
    connectionSocket.send(marshal.dumps(lista_div))
    print(f"Servidor enviou a lista de divisores para o cliente.")

    # Fecha a conexão
    connectionSocket.close()


#######################################
# PROGRAMA PRINCIPAL
#######################################

# Numero de porta.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_STREAM indicam TCP.
serverSocket = socket(AF_INET, SOCK_STREAM)
# Reusar porta no caso de matar processo, por exemplo.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Associa porta ao socket.
serverSocket.bind(('', serverPort))
# Aceita 1 conexao por vez antes de realizar o accept.
serverSocket.listen(1)

while True:
    # Aguardar nova conexao
    print ('Aguardando conexao...')
    connectionSocket, addr = serverSocket.accept()

    # Trata a requisicao sem usar threads
    # Descomente aqui para testar sem e comente as 
    # duas linhas de código abaixo.
    #trataRequisicao(connectionSocket)

    # Trata a requisicao usando threads
    t = threading.Thread(target=trataRequisicao, args=(connectionSocket,))

    # Inicia a thread
    t.start()


