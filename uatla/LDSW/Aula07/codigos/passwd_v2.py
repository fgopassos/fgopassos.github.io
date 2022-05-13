import hashlib

def verificaPalavraPasse(hash, passwd):
    bytes = passwd.encode()
    return(hashlib.sha256(bytes).digest() == hash)
    
def geraHash(passwd):
    # Gera o hash (SHA 256) da palavra-passe
    hash = hashlib.sha256(passwd.encode())
    # Obtém o hexadecimal e retorna
    return (hash.digest())


# Dicionario que guarda os utilizadores
dic = {}

user = "Maria"
passwd = "teste123"

dic[user] = {}
# Insere hash da palavra-passe para o utilizador
dic[user]["hash"] = geraHash(passwd)

# Assumindo que user é Maria...
passwd_in = input("Palavra-passe: ")
print(verificaPalavraPasse(dic[user]["hash"], passwd_in))