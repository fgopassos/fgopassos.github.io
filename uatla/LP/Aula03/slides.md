---
author: Fernanda Passos
note: Linguagem de Programação
date:
subtitle: Aula 03
title: Condicionais e Repetições em Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Condicionais em Python{.part}

# Condicional de Um Ramo em Python

- Sintaxe:
~~~{#cond1 .python}
if (condicao):
    # Bloco que será executado se condição for verdadeira.
~~~

- Note que o afastamento da margem esquerda determina o bloco.
- Exemplo de dois comandos dentro do bloco `if`:

~~~{#condEx1 .python}
    a = 0
    x = int(input("Entre com um número: "))
    if (x > 0):
        print("Número é positivo.")
        a = a + 1
    print(a)
~~~


# Indentação em Python

::::::{.block .centered}
:::{.blocktitle}
Definição de Indentação:
:::
É o afastamento horizontal em relação à margem esquerda.
::::::

- Usado para criar os blocos.
    - Importantíssimo em Python!
    - Pode causar erros se não for feito de forma correta!
- Podem ser espaços ou tabs.
    - Muitas vezes tabs são convertidos (pelo editor de texto) em 4 ou 8 espaços.
- **[Dica]{style="color:violet"}**: usar sempre tecla **tab** para realizar a indentação.
    - Ou usar sempre a mesma quantidade de espaços.


# Condicional de Dois Ramos em Python

- Sintaxe:

~~~{#cond2 .python style="font-size: 80%"}
if (condicao):
    # Bloco que será executado se condição for verdadeira.
else:
    # Bloco que será executado se condição for falsa.
~~~

- Exemplo:

~~~{#condEx2 .python style="font-size: 80%"}
a = 0
x = int(input("Entre com um número: "))
if (x > 0):
    print("Número é positivo.")
    a = a + 1
else:
    print("Número é zero ou negativo.")
    a = a - 1
print(a)
~~~


# Expressões Relacionais em Python

- Operadores são similares aos da matemática:

Operador | Significado
:-------:|:-----------:
    ==   | igualdade
    !=   | diferença
    >    | maior
    <    | menor
    >=   | maior ou igual
    <=   | menor ou igual

# Expressões Lógicas em Python

- São usadas nas condições de um **if**, por exemplo.
- Constantes lógicas: `True`, `False`.
- Expressões relacionais.
- Operadores lógicos:
    - `not` (não)
    - `or` (ou)
    - `and` (e)
- Prioridade:
    - Maior: Parênteses
    - Depois: expressões relacionais
    - Depois: not
    - Menor: or, and

# Aninhamento de if

- Comando: `elif`
- Exemplo:
~~~{#condEx3 .python style="font-size: 70%; width: 90%"}
num = float(input("Entre com um número: "))
if (num < 0):
    print(num, "é negativo!")
elif (num < 25):
    print(num, "está no intervalo [0, 25[.")
elif (num < 50):
    print(num, "está no intervalo [25, 50[.")
elif (num < 75):
    print(num, "está no intervalo [50, 75[.")
elif (num <= 100):
    print(num, "está no intervalo [75, 100].")
else:
    print(num, "é maior que 100.")
~~~

# Aninhamento de if (II)

- Também pode ser transformado em else e if interno.
    - Fica em forma de escada.

~~~{#condEx4 .python style="font-size: 70%"}
num = float(input("Entre com um número: "))
if (num < 0):
    print(num, "é negativo!")
else:
    if (num < 25):
        print(num, "está no intervalo [0, 25[.")
    else:
        if (num < 50):
            print(num, "está no intervalo [25, 50[.")
        else:
            if (num < 75):
                print(num, "está no intervalo [50, 75[.")
            else:
                if (num <= 100):
                    print(num, "está no intervalo [75, 100].")
                else:
                    print(num, "é maior que 100.")
~~~

# Módulo de Matemática

- Através do módulo `math`.
	- Funções matemáticas definidas pelo C Standard.
	- Deve ser incluído no início do código (import).
- Algumas funções:
	- `sqrt(x)`: retorna a raiz quadrada do parâmetro x;
	- `log2(x)`: retorna o logaritmo de x na base 2;
	- `log10(x)`: retorna o logaritmo de x na base 10;
	- `log(x)`: retorna o o logaritmo neperiano (base e) de x;
	- `log(x, b)`: retorna o o logaritmo de x na base b;
	- `ceil(x)`: retorna o teto do parâmetro x;
	- `floor(x)`: retorna o piso do parâmetro x.
- Apresenta também constantes como:
	- `math.pi`, `math.e`, `math.inf`.
	

# Exercícios (I)

## Faça programas em Python para:

1. Obter um número inteiro e indicar se ele é par ou ímpar.
1. Obter um número inteiro e indicar se ele é múltiplo de 3 ou 7.
1. Obter um número inteiro e indicar se ele é múltiplo de 3 e não múltiplo de 2.
1. Obter dois números reais e indicar se a raiz quadrada da soma das potências de 2 deles é maior que 100. Isto é, se $\sqrt{x^2 + y^2} > 100$. Use `math.sqrt(z)` para calcular a raiz quadrada de um número z. Use `import math` no início de seu programa para importar o módulo.


# Módulo de Números Aleatórios (I)

- Através do módulo random.
	- Deve ser incluído no início do código (import).
- Gera vários tipos de números aleatórios, embaralha conjuntos, escolhe elemento de um conjunto, ...
	- `random()`: retorna um número real aleatório no intervalo [0.0, 1.0).
	- `randint(a, b)`: retorna um número inteiro aleatório entre a e b.
- Exemplo: gerar um número aleatório inteiro de 1 a 10.

~~~{#condEx5 .python}
import random

numAleatorio = random.randint(1, 10) # Retorna número aleatório entre 1 e 10.
~~~

# Módulo de Números Aleatórios (II)

- Semente (seed): define a fonte (semente) de uma sequência de números aleatórios.
	- `random.seed(s)`
- Em programação de computadores, números aleatórios são pseudo-aleatórios.
	- Com a mesma semente, ao reexecutar o programa, ele irá gerar os mesmos números aleatórios!
	- Sem especificar semente, sementes diferentes são usadas a cada chamada de um método de geração de número aleatório.
- Para mais detalhes, consultar: https://docs.python.org/3/library/random.html 


# Exercícios (II)

## Faça programas em Python para:

:::::{.columns}
::::{.column style="width: 60%; font-size: 16px;"}
1. Obter um número inteiro do usuário e indicar se ele acertou o número sorteado pelo programa entre 1 e 10. Caso o usuário erre, indique também se o número digitado é maior ou menor que o número sorteado.
2. Ler as duas notas parciais obtidas por um aluno numa disciplina, calcular sua média e atribuir conceitos conforme a tabela ao lado. O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E. 

::::
::::{.column width=40%}

:::{style="line-height: 100%; font-size: 20px;"}

Média $x$ de Aproveitamento |  Conceito
-----------------------:|:---------
$9{,}0 \le x < 10{,}0$        | A
$7{,}5 \le x < 9{,}0$         | B
$6{,}0 \le x < 7{,}5$         | C
$4{,}0 \le x < 6{,}0$         | D
$0{,}0 \le x < 4{,}0$        | E

:::

::::

:::::


# Repetições em Python {.part}

# Repetição Definida em Python

- Comando `for`.
- Sintaxe:

~~~{#idfor .python}
for i in sequência:
    # Bloco que será repetido com valor i.
~~~

- Note que o afastamento da margem esquerda determina o bloco.

# Sequência de Repetição

- Repetição é feita em .**sequência de valores** explícita.
- Sequência de qualquer valor, não necessariamente números.
- Algumas formas de se especificar uma sequência:
    - (1, 4, 5)
    - ("a", "e", "i", "o", "u")
    - (1, "dois", 7.9, -1)
- Exemplo:
~~~{#idforEx1 .python}
for k in (1, "dois", 7.9, -1):
    print(k)
~~~

- São 4 repetições e em cada uma delas k terá o valor da sequência.
	- Primeiro 1, depois "dois", depois 7.9 e depois -1.

# Range

- O comando `range` de Python permite especificar faixa de valores numéricos.
- Apresenta os seguintes parâmetros (nesta ordem):
    - **início** (opcional): indica o início da sequência inclusive.
    - **fim** (obrigatório): indica o fim da sequência (não inclusive).
    - **incremento** (opcional): indica o incremento da sequência.
- Exemplo:

~~~{#idforEx1 .python}
for k in range(5):
    print(k)
~~~

- k varia em {0, 1, 2, 3, 4} em cada repetição.

# Range (II)

:::::{.columns}
::::{.column width=45%}
## Exemplo com início especificado:

~~~{#idforEx2 .python}
for k in range(4, 10):
    print(k)
~~~

- k varia em {4, 5, 6, 7, 8, 9} em cada repetição.
::::

::::{.column width=5%}
::::

::::{.column width=50%}
## Exemplo com início e incremento especificados:

~~~{#idforEx3 .python}
for k in range(4, 10, 2):
    print(k)
~~~

- k varia em {4, 6, 8} em cada repetição.
::::

:::::

# Exemplo de Uso do for

- Programa que imprime os números pares entre m e n.
~~~{#idforEx4 .python}
m = int(input("Entre com o primeiro valor do intervalo: "))
n = int(input("Entre com o segundo valor do intervalo: "))
for i in range(m, n):
    if i % 2 == 0:
        print(i)
~~~

# Imprimindo Séries

- No exemplo do slide anterior, o print imprime linha por linha.
- Em Python, podemos imprimir a série em uma mesma linha de diversas maneiras.
- Veremos duas delas:
    - Concatenando strings e imprimindo o resultado no final.
    - Suprimindo quebra de linha do comando print.

# Concatenando Strings

- Para juntar (concatenar) strings, basta usar o sinal `+` entre strings.
- Para converter um número em string, usar:
    - `str(número)`

~~~{#idforEx4 .python}
m = int(input("Entre com o primeiro valor do intervalo: "))
n = int(input("Entre com o segundo valor do intervalo: "))
texto = ''
for i in range(m, n):
    if i % 2 == 0:
        texto = texto + ' ' + str(i)
print(texto)
~~~

- Note que deve haver um espaço entre o texto anterior e o valor de i.
- Saída para m = 1 e n = 10: `2 4 6 8 `


# Suprimindo Quebra de Linha

- O comando print permite especificar parâmetros opcionais.
- Um deles é o `end=`.
    - Uso: `print('texto', end='')`
    - Indica qual(is) caractere(s) de finalização da string.
    - Por padrão, é a quebra de linha (cujo código é '\n').
- Se `end` é igualado a `' '` (espaço), a quebra de linha é substituída por um espaço.

~~~{#idforEx5 .python}
m = int(input("Entre com o primeiro valor do intervalo: "))
n = int(input("Entre com o segundo valor do intervalo: "))
for i in range(m, n):
    if i % 2 == 0:
        print(i, end=' ')
print() # Para quebrar linha no final apenas
~~~

- Saída para m = 1 e n = 10: `2 4 6 8 `

# Exercício I

#### Faça programas em Python para:

1. Escrever o resultado do produtório de 10 números obtidos do usuário.
1. Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo Fib(n) = Fib(n-1) + Fib(n-2). Como base tem-se que Fib(0) = 0 e Fib(1) = 1. Por exemplo, caso o usuário informe o número 9, o resultado seria: 0, 1, 1, 2, 3, 5,  8, 13, 21, 34.
1. Indicar se um dado n é primo (divisível apenas por 1 e ele mesmo).

# Solução

<iframe height="500px" width="1200px" src="https://repl.it/@fgopassos/fibonacci?lite=true#main.py" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

# Repetição Indefinida em Python

- Comando `while`.
- Similar ao uso em pseudocódigo.
- Sintaxe:

~~~{#idWhile .python}
while condição:
    # Bloco que será repetido enquanto condição é verdadeira.
~~~

- Note que o afastamento da margem esquerda determina o bloco.

# Repetição Indefinida em Python (II)

- Exemplo:

~~~{#idWhile .python}
x = int(input("Entre com um número: "))
while x >= 0:
    print(x)
    x = x - 1
print("Fim!")
~~~

# Exercício II

## Faça programas em Python para:

1. Pedir que o usuário entre com um número inteiro positivo até que ele realmente seja. Depois, calcule o fatorial deste número e apresente o resultado.
1. Repetir o processo de obter um número inteiro do usuário até que ele acerte o número sorteado pelo programa, entre 1 e 10. Caso ele acerte, exiba uma mensagem parabenizando. Caso erre, como dica, indique se o número digitado é maior ou menor que o número sorteado.
	- Adicionalmente, conte quantas vezes o usuário tentou acertar o número e exiba esta informação ao final.

# Exercícios III

## Faça programas em Python para:

1. Imprimir a tabuada de 1 a 10 da seguinte forma:

```
    1 x 1 = 1
    1 x 2 = 2
    ...
```

2. Gerar a tabela de jogos de um campeonato de futebol que tem 4 times (times jogam em casa e na casa do adversário).
    - Os times são: Benfica, Sporting, Porto e Braga.

```
    Benfica  x Sporting
    Benfica  x Porto 
    ...
```

# Alguns Desvios Incondicionais {.part}

# Comando break (I)

- O comando `break` serve para **sair de repetições abruptamente**.
- Exemplo de uso:

~~~{#idWhileEx1 .python}
for i in range(3, 100, 3):
  print(i, end=" ") # Imprime múltiplos de 3 a partir de 3.
  if i % 7 == 0: # Quando o índice também for divisível por 7, para.
    break
print()
~~~

- Embora o melhor seja estruturar o código apenas com condições (no while), pode ser útil as vezes.
  - O break desestrutura o código.
  - Mas pode ser útil em alguns casos para facilitar a escrita.

# Comando break (II)

- Exemplo: imprimir todos os 5 primeiros múltiplos naturais de 2 ou 3 usando um for.

~~~{#idWhileEx2 .python}
cont = 0
# Usar um range com um limite superestimado.
for i in range(0, 100):
  if i % 2 == 0 or i % 3 == 0:
    print(i, end=" ")
    cont = cont + 1
  if cont == 5:
    break
print()
~~~

- **Exercício:** modificar nosso algoritmo para indicar se um número é primo ou não, usando um break assim que encontrar um número divisível.

# Comando continue

- O comando `continue` é semelhante ao break mas tem o efeito oposto.
  - Ao invés de parar o loop, ele continua.
  - O que ele faz é voltar para o laço inicial de repetição.
  - Ignora todos os comandos após ele.
- Exemplo: indicar quantos números diferentes de 0 foram lidos do usuário.

~~~{#idWhileEx3 .python}
cont = 0
for i in range(10):
  n = int(input("Entre com um número: "))
  if n == 0:
    continue
  cont = cont + 1
print("Foram lidos", cont, "numeros diferentes de 0.")
~~~

# Desvio Incondicional

- `break` e `continue` são exemplos de **desvio incondicional**.
- Repare que eles só fazem sentido dentro de comandos de repetição.
  - E devem ser usados dentro de if's.
- Evitar o uso, pois desestrutura o código.
  - Seu uso excessivo pode trazer confusão.
      - Quem vê um `for` ou `while` espera que a repetição ocorra até o fim!
  - Usar apenas quando for extremamente necessário.

