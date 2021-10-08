---
author: Fernanda Passos
note: Linguagem de Programação
date: 
subtitle: Aula 02
title: Introdução à Linguagem Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Python: uma Linguagem Multiparadigma

- Imperativa: comandos são ações.
- Orientada a objetos: abstração de dados.
- Programação concorrente e paralela.
- Programação funcional: notação *lambda*.


# Python é Originalmente Orientada a Objetos

- A linguagem Python possui sua sintaxe bem definida.
- *Coisas* em Python são referidas como **objetos**.
    - Constantes, variáveis, listas, tuplas, dicionários...
    - Veremos com detalhes cada um deles em aulas futuras.
- Também veremos como programar orientado a objetos.
	- Definição de classes;
	- Instanciação de objetos;
	- ...

# Exemplo de Classe em Python

~~~{#exClasse .python}
class Pessoa:

    # Construtor
    def __init__(self, nome, id, idade):
        self.nome = nome
        self.id = id
        self.idade = idade

    # Método padrão que converte classe em string
    def __str__(self):
        return("Nome: " + self.nome + ", ID: " + self.id + ", Idade: " + str(self.idade))

    def adicionaIdade(self):
        self.idade += 1
~~~

# Python Estruturado

- Tudo em Python é objeto.
- No entanto, a *programação orientada a objetos* é geralmente opcional.
	- Embora os objetos básicos da linguagem estejam sempre presentes!
- Códigos em Python podem ser programados de forma **estruturada**.
	- Sequências de comandos;
	- Estruturas de controle (seleção e repetições).

# Python Concorrente e Paralelo

- Apresenta módulos para criar tarefas concorrentes ou paralelas.
	- Concorrente: programa que concorre por recursos (processamento, memória, I/O, ...).
	- Paralelo: recurso é multiplicado e, portanto, são usados simultaneamente.
- **Multithreading**: concorrente.
- **Multiprocessing**: processos paralelos.
- Mecanismos para sincronizar tarefas.
	- *Locks*;
	- Semáforos;
	- Filas de recursos (*queue*).

# Interpretando Códigos em Python

- Linguagem é **interpretada**.
	- Trechos de códigos são traduzidos por vez.

:::::{.columns}
::::{.column width=33.3%}
~~~{#interpretacao .python}
a = 5
b = 2
c = a + b
d = c * 2
~~~
::::
::::{.column width=28.3%}
:::::::{.center}
<br>
<span style='font-size: 80px; color: blue'> ➡ </span>
:::::::
::::
::::{.column width=33.3%}
~~~{#saida .qq}
a = 5
b = 2
c = 7
d = 14
~~~
::::
::::{.column width=5%}
::::
:::::


# Entendendo Erros em Python

- Qualquer interpretador de Python é capaz de acusar erros de sintaxe.
- Exemplo: suponha o seguinte código:
~~~{#primeiroProg .python}
prit("Olá Mundo!")
~~~
- Podemos perceber que o comando `print` está escrito errado.
- A mensagem de execução do comando será:

<pre class="nova" style="font-size:16px; font-family: 'Roboto', Roboto, mono; color:red;">
$ python3 olaMundo.py 
Traceback (most recent call last):
  File "olaMundo.py", line 2, in <module>
    prit("Olá Mundo!")
NameError: name 'prit' is not defined
</pre>

# Erros e Interpretação de Código

- Código executa até interpretar uma linha que contenha erro.

:::::{.columns}
::::{.column width=45%}
- Este código tem um erro na 5ª linha.
	- Programa é interrompido nesta linha!
~~~{#erroInterpretando .python}
a = 4
b = 9
print("Valor de a:", a)
print("Valor de b:", b)
comandoNaoExiste()
c = a + b
print(c)
~~~
::::
::::{.column width=5%}
::::
::::{.column width=45%}
- Este código tem erro na linha 6.
	- Mas programa executa até o fim!
~~~{#erroInterpretando .python}
a = 4
b = 9
print("Valor de a:", a)
print("Valor de b:", b)
if (a == 3):
	comandoNaoExiste()
c = a + b
print(c)
~~~
::::
::::{.column width=5%}
::::

:::::

# Comentários de Linha

- Comentários em códigos são bem vindos!
    - São partes do código que serão ignoradas.
    - Servem para incluir alguma explicação do código.
- `#` é o caractere que define um comentário.
- Exemplo:

~~~{#id .python}
# Programa que imprime "Olá"
print("Olá") # Comentário pode ser usado aqui também!
~~~

# Comentários de Bloco

- Comentário de bloco:
    - Texto entre `'''` e `'''`.

~~~{#id .python}
''' Programa que imprime "Olá".
    Este é um exemplo de mais de uma linha de comentário! '''
print("Olá")
~~~

# Tipos em Python (I)

:::::{.columns}
::::{.column width=60%}
- **Tipagem dinâmica**: tipo é atribuído no momento da atribuição.
	- **Não há declaração de tipo!**
	- *Duck Typing: "If it walks like a duck and it quacks like a duck, then it must be a duck."*

~~~{#tipoDinamico .python}
a = 5			 # é inteiro
pi = 3.14		 # é float
c = "uma string" # é string
~~~

::::
::::{.column width=40%}

:::::::{.center}
![](img/duckTyping.jpeg){#id width=60%}
:::::::

::::
:::::

# Tipos em Python (II)

- **Tipagem forte**: não há coerção de tipos.
	- Tipo da variável se mantém.
	- Até que a atribuição ocorra novamente.
		- Nesse caso, o objeto da variável muda!
- No exemplo a seguir há um erro de tradução.
	- Erro na 3ª linha: `tempo` é do tipo int e não pode ser convertido para string.

~~~{#interpretacao .python}
tempo = 5
seg = "s"
print(tempo + seg)
~~~

# Módulos de Python

- Possui diversos módulos (bibliotecas):
    - coleção de objetos e funções já prontas.
    - Uso do comando `import` para incluir um módulo.
    - Por exemplo, para o módulo de matemática:

~~~{#exemploImport .python}
import math
~~~

# Constantes em Python

- Numéricas:
    - Inteiro (int)
        - Exemplos: 1, 43, -52, 2018, 364567
    - Real (float)
        - Uso de ponto ao invés de vírgula como separador decimal.
        - float vem de *floating point* (ponto flutuante).
        - Exemplos: 0.5, 3.1415..., 8.0, -1000.761, 79.0001
    - Complexo (complex)
        - Números Complexos.
        - Exemplos: 4+2j, 2.9+2.1j, -7.32+0.3j, 8-100j

# Constantes em Python (II)

:::::{.columns}
::::{.column width=60%}
- String (str)
    - Representa texto.
    - Entre aspas simples ou duplas.
    - Exemplos: `"Olá"`, `"a"`, `'Bom dia!'`.
    - Para incluir as aspas no texto:
        - `'Incluir "aspas duplas"'`
        - `"Incluir 'aspas simples'"`
    - Aspas triplas permite incluir texto com quebra de linha:
- Lógica (bool)
    - *bool* vem de booleano (Lógica de Boole)
    - Dois exemplos apenas: **True** e **False**
        - Primeira letra é maiúscula.
::::
::::{.column width=40%}
<br><br><br><br><br><br><br>

~~~{#id .python}
'''Texto com
quebra de linha'''```
~~~
::::

:::::

# O Comando Type

- Já vimos que não há declaração.
    - Antes de usar, deve-se apenas inicializar a variável.
    - *Duck typing*!
- Exemplo:
    - `x = 3.2`
    - O tipo de x será *float*.
- Experimente no console:
    - Associe um valor a uma variável x;
    - Execute o comando `type(x)` para ver qual é o tipo.


# Console do Interpretador de Python

- Digitar um comando por vez.
    - *Script*: interpretação por comando.
    - A cada *enter*, o resultado da operação (se houver) é mostrado.
- Útil para testar pequenos algoritmos.
- Experimente usar o comando `type` para indicar qual é o tipo de uma constante:
    - `type(16)`
    - `type(3.1415)`
    - `type('A')`
    - `type(True)`
- Note que o resultado aparece logo abaixo.

# Comando de Impressão em Python

- Comando: `print`
- Permite imprimir um objeto Python.
    - Constantes, resultados de expressões, variáveis ...
- Local de impressão:
    - Na saída padrão, que geralmente é no *console*.
- Exemplo:

~~~{#exemplo .python}
print("Olá mundo")
~~~

# Exercício I

- No console, experimente imprimir as constantes:
	a) 16 (tipo inteiro)
	b) 3.1415 (tipo float)
	c) A
	d) Um exemplo de texto.
	e) Exemplo de texto com "aspas duplas" aparecendo.
	f) Exemplo de texto com 'aspas simples' aparecendo.
	g) Era uma vez...<br>
	Um texto com quebra de linha.
	h) True (tipo booleano)

# Expressões Aritméticas em Python

- Alguns operadores parecidos com os da matemática.

Operação |	Operador | Exemplo  | Resultado
---------|-----------|----------|----------
adição 	 | +         |`5+2`     | 7
subtração| -         |`5-2`     | 3
multiplicação |	*    |`5*2`     | 10
divisão  |	/        |`5/2`     | 2.5
exponenciação |**    |`5**2`    | 25
divisão inteira |//  |`5//2`    | 2
módulo (resto)| %    |`5%2`     | 1

# Precedências dos Operadores

- Maior: Parênteses ()
- Depois: ** (exponenciação)
- Depois: sinal -
- Depois: * (multiplicação), / (divisão), // (divisão inteira), % (resto)
- Por último: + (adição), - (subtração)

# Exercício II

## Testar no console as expressões:
- `5 + 2`
- `39/6`
- `39//6`
- `3**3`
- `(5+2) % 3`
- `(5-1)/2**2-4/2*(5-1)+1`

No PyCharm: View > Tools Windows > Python Console

# Variáveis em Python

- Guardam valores na memória do computador.
- Precisa de um identificador (nome) para indicar posição de memória no código.
    - Nome é formado por combinações de qualquer letra, número e "_".
    - Não pode começar por número e não pode ser uma palavra reservada.
    - Nome é *case sensitive*: diferencia letras maiúsculas de minúsculas.
    - Exemplos válidos:
        - x, X, x2, minha_variavel, PI
    - Exemplos não válidos:
        - 1x, +, !, x.y
- **Atribuição** de valor é feita pelo sinal "="
    - Exemplo: `x = 4`

# Palavras Reservadas em Python

- Como o nome já diz, são **reservadas** para a linguagem.
    - Não podem ser usadas para nomear variáveis!

<table style="width:90%">
<tr>
<td>and</td>  <td> as </td>  <td> assert </td>  <td> break </td>  <td> class </td>  <td> continue </td>
</tr>
<tr>
<td>def</td>  <td>del</td>  <td>elif</td>  <td>else</td>  <td>except</td>  <td>exec </td>
</tr>
<tr>
<td>finally </td>  <td>for</td>  <td>from</td>  <td>global</td>  <td>if</td>  <td>import </td>
</tr>
<tr>
<td>in</td>  <td>is</td>  <td>lambda</td>  <td>nonlocal </td>  <td>not </td>  <td>or  </td>
</tr>
<tr>
<td>pass </td>  <td>raise </td>  <td>return </td>  <td>try</td>  <td>while</td>  <td>with </td>
</tr>
<tr>
<td>yield</td>  <td>True</td>  <td>False</td>  <td>	None</td>  <td></td>  <td></td>
</tr>
</table>



# Exercícios III

- No console, reporte o que acontece para cada comando abaixo executado na ordem especificada:
	1. `1x = 3`
	1. `A = 3.4`
	1. `type(A)`
	1. `A = "3.4"`
	1. `type(A)`
	1. `B = 1.2`
	1. `A + B`

# Obtendo Dados do Usuário em Python

- Comando chama-se `input`
- Exemplo de uso:

```Python
    texto = input("Entre com um texto: ")
```

# Obtendo Dados do Usuário em Python (II)


- Note que input é um função que retorna sempre uma string.
- Se quiser obter um inteiro, por exemplo, deve-se converter explicitamente:

~~~{#inputInt .python}
numero = int(input("Entre com um número: "))
~~~

- Exemplo para obter real:

~~~{#inputFloat .python}
numero = float(input("Entre com um número: "))
~~~


# Obtendo Dados do Usuário em Python

- E se usuário entrar com um texto quando é pedido um número, por exemplo?
    - Ocorrerá um erro de execução!
- Exemplo:
    <pre style="font-size:20px; font-family: 'Roboto', Roboto, mono;">
    >>> numero = int(input("Entre com um número: "))
    Entre com um número: a
    </pre>
    <pre style="font-size:20px; font-family: 'Roboto', Roboto, mono; color:red;">
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'a'
    </pre>
- É bom e é possível evitar!
    - Veremos como fazer isso em aulas futuras...
    - Por enquanto, supor que usuário vai digitar valores nos tipos esperados!

# Exercícios IV

## Escreva os seguintes programas em Python:

1. Escreva um programa que leia 3 notas de um aluno e calcule a média com os seguintes pesos: 1 para a primeira nota, 2 para a segunda e 3 para a terceira.
2. Escreva um programa que leia uma temperatura em graus Fahrenheit e converta para
graus Celsius, cuja fórmula de conversão é: $$(Fahrenheit - 32) \times \frac{5}{9}$$

- Lista online: <a href="https://wiki.python.org.br/EstruturaSequencial" target="_blank"> https://wiki.python.org.br/EstruturaSequencial</a>.

