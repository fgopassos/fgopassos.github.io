---
author: Fernanda Passos
note: Linguagem Programação
date:
subtitle: Aula 07
title: Modularização em Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Modularização (I)

- Permite organizar o código em partes/módulos.
    - Também chamado de sub-programas.
- Cada módulo tem seu objetivo.
- Pode possuir entradas e saídas.
    - Geralmente entradas são computadas pelo código do módulo 
- Há dois tipos de módulos:
    - **Função**: retorna valor.
    - **Procedimento**: não retorna valor.

# Modularização (II)

- Na **declaração** de um módulo, deve indicar:
    - nome: identificador;
    - argumentos ou parâmetros: dados de entrada e/ou saída.
    - retorno: se for uma função.
- Assinatura: definição do módulo contendo nome e argumentos...
- Na **chamada** de um módulo:
    - o nome deve ser utilizado;
    - os parâmetros devem corresponder à assinatura do módulo;
    - se for função, associar o retorno a alguma ação (atribuir a uma variável, imprimir, ...).

# Funções e Procedimentos em Python{.part}

# Declaração de Funções em Python

- Funções em Python são implementadas usando `def`.
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
    - Os parâmetros devem ser 3 números inteiros.
    - Não usar a função `min`.
2. Escreva um procedimento que imprima a tabuada formatada (de 1 a 10) de um dado número.


