
---
author: Fernanda Passos
note: Programação Avançada
date:
subtitle: Aula 04
title: Comandos de Repetição em Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

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

