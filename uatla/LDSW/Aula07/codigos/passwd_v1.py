def verificaPalavraPasse(passwd_dic, passwd_input):
    return(passwd_dic == passwd_input)

# Dicionario que guarda os utilizadores
dic = {}

user = "Maria"
passwd = "teste123"

dic[user] = passwd

# Assumindo que user é Maria...
passwd_in = input("Palavra-passe: ")
print(verificaPalavraPasse(dic[user], passwd_in))