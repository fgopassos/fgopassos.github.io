import hashlib, string, random

def verificaPalavraPasse(salt, hash, passwd):
    bytes = (salt+passwd).encode()
    return(hashlib.sha256(bytes).digest() == hash)
    
def geraHash(passwd):
    caracteres = string.ascii_letters+string.digits+string.punctuation
    # Gera um salt de 16 bits aleatoriamente
    salt = ''.join(random.choices(caracteres, k=16))
    # Gera o hash (SHA 256) do salt + palavra-passe
    hash = hashlib.sha256((salt+passwd).encode())
    # Retorna uma tupla com o salt e os bytes do hash
    return (salt, hash.digest())


# Dicionario que guarda os utilizadores
dic = {}

user = "Maria"
passwd = "teste123"

dic[user] = {} # Ex.: {'Maria': {'salt' = '...', 'hash': '...'}}
# Insere hash da palavra-passe para o utilizador
dic[user]["salt"], dic[user]["hash"] = geraHash(passwd)

# Assumindo que user é Maria...
passwd_in = input("Palavra-passe: ")
print(verificaPalavraPasse(dic[user]["salt"], dic[user]["hash"], passwd_in))

