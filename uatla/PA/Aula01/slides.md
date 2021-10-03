---
author: Fernanda Passos
note: Programação Avançada
date: 
subtitle: Aula 01 
title: Introdução
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Estrutura da Unidade Curricular

- Programação avançada.
- Objetivos:
	1. Compreender os conceitos de arquitectura cliente-servidor, para a par (P2P)  e híbridas.
	2. Desenvolver aplicações cliente-servidor  web.
	3. Desenvolver a capacidade de implementação de serviços web na nuvem.
	4. Desenvolver programas de computadores em qualquer tipo de arquitetura de redes utilizando sockets UDP e TCP.
	5.	Compreender os princípios de concorrência e paralelismo computacional.
	6. Desenvolver programas paralelos multiprocessados.

# Informações Gerais

::::::{.block .centered}
:::{.blocktitle}
Horário e Sala
:::
- Segundas de 20:30h às 22:30h
- Terças de 20:30h às 22:30h (apenas nos dias de 12/10 a 31/11)
- Lab 3
::::::

::::::{.block .centered}
:::{.blocktitle}
Contato
:::
* fpassos@uatlantica.pt
* Moodle:
  * Calendário.
  * Material didático.
  * Listas de Exercícios.
  * **Avisos**.
::::::

# Conteúdo Programático (I)

- A Linguagem Python 3
- Arquitetura Cliente-Servidor
- Revisão de conceitos de Web (HTTP, cookies)
- Desenvolvimento de aplicações web (HTML5, CSS, Javascript)
- Framework Flask


# Conteúdo Programático (II)

- Programação de serviços na nuvem (Flask na nuvem)
- Arquitecturas P2P e Híbridas
- Programação em Sockets (UDP e TCP)
- Princípios de Programação Concorrente e Paralela

# Material de Apoio

::::::{.block .centered}
:::{.blocktitle}
Livros:
:::
* Livro: Sebesta, R. W. (2018). *Conceitos de Linguagens de Programação.* Edição 11. Bookman Editora.
::::::

::::::{.block .centered}
:::{.blocktitle}
Links:
:::
  * Menezes, N. N. C. (2019). *Introdução à programação com Python: Algoritmos e lógica de programação para iniciantes.* Edição 3. Novatec.
  * Links na Internet: http://python.org.br
::::::


# Avaliação

* 
* Nota final: $\frac{T1 + T2}{2}$
* Exame Final:
	* Em caso da nota final abaixo de 50%.

# Visão Geral do Curso

- Atualmente, existem diversas formas de programação.
	- Várias linguagens,
	- vários frameworks de desenvolvimento, ...
- Programação na Web é fundamental!
	- Há diversos *frameworks* que facilitam!
- Programação de outras aplicações em redes.
	- Desenvolver programas na rede;
	- Internet das coisas: programação de dispositivos ubíquos conectados;
	- ...

# Visão Geral do Curso (II)

- Como podemos usar as nuvens de computadores?
	- Tema relevante.
	- Quais são as plataformas e o que podemos fazer?
- Programação paralela:
	- como desenvolver programas multithreading?
	- e multiprocessados?

# Introdução à Linguagem Python{.part}

# Surgimento da Linguagem Python

- Criada por Guido Van Rossum em 1989.
	- No Instituto de Pesquisa Nacional para Matemática e Ciência da Computação (CWI).
	- Lançada em 1991.
- Versões 1, 2 (em 2000) e 3 (em 2008).
	- Versões 2 e 3 não compatíveis.
- Projetada para diminuir o esforço de programação.
	- Prioriza legibilidade, velocidade (?).
	- Mais produtiva.
- Origem do nome em homenagem ao grupo humorístico britânico *Monty Python*.

# Uma Breve Descrição de Python

<a href="https://python.org/" target="_blank">.center[![:imageS width:40%;](imagens/Python_logo.svg)]</a>

- Linguagem de alto nível criada por Guido van Rossum em 1991.
- Características:
    - Interpretada: trechos de códigos são traduzidos por vez.
    - Imperativa: comandos são ações.
    - Suporta orientação a objetos: abstração de dados.
    - Tipagem dinâmica e forte:
        - Não há declaração e tipo de variáveis é definido em tempo de execução.
        - *Duck typing: "If it walks like a duck and it quacks like a duck, then it must be a duck."*
        - É forte porque exige tipo do valor igual ao tipo da variável.