# Escopo de Variáveis (I)

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
~~~{#ex1 .python style="font-size: 75%;"}
def f2():
    x = 10

f2()
print(x)
~~~
::::
::::{.column width=5%}
::::
::::{.column width=50%}
<span style="color:red">Erro!</span> <br>
`x` está no escopo local de `f2` e é acessível apenas em `f2`.
::::
:::::

- Exemplo de acesso à variável em escopo global:


:::::{.columns}
::::{.column width=45%}
~~~{#ex1 .python style="font-size: 75%;"}
def f3():
    x = y + 10
    print(x)

y = 2
f3()
~~~
::::
::::{.column width=5%}
::::
::::{.column width=50%}
<span style="color:green">Ok!</span> <br>
`y` está em escopo global, acessível pelo escopo de `f3`!
::::
:::::

# Exercício (II)

### Para cada código abaixo, indique o que será impresso:

:::::{.columns}
::::{.column width=47%}
~~~{#ex1 .python style="font-size: 90%;"}
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
~~~{#ex1 .python style="font-size: 90%;"}
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

# Parâmetros de Função

- Podem ser de tipos primitivos: números, strings, booleanos...
- Parâmetro é nova variável e valor é copiado para ela.
    - Está dentro de escopo local!
- Modificação de parâmetro só é visível dentro de escopo da função.
    - Apenas a cópia é modificada.

:::::{.columns}
::::{.column width=45%}
~~~{#ex .python style="font-size: 80%;"}
def f(y):
    y = "laranja"
    print("Dentro de f:", y)

y = "uva"
print("Antes de chamar f:", y)
f(y)
print("Depois de chamar f:", y)
~~~

::::
::::{.column width=10%}

::::
::::{.column width=45%}
~~~{#exSaida .csv style="font-size: 80%;"}
Antes de chamar f: uva
Dentro de f: laranja
Depois de chamar f: uva
~~~
::::
:::::


# Parâmetros de Função (II)

- Podem também ser listas, tuplas e dicionários.
- Agora, é importante fazer distinção entre **referência** e **valor**.

~~~{#ex1 .python style="font-size: 75%;"}
l = [1, 2, 3]
~~~

- Neste exemplo, `l` é **referência**.
    - Os elementos são os **valores**.
- Em Python, apenas a referência de `l` é copiada para a variável local do parâmetro da função.

~~~{#ex1 .python style="font-size: 75%;"}
def func(v):
    print(v)

l = [1, 2, 3]
func(l)
~~~

# Parâmetros de Função (III)

- Alterar a referência **não modifica** lista externamente:

~~~{#ex1 .python style="font-size: 80%;"}
def func(v):
    v = [10, 20, 30]
    print("Dentro da função:", v)

l = [1, 2, 3]
print("Antes de chamar a função:", l)
func(l)
print("Depois de chamar a função:", l)
~~~

~~~{#ex1 .text style="font-size: 70%;"}
Antes de chamar a função: [1, 2, 3]
Dentro da função: [10, 20, 30]
Depois de chamar a função: [1, 2, 3]
~~~

# Parâmetros de Função (IV)

- Alterar valor **modifica** a lista externamente:

~~~{#ex1 .python style="font-size: 80%;"}
def func(v):
    v[0] = 10
    v[1] = 20
    print("Dentro da função:", v)

l = [1, 2, 3]
print("Antes de chamar a função:", l)
func(l)
print("Depois de chamar a função:", l)
~~~

~~~{#ex1 .text style="font-size: 70%;"}
Antes de chamar a função: [1, 2, 3]
Dentro da função: [10, 20, 3]
*Depois de chamar a função: [10, 20, 3]
~~~

# Retorno de Funções

- O retorno pode ser de qualquer tipo.
    - Primitivos: int, float, bool...
    - Strings, listas, tuplas, dicionários...
- Exemplo retornando lista:


~~~{#ex1 .python style="font-size: 75%;"}
def pares(x, y):
    lista = []
    for i in range(x, y+1):
        if i % 2 == 0:
            lista.append(i)
    return(lista)

print(pares(3, 10))
~~~

~~~{#ex1 .python style="font-size: 75%;"}
[4, 6, 8, 10]
~~~

# Retorno de Funções (II)

- Exemplo retornando tupla:

~~~{#ex1 .python style="font-size: 75%;"}
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
print(r)
if r != None:
    print("O menor elemento", r[0], "está na posição", r[1], "do vetor.")
~~~

# Retorno de Funções (III)

- Exemplo retornando dicionário:

~~~{#ex1 .python style="font-size: 75%;"}
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

### Para cada código abaixo, indique o que será impresso:

:::::{.columns}
::::{.column width=45% }
~~~{#ex1 .python style="font-size: 90%;"}
# Programa 3:
def f3(x, y):
    y = y - x
    x = x + 2

y = 5
x = 2
f3(x, y)
print(x, y)
~~~

::::
::::{.column width=10%}

::::
::::{.column width=45%}
~~~{#ex1 .python style="font-size: 90%;"}
# Programa 4:
def f4(y):
    y = y + 10
    return(y)

y = 2
x = f4(y)
print(x, y)
~~~
::::
:::::


# Exercícios (IV)

### Para cada item, escreva um programa em Python que:

1. Escreva uma função que calcule o fatorial de um dado $n$.
    - Exemplo: para $n = 5$, $fat(n) = 5 \times 4 \times 3 \times 2 \times 1$.
2. Escreva uma função que calcule as raízes da fórmula de Bháskara, a partir de $a$, $b$ e $c$.
$$ x = \frac{-b \pm \sqrt{b^2 - 4 \times a \times c}}{2 \times a} $$

# Recursão

- Capacidade de uma função chamar a si própria.
- Útil para **recorrências**.
    - Isto é, uma função em que cada termo de uma sequência é definido em função dos elementos anteriores.
- Assim como em uma repetição, deve ter uma **condição de parada**.
- Exemplo:

:::::{.columns}
::::{.column width=45%}
~~~{#id .python }
def contagemRegressiva(n):
    if n == 0:
        print('Decolar!')
    else:
        print(n)
        contagemRegressiva(n-1)
~~~
::::
::::{.column width=10%}

::::
::::{.column width=45%}
~~~{#id .python }
def contagemRegressiva(n):
    while(n):
        print(n)
        n = n - 1
    print('Decolar!')
~~~
::::
:::::

# Exemplo de Função Recursiva: Recorrência

:::::{.columns}
::::{.column width=45%}
- Fatorial: função de recorrência.
$$fat(n) = \left\{ \begin{array}{ll}
         1 & \mbox{if $n \geq 0$};\\
        n \times fat(n-1) & \mbox{if $n > 0$}.\end{array} \right.$$
::::
::::{.column width=10%}

::::
::::{.column width=45%}
~~~{#fat .python }
def fatorial(n):
    # Para n >= 0
    if n == 0:
        return 1
    else:
        temp = n * fatorial(n-1)
        return temp
~~~
::::
:::::

# Mais um Exemplo e Exercício

- Função de recorrência de Fibonacci:
$$fib(n) = \left\{ \begin{array}{ll}
         0 & \mbox{if $n = 0$};\\
         1 & \mbox{if $n = 1$};\\
         fib(n-1) + fib(n-2) & \mbox{if $n > 1$}.\end{array} \right.$$

- **Exercício:** Escreva uma função recursiva para calcular o enésimo termo da sequência Fibonacci conforme a função de recorrência acima.


# Exercício (VI)

1. Escreva uma função recursiva que calcule a potência de um $x$ elevado a $n$.
    - Isto é, $potencia(x, n)$
    - Isto é, o mesmo que `x**n`

# Solução

~~~{#id .python }
def potencia(x, n):
    if n == 0:
        return 1
    else:
        return(x * potencia(x, n-1))
~~~

# Função anónima: lambda

- Python permite criar função *sem nome*.
- Sintaxe: **`lambda argumentos: expressão`**
- Exemplo:
~~~{#id .python }
print((lambda x: x**2 - x + 2)(10))
~~~
- Exemplo com atribuição de nome:
~~~{#id .python }
nome_func = lambda x: x**2 - x + 2
print("y = ", nome_func(10))
~~~


# Função anónima: lambda *vs.* definição de função

:::::{.columns}
::::{.column width=45%}

- Função lambda:

~~~{#id .python }
nome_func = lambda x: x**2 - x + 2

print("y = ", nome_func(4))
~~~
::::
::::{.column width=10%}

::::
::::{.column width=45%}

- Definição de função:

~~~{#id .python }
def nome_func(x):
    return(x**2 - x + 2)

print("y = ", nome_func(4))
~~~
::::
:::::

# Uso do lambda

- Bom para realizar operações curtas.
- Quando deseja-se aplicar uma função simples a uma série de elementos.
    - Por exemplo, elevar ao quadrado todos os elementos de uma lista.
- Usado em diversos módulos de Python para análise de dados.
    - Por exemplo, módulo *pandas*.

# Exemplo com Argumento *key* de função *sorted*

- Objetivo: mostrar ordenação de dicionário por valor.
    - Uso do argumento `key` da função `sorted` do Python.
    - `key` (opcional) aceita função para decidir a ordem.
    
~~~{#id .python style="font-size: 90%;"}
frutas={'laranja':30, 'maçã': 25, 'morango': 40, 'uva': 25}

for e in sorted(frutas, key=lambda f: frutas[f]):
    print(e, frutas[e])
~~~

~~~{#id .csv style="font-size: 70%;"}
maçã 25
uva 28
laranja 30
morango 40
~~~

# Uso do lambda: filter

- Função *built-in* `filter`.
- Aplica um filtro (função que retorna verdadeiro ou falso) a cada elemento de uma lista/tupla.
    - Retorna um objeto *filter* que pode ser convertido para lista ou tupla.
- Exemplo: filtrar todos os elementos pares de uma tupla:

~~~{#id .python style="font-size: 90%;"}
tupla = (1, 5, 8, 9, 2, 3, 15, 18)
print(list(filter(lambda arg: arg % 2 == 0, tupla)))
~~~

~~~{#id .csv style="font-size: 70%;"}
[8, 2, 18]
~~~

# Uso do lambda: map

- Função *built-in* `map`.
- Aplica um mapa (resultado de uma função) a cada elemento de uma lista/tupla.
    - Retorna um objeto *map* que pode ser convertido para lista ou tupla.
- Exemplo: elevar ao cubo todos os elementos de uma lista:

~~~{#id .python style="font-size: 90%;"}
lista = [1, 5, -8, 9, 2, 3, -15, 18]
print(list(filter(lambda x: x**3, lista)))
~~~

~~~{#id .csv style="font-size: 70%;"}
[1, 125, -512, 729, 8, 27, -3375, 5832]
~~~

# Manipulação de Strings em Python {.part}

# Manipulação de Strings

- Python apresenta diversas funções e métodos para manipular strings.
- Útil para lidar com texto de entrada do `input`, por exemplo.
- Algumas delas são:
    - Converter para string.
    - Obter tamanho de string.
    - Separar strings por espaço (ou outro caractere).
    - Colocar todas as letras maiúsculas (ou minúsculas).
    - Verificar se é algarismo, letra.
    - Verificar se uma string é substring de outra.
    - Entre muitas outras...

# Operações Sobre Strings

:::::{.columns}
::::{.column width=50%}

- Acesso à letra:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 'banana'
print(palavra[2])
~~~

- Tamanho de string:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 'banana'
print(len(palavra))
~~~

- Pertinência de letra:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 'banana'
if 'ana' in palavra:
    print(palavra, "contém 'ana'.")
else:
    print(palavra, "não contém 'ana'.")
~~~

::::
::::{.column width=10%}
<br>
&#8680;

<br><br>

&#8680;

<br><br>

&#8680;
::::
::::{.column width=40%}
Saída:

~~~{#exSaida .text style="font-size: 75%;"}
n
~~~

Saída:

~~~{#exSaida .text style="font-size: 75%;"}
6
~~~

Saída:

~~~{#exSaida .text style="font-size: 75%;"}
banana contém 'ana'.
~~~
::::
:::::

# Operações Sobre Strings (II)

:::::{.columns}
::::{.column width=50%}
- Concatenar strings:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 'ban' + 'ana'
print(palavra)
~~~

- Multiplicar string:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 3*'blá '
print(palavra)
~~~

- Iterar em uma string:

~~~{#ex1 .python style="font-size: 75%;"}
palavra = 'banana'
cont_a = 0
for letra in palavra:
    if letra == 'a':
        cont_a = cont_a + 1
print("Existem", cont_a, "letras 'a' em",
palavra)
~~~

::::
::::{.column width=10%}
<br>
&#8680;

<br><br>

&#8680;

<br><br>

&#8680;
::::
::::{.column width=40%}
Saída:

~~~{#exSaida .text style="font-size: 75%;"}
banana
~~~

Saída:

~~~{#exSaida .text style="font-size: 75%;"}
blá blá blá
~~~

Saída:

~~~{#exSaida .text style="font-size: 75%;"}
Existem 3 letras 'a'
em banana
~~~
::::
:::::

# Operações Sobre Strings (III)

- Transformar string em lista/tupla de caracteres:

~~~{#ex1 .python}
palavra = 'trasplante'
lista = list(palavra) # para tupla, trocar list por tuple
print(lista)
~~~

~~~{#exSaida .text}
['t', 'r', 'a', 's', 'p', 'l', 'a', 'n', 't', 'e']
~~~

# Operações Sobre Strings (IV)

- Juntar novamente com método `join`:

~~~{#ex1 .python}
palavra = 'trasplante'
lista = list(palavra)
lista.insert(3, 'n')
print(''.join(lista))
~~~

~~~{#exSaida .text}
transplante
~~~

# Métodos de Strings

- Métodos sobre string: função associada a uma string.
    - Forma de uso: `var_string.metodo()`
- Existem várias:

:::{style="font-size: 16pt;"}
Método  |  Parâmetros     | Descrição                                                         |
--------|-----------------|-------------------------------------------------------------------
split   | sep (opcional)  | Retorna lista contendo substrings separadas por sep.
count   | substr          | Conta quantas substrings há na string.
find    | substr          | Procura a primeira ocorrência da substring na string. Retorna o índice e -1 se não encontrar.
replace | str1, str2      | Retorna a string substituindo str2 em todas as ocorrências de str1.
join    | lista           | Junta strings de uma lista separadas pela string de chamada.
:::

# Métodos de Strings (II)

:::{style="font-size: 20pt;"}
Método  |  Parâmetros   | Descrição                                            |
--------|---------------|-------------------------------------------------------
upper   | nenhum      | Retorna a string com todas as letras maiúsculas.
lower   | nenhum      | Retorna a string com todas as letras minúsculas.
isalpha | nenhum      | Retorna True ou False para indicar se string contém apenas letras.
isdigit | nenhum      | Retorna True ou False para indicar se string contém apenas dígitos.
islower | nenhum      | Retorna True ou False para indicar se string está toda em minúscula.
isupper | nenhum      | Retorna True ou False para indicar se string está toda em maiúscula.
:::

# Métodos de Strings (III)

:::{style="font-size: 20pt;"}
Método  |  Parâmetros   | Descrição                                            |
--------|---------------|-------------------------------------------------------
center  | d, c (opcional)     | Retorna string centralizada em d quantidade de caracteres, complementando com c (caractere).
rjust   | d, c (opcional)     | Retorna string alinhada à direita em d quantidade de caracteres, complementando com c (caractere).
ljust   | d, c (opcional)     | Retorna string alinhada à esquerda em d quantidade de caracteres, complementando com c (caractere).
:::

- Para ver mais, aceder: https://wiki.python.org.br/ManipulandoStringsComPython

# Exercício (VII)

1. Escrever uma função que indica se uma string é palíndromo.
    - Uma palavra (ou texto) é palíndromo se ela é lida da mesma forma em ambos os sentidos (de frente para trás ou de trás para frente).
2. Obter frase do usuário e remover todo espaço sobrando entre as palavras.
    - Isto é, deixar apenas um espaço entre cada palavra.
3. Obter frase do usuário e indicar a ocorrência da palavra 'não'.
4. Obter frase do usuário e apresentar a quantidade de cada caractere existente nela. Dica: usar dicionário com a chave sendo a letra e o valor sendo a quantidade.

# Checar se Entrada é Número (I)

- Forma mais correta de verificar se uma entrada é número:
    - Usar comando `try-except`
- Como usar para este fim:

~~~{#ex1 .python style="font-size: 75%;"}
try:
    n = int(input("Entre com um número: "))
except ValueError:
    print("Erro de entrada!")
    print("Finalizando programa...")
    quit() # Termina programa
~~~

# Checar se Entrada é Número (II)

- Neste exemplo, tenta-se fazer a conversão.
- Se der erro (ValueError), o erro em si não aparece!
    - Ao invés disso, executa o código dentro do `except`.
- `try-except` também pode ser usado para outros fins.
    - Veremos em aulas futuras.

# Checar se Entrada é Número (III)

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

# Exercício (VIII)

1. Obter matriz do usuário linha por linha. Cada linha deve ser tratada como string e os valores devem ser convertidos para float.
    - Multiplique todos os valores da matriz por -1.
    - Imprima a matriz ao final.
