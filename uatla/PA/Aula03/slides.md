---
author: Fernanda Passos
note: Programação Avançada
date:
subtitle: Aula 03
title: Condicionais em Python
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