# 

:::::{.columns}
::::{.column width=35%}
## Popularidade das Linguagens:
- Segundo índice TIOBE, setembro de 2021.
	- https://www.tiobe.com/tiobe-index/
::::
::::{.column width=65%}
:::::::{.center}
![](img/tiobe.png){#id width=80%}
:::::::
::::
:::::

# Versões da Linguagem Python

- .alert[Versão 2:]
    - Ainda usada, pois existem programas escritos nela!
- .alert[Versão 3:]
    - Mais usada atualmente.
    - **Iremos utilizá-la**.
- Versões 2 e 3 não são compatíveis!
    - São diferentes!
    - Atenção ao ver exemplos pela Internet.
    - Como diferenciar?
        - Existem várias maneiras e uma delas é pelo comando de print, se houver.
        - Python 2 usa `print "Olá."`
        - Python 3 usa `print ("Olá.")`


# Instalando Python 3

- Pode ser apenas instalado o interpretador de Python.
    - Escreve código diretamente nele ou executa em linha de comando.
    - No Windows, é instalado o interpretador IDLE (*prompt*).
- Uso de IDE (Ambiente de Desenvolvimento Integrado):
    - Editor de texto com interpretador embutido, além de outras ferramentas.
    - <a href="https://www.jetbrains.com/pycharm-edu/" target="_blank">PyCharm Edu</a> é um exemplo.
    - **Iremos utilizá-lo**.
    - Instalar: basta baixar e seguir os passos de instalação.

<a href="https://www.jetbrains.com/pycharm-edu" target="_blank">.center[![:imageS width:20%;](imagens/pycharm-edu_logo.png)]</a>

# Usando PyCharm Edu

- Escolha o modo "learner".
- Crie um projeto:
    - Sugestão de nome no lab: "Seu_nome".
    - Sugestão de nome em casa: "Aprendendo".
- File > New: escolha "Python File".
    - Dê um nome com final .py
    - .py é a extensão do arquivo em Python.
    - Cada programa fica em um arquivo ou conjunto deles.
- Experimente: digite no editor de texto:
    ```Python
    print("Meu primeiro programa em Python.")
    ```
    - Clique em ![:imageS width:2%;](imagens/play.png) para executar os comandos.
    - Saída do programa é exibida na caixa de texto abaixo.

# Usando PyCharm Edu

.center[![:imageS width:95%;](imagens/pycharm-edu_tela.png)]


# Introdução à Linguagem Python

- A linguagem Python possui sua sintaxe bem definida.
- Coisas em Python são referidas como .alert[objetos].
    - Constantes, variáveis, listas, tuplas, dicionários...
    - Veremos com detalhes cada um deles em aulas futuras.
- Possui diversos módulos (bibliotecas):
    - coleção de objetos e funções já prontas.
    - Uso do comando `import` para incluir um módulo.
    - Por exemplo, para matemática:
        ```Python
        import math
        ```

# Entendendo Erros em Python

- Qualquer interpretador de Python é capaz de acusar erros de sintaxe.
- Exemplo: suponha que você escreveu o seguinte código:
```Python
prit("Olá")
```
- Podemos perceber que o comando `print` está escrito errado.
- A mensagem de execução do comando será:

<pre class="nova" style="font-size:16px; font-family: 'Roboto', Roboto, mono; color:red;">
Traceback (most recent call last):
  File "C:/Users/Passos/PycharmProjects/Aprendendo/olaMundo.py", line 1, in ...
    prit("Olá Mundo!")
NameError: name 'prit' is not defined

Process finished with exit code 1
</pre>

# Comentários em Python

- Comentários em códigos são bem vindos!
    - São partes do código que serão ignoradas.
    - Servem para incluir alguma explicação do código.
- `#` é o caractere que define um comentário.
- Exemplo:
```Python
# Programa que imprime "Olá"
print("Olá") # Comentário pode ser usado aqui também!
```
- Comentário de bloco:
    - Texto entre `'''` e `'''`.
```
''' Programa que imprime "Olá".
    Este é um exemplo de mais de uma linha de comentário! '''
print("Olá")
```

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

- String (str)
    - Representa texto.
    - Entre aspas simples ou duplas.
    - Exemplos: `"Olá"`, `"a"`, `'Bom dia!'`.
    - Para incluir as aspas no texto:
        - `'Incluir "aspas duplas"'`
        - `"Incluir 'aspas simples'"`
    - Aspas triplas permite incluir texto com quebra de linha:
        ```
        '''Texto com
        quebra de linha'''```
- Lógica (bool)
    - *bool* vem de booleano (Lógica de Boole)
    - Dois exemplos apenas: **True** e **False**
        - Primeira letra é maiúscula

# Usando Console do PyCharm Edu

- View > Tools Windows > Python Console
- Serve para digitar um comando por vez.
    - Script: interpretação por comando.
    - A cada *enter*, o resultado da operação (se houver) é mostrado.
- Util para testar pequenos algoritmos.
- Experimente usar o comando type para indicar qual é o tipo de uma constante:
    - `type(16)`
    - `type(3.1415)`
    - `type('A')`
    - `type(True)`
- Repare que o resultado aparece logo abaixo.

# Comando de Impressão em Python

- Comando: `print`
- Permite imprimir um objeto Python.
    - Constantes, resultados de expressões, variáveis ...
- Imprime aonde?
    - Na saída padrão, que geralmente é o *console*.
- Exemplo:
    ```Python
        print("Olá mundo!")
    ```
![:imageS width:40%;](imagens/ex_print.png)

# Exercício I

#### No console do PyCharm, experimente imprimir as constantes:

- 16
- 3.1415
- A
- Um exemplo de texto.
- Exemplo de texto com "aspas duplas" aparecendo.
- Exemplo de texto com 'aspas simples' aparecendo.
- Era uma vez...<br>
Um texto com quebra de linha.
- True

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

#### Testar no console do PyCharm as expressões:
- `5 + 2`
- `39/6`
- `39//6`
- `3**3`
- `(5+2) % 3`
- `(5-1)/2**2-4/2*(5-1)+1`

Acesse no PyCharm: View > Tools Windows > Python Console

# Variáveis em Python

- Guardam valores na memória do computador.
- Precisa de um identificador (nome) para indicar posição de memória no código.
    - Nome é formado por combinações de qualquer letra, número e "_"
    - Não pode começar por número e não pode ser uma palavra reservada.
    - Nome é *case sensitive*: diferencia maiúscula de minúscula.
    - Exemplos válidos:
        - x, X, x2, minha_variavel, PI
    - Exemplos não válidos:
        - 1x, +, !, x.y
- .alert[**Atribuição**] de valor é feita pelo sinal "="
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

# Tipos de Variáveis em Python

- Não há declaração.
    - Antes de usar, deve-se apenas inicializar a variável.
- Um tipo é associado de acordo com o valor associado.
    - *Duck typing*!
- Exemplo:
    - `x = 3.2`
    - O tipo de x será *float*.
- Experimente no console do PyCharm:
    - Associe um valor a uma variável x;
    - Execute o comando `type(x)` para ver qual é o tipo.

# Exercícios III

#### No console do PyCharm, veja o que acontece para cada comando abaixo executado na ordem especificada:

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
- Note que input é um função que retorna sempre uma string.
- Se quiser obter um inteiro, por exemplo, deve-se converter explicitamente:
```Python
numero = int(input("Entre com um número: "))
```
- Exemplo para obter real:
```Python
numero = float(input("Entre com um número: "))
```

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

#### Escreva os seguintes programas em Python:

1. Escreva um programa que leia 3 notas de um aluno e calcule a média com os seguintes pesos: 1 para a primeira nota, 2 para a segunda e 3 para a terceira.
2. Escreva um programa que leia uma temperatura em graus Fahrenheit e converta para
graus Celsius, cuja fórmula de conversão é: $$(Fahrenheit - 32) \times \frac{5}{9}$$

- Lista online: https://wiki.python.org.br/EstruturaSequencial
- Use o Pycharm e crie seus códigos no editor de texto (sem usar o console).

