---
author: Fernanda Passos
note: Programação Avançada
date:
subtitle: Aula 06
title: Módulos/Funções em Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Módulos: Procedimentos e Funções

# Módulos

- 

# Funções em Python{.part}

# Declaração de Funções em Python

- Funções (e procedimentos) em Python são implementados usando `def`.
    - Define o **bloco** da função/procedimento.
- Sintaxe de função (com retorno):

~~~{#ex1 .python}
def nome_funcao(parametros):
    # Corpo da função
    return valor_retorno
~~~

- `nome_funcao` é identificador (letras, algarismos - não no início - e '_').
- `parametros` é opcional e são separados por vírgula.
- `valor_retorno` é o valor de retorno da função.

# Declaração de Procedimentos em Python

- Similar à função, mas **sem** `return`.
- Sintaxe de procedimento:

~~~{#ex1 .python}
def nome_procedimento(parametros):
    # Corpo do procedimento
~~~

- `nome_procedimento` é identificador (letras, algarismos - não no início - e '_').
- `parametros` é opcional e são separados por vírgula.
    - Parênteses são obrigatórios mesmo sem parâmetros!

# Chamada de Funções

- Exemplo de uma função que implementa uma equação de segundo grau:

~~~{#ex1 .python}
# Definição da função f1:
def f1(x):
    y = x**2 - 2*x + 4
    return y

num = float(input("Entre com um numero: "))
# Chamada de f1:
resultado = f1(num)
print(resultado)
~~~

- Função/Procedimento deve ser declarando antes de uso!

# Chamada de Procedimentos

- Exemplo de procedimento que imprime cabeçalho:

~~~{#ex1 .python}
# Definicao do procedimento cabecalho:
def cabecalho(nome_programa, autor):
    print('******************************')
    print('{:^30}'.format(nome_programa))
    print('{:^30}'.format("Autor: " + autor))
    print('******************************')

# Chamada de cabecalho:
cabecalho("Olá mundo!", "Fernanda")
~~~

# Exercício I

## Faça o que se pede em Python:

1. Escreva uma função que indique o maior valor entre 3 números.
2. Escreva um procedimento que imprima a tabuada (de 1 a 10) de um dado número.


# Escopo de Variáveis

- O escopo de uma variável indica sua visibilidade.
    - Isto é, onde a variável é acessível (leitura) no código.
- Os escopos podem ser:
    - **global**: variáveis são acessíveis em todos os escopos.
    - **local**: variáveis são acessíveis apenas no escopo em que foram declaradas.

:::::::{.center}
![](imagens/escopo.svg){#escopo width=60%}
:::::::

# Escopo de Variáveis (II)

- Exemplo de acesso à variável de escopo inexistente:

:::::{.columns}
::::{.column width=45%}
~~~{#ex1 .python}
def f2():
    x = 10

f2()
print(x)
~~~
::::
::::{.column width=5%}
::::
::::{.column width=50%}
<br>
<span style="color:red">Erro!</span>
<br>
`x` está no escopo local de `f2` e é acessível apenas em `f2`.
::::
:::::

- Exemplo de acesso à variável em escopo global:


:::::{.columns}
::::{.column width=45%}
~~~{#ex1 .python}
def f3():
    x = y + 10
    print(x)

y = 2
f2()
~~~
::::
::::{.column width=5%}
::::
::::{.column width=50%}
<br>
Ok!<br> `y` está em escopo global, acessível pelo escopo de `f3`!
::::
:::::

# Exercício (II)

## Para cada código abaixo, indique o que será impresso:

:::::{.columns}
::::{.column width=47%}
~~~{#ex1 .python}
# Programa 1:
def f1():
    x = y + 10
    z = y + 1
    print(x, z)

y = 5
f1()
print(y)
~~~

::::
::::{.column width=6%}
::::
::::{.column width=47%}
~~~{#ex1 .python}
# Programa 2:
def f2():
    x = y + 10
    print(x, y)

y = 5
f2()
print(x, y)
~~~

::::
:::::

# Parâmetros em LP

- Há 2 tipos de passagem de parâmetros:
    - **Passagem por valor:** apenas o valor da variável é passado para o escopo do módulo.
        - Há uma cópia do valor internamente.
        - Alterações no parâmetro não modificam a variável externa ao módulo.
    - **Passagem por referência:** é passada a referência da variável.
        - Logo, valor da variável pode mudar.

# Parâmetros em Python

- Python distingue objetos como **mutável** e **imutável**.
- Objetos mutáveis: seu
    - Exemplos: variáveis de 

# Parâmetros de Função

- Podem ser de tipos primitivos: números, strings, booleanos...
- Parâmetro é nova variável e valor é copiado para ela.
    - Está dentro de escopo local!
- Modificação de parâmetro só é visível dentro de escopo da função.
    - A cópia é modificada.

~~~ Python
def f(y):
    y = "laranja"
    print("Dentro de f:", y)

y = "uva"
print("Antes de chamar f:", y)
f(y)
print("Depois de chamar f:", y)
~~~

~~~
Antes de chamar f: uva
Dentro de f: laranja
Depois de chamar f: uva
~~~

# Parâmetros de Função (II)

- Podem também ser listas, tuplas e dicionários.
- Agora, é importante fazer distinção entre .alert[referência] e .alert[valor].

~~~{#ex1 .python}
l = [1, 2, 3]
~~~

- Neste exemplo, `l` é **referência**.
    - Os elementos são os **valores**.
- Em Python, apenas a referência de `l` é copiada para a variável local do parâmetro da função.

~~~{#ex1 .python}
def func(v):
    print(v)

l = [1, 2, 3]
~~~

# Parâmetros de Função (III)

- Alterar **referência** .alert[não modifica] lista externamente:

~~~ Python
def func(v):
    v = [10, 20, 30]
    print("Dentro da função:", v)

l = [1, 2, 3]
print("Antes de chamar a função:", l)
func(l)
print("Depois de chamar a função:", l)
~~~

~~~
Antes de chamar a função: [1, 2, 3]
Dentro da função: [10, 20, 30]
*Depois de chamar a função: [1, 2, 3]
~~~

# Parâmetros de Função (IV)

- Alterar **valor** .alert[modifica] a lista externamente:

~~~ Python
def func(v):
    v[0] = 10
    v[1] = 20
    print("Dentro da função:", v)

l = [1, 2, 3]
print("Antes de chamar a função:", l)
func(l)
print("Depois de chamar a função:", l)
~~~

~~~
Antes de chamar a função: [1, 2, 3]
Dentro da função: [10, 20, 3]
*Depois de chamar a função: [10, 20, 3]
~~~

# Retorno de Funções

- O retorno pode ser de qualquer tipo.
    - Primitivos: int, float, bool...
    - Strings, listas, tuplas, dicionários...
- Exemplo retornando lista:


~~~ Python
def pares(x, y):
    lista = []
    for i in range(x, y+1):
        if i % 2 == 0:
            lista.append(i)
    return(lista)

print(pares(3, 10))
~~~

~~~
[4, 6, 8, 10]
~~~

# Retorno de Funções (II)

- Exemplo retornando tupla:

~~~ Python
# Função que retorna o menor elemento e sua posição no vetor.
def menor(vet):
    if len(vet) <= 0:
        return(None)
    menor = vet[0]
    menor_i = 0
    for i in range(1, len(vet)):
        if vet[i] < menor:
            menor = vet[i]
            menor_i = i
    return((menor, menor_i))

v = [1, 4, -2, 0, 10, -2, 1]
r = menor(v)
if r != None:
    print("O menor elemento", r[0], "está na posição", r[1], "do vetor.")
~~~

~~~Text
(-2, 2)
~~~

# Retorno de Funções (III)

- Exemplo retornando dicionário:

~~~ Python
# Obtem do usuário dados de uma agenda telefônica.
def obtem_agenda():
    agenda = {}
    nome = input("Nome: ")
    while nome != '':
        telefone = input("Telefone: ")
        if nome in agenda:  #Guarda telefones em lista.
            agenda[nome].append(telefone)
        else:
            agenda[nome] = [telefone]
        nome = input("Nome: ")
    return(agenda)

agenda = obtem_agenda()
print(agenda)
~~~

# Exercícios (III)


#### Para cada código abaixo, indique o que será impresso:

.col-3[
~~~{#ex1 .python}
# Programa 3:
def f3(x, y):
    y = y - x
    x = x + 2

y = 5
x = 2
f3(x, y)
print(x, y)
~~~
]

![:column 10%](<br>)

.col-3[
~~~{#ex1 .python}
# Programa 4:
def f4(y):
    y = y + 10
    return(y)

y = 2
x = f4(y)
print(x, y)
~~~
]

<br><br><br><br><br><br> <br><br>

#### Para cada item, escreva um programa em Python que:

1. Defina uma função para gerar a sequência fibonacci até um dado n (inclusive).
    - Teste sua função usando os valores -1, 0, 1, 10 e 100.

---

class: section-slide
layout: false

# Manipulação de Strings em Python

---

template: conteudo
layout: true

# Manipulação de Strings

- Python apresenta diversas funções e métodos para manipular strings.
- Útil para lidar com texto de entrada do `input`, por exemplo.
- Algumas utilizadas:
    - Converter para string.
    - Obter tamanho de string.
    - Separar strings por espaço (ou outro caractere).
    - Colocar todas as letras maiúsculas (ou minúsculas).
    - Verificar se é algarismo, letra.
    - Verificar se uma string é substring de outra.
    - Entre muitas outras...

# Operações Sobre Strings

![:column 60%](
- Acesso à letra:

~~~{#ex1 .python}
palavra = 'banana'
print(palavra[2]\)
~~~

- Tamanho de string:

~~~{#ex1 .python}
palavra = 'banana'
print(len(palavra\)\)
~~~

- Pertinência de letra:

~~~{#ex1 .python}
palavra = 'banana'
if 'ana' in palavra:
    print(palavra, "contém 'ana'."\)
else:
    print(palavra, "não contém 'ana'."\)
~~~
)

![:column 7%](<br><br>)

![:column 33%](
<br>
Saída:

~~~
n
~~~
<br>

Saída:

~~~
6
~~~

<br>

Saída:

~~~
banana contém 'ana'.
~~~
)

# Operações Sobre Strings (II)

![:column 60%](
- Concatenar strings:

~~~{#ex1 .python}
palavra = 'ban' + 'ana'
print(palavra\)
~~~

- Multiplicar string:

~~~{#ex1 .python}
palavra = 3*'blá '
print(palavra\)
~~~

- Iterar em uma string:

~~~{#ex1 .python}
palavra = 'banana'
cont_a = 0
for letra in palavra:
    if letra == 'a':
        cont_a = cont_a + 1
print("Existem", cont_a, "letras 'a' em",
palavra\)
~~~
)

![:column 7%](<br><br>)

![:column 33%](
<br>
Saída:

~~~
banana
~~~
<br>

Saída:

~~~
blá blá blá
~~~

<br>

Saída:

~~~
Existem 3 letras 'a'
em banana
~~~
)

# Operações Sobre Strings (III)

- Transformar string em lista/tupla de caracteres:

~~~{#ex1 .python}
palavra = 'trasplante'
lista = list(palavra) # para tupla, trocar list por tuple
print(lista)
~~~

~~~
['t', 'r', 'a', 's', 'p', 'l', 'a', 'n', 't', 'e']
~~~

- Juntar novamente com método `join`:

~~~{#ex1 .python}
palavra = 'trasplante'
lista = list(palavra)
lista.insert(3, 'n')
print(''.join(lista))
~~~

~~~
transplante
~~~

# Métodos de Strings

- Métodos sobre string: função associada a uma string.
    - Forma de uso: `var_string.metodo()`
- Existem várias:

Método  |  Parâmetros | Descrição |
--------|-------------|------------
`split`   | sep (opcional) | Retorna lista contendo substrings separadas por sep.
`count`   | substr          | Conta quantas substrings há na string.
`find`    | substr          | Procura a primeira ocorrência da substring na string. Retorna o índice e -1 se não encontrar.
`replace` | str1, str2      | Retorna a string substituindo str2 em todas as ocorrências de str1.
`join`    | lista           | Junta strings de uma lista separadas pela string de chamada.

# Métodos de Strings (II)

Método  |  Parâmetros   | Descrição |
--------|---------------|------------
`upper`   | nenhum      | Retorna a string com todas as letras maiúsculas.
`lower`   | nenhum      | Retorna a string com todas as letras minúsculas.
`isalpha` | nenhum      | Retorna True ou False para indicar se string contém apenas letras.
`isdigit` | nenhum      | Retorna True ou False para indicar se string contém apenas dígitos.
`islower` | nenhum      | Retorna True ou False para indicar se string está toda em minúscula.
`isupper` | nenhum      | Retorna True ou False para indicar se string está toda em maiúscula.

# Métodos de Strings (III)

Método  |  Parâmetros   | Descrição |
--------|---------------|------------
`center`  | d, c (opcional)     | Retorna string centralizada em d quantidade de caracteres, complementando com c (caractere).
`rjust`   | d, c (opcional)     | Retorna string alinhada à direita em d quantidade de caracteres, complementando com c (caractere).
`ljust`   | d, c (opcional)     | Retorna string alinhada à esquerda em d quantidade de caracteres, complementando com c (caractere).

- Para ver mais, acesse:

https://wiki.python.org.br/ManipulandoStringsComPython

# Exercício (III)

1. Escrever uma função que indica se uma string é palíndromo.
    - Uma palavra (ou texto) é palíndromo se ela é lida da mesma forma em ambos os sentidos (de frente para trás ou de trás para frente).
2. Obter frase do usuário e remover todo espaço sobrando entre as palavras.
    - Isto é, deixar apenas um espaço entre cada palavra.
3. Obter frase do usuário e indicar a ocorrência da palavra 'não'.
4. Obter frase do usuário e apresentar a quantidade de cada caractere existente nela. Dica: usar dicionário com a chave sendo a letra e o valor sendo a quantidade.

# Checar se Entrada é Número

- Meio mais correto de verificar se uma entrada é número:
    - Usar comando `try-except`
- Como usar para este fim:

~~~{#ex1 .python}
try:
    n = int(input("Entre com um número: "))
except ValueError:
    print("Erro de entrada!")
    print("Finalizando programa...")
    quit() # Termina programa
~~~

- Neste exemplo, tenta-se fazer a conversão.
- Se der erro (ValueError), o erro em si não aparece!
    - Ao invés disso, executa o código dentro do `except`.
- `try-except` também pode ser usado para outros fins.
    - Veremos em aulas futuras.

# Checar se Entrada é Número (II)

- Para checar repetidamente:

~~~{#ex1 .python}
num_ok = False
while not num_ok:
    try:
        num = int(input("Entre com um número: "))
        num_ok = True
    except ValueError:
        print("Erro de entrada! Número deve ser inteiro!")

# Usar num a partir daqui...
~~~

# Exercício (IV)

1. Obter matriz do usuário linha por linha. Cada linha deve ser tratada como string e os valores devem ser convertidos para float.

