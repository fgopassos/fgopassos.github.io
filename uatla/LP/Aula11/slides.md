---
author: Fernanda Passos
note: Linguagem de Programação
date:
subtitle: Aula 11
title: Programação Concorrente em Python
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Paradigma Concorrente

- Estruturar o programa em um conjunto de unidades concorrente.
    - Partes do programa concorrem por recursos de processamento (memória, CPU, ...).
- Concorrente *versus* Paralelo:
    - Concorrente: partes do programa executam concorrendo por recursos;
        - Quando não há recursos disponíveis simultaneamente.
        - Sistema operativo executa as partes com a técnica de preempção temporal.
    - Paralelo: partes do programa executam ao mesmo tempo.
        - Neste caso, há recursos disponíveis para isso.
        - Por exemplo, através de multiprocessamento (*e.g.*, múltiplos núcleos de CPU).

# Programação Concorrente: Threads e Processos
::::::{.block .centered}
:::{.blocktitle}
Definações:
:::
- Uma thread é um fluxo de controle sequencial dentro de um programa em execução (processo).
    - Um processo é formado por uma ou mais threads.
::::::

:::::{.columns}
::::{.column width=50%}
:::::::{.center}
![](imagens/thread1.png){#thread1 width=50%}
:::::::
::::
::::{.column width=50%}
:::::::{.center}
![](imagens/thread2.png){#thread2 width=65%}
:::::::
::::
:::::


# Multithreading

- Uma aplicação que usa múltiplas threads é chamada de **multithreading**.
- Um sistema de threads mantém a **mínima informação** para que permita que a CPU possa ser compartilhada por vários threads.
    - Contexto de thread.
- No conceito de *multithreading*, um processo pode possuir vários fluxos de controle (threads).
- Threads de um processo partilham o mesmo espaço de endereçamento.
    - **Memória partilhada**.
- Trocas de contexto de threads de um mesmo processo são mais rápidas.
    - Comparado ao processo.

# Multiprocessamento

- Aplicação que usa múltiplos processos.
- Processos são partes de um programa *isolados*.
    - Por definição, **não partilham memória** entre si.
    - Embora existam chamadas de sistema para tal propósito.
    - S.O. demora mais para criar um processo, comparado a threads.
    - Contexto de processos é maior e troca é mais cara.
- Uma aplicação multiprocessada pode explorar múltiplos computadores.
    - Necessária a **comunicação** entre computadores (redes).
    - Necessário escalonamento nas múltiplas máquinas.
    - Possibilidade de **aumentar a escala**!
        - Apenas com threads, isto não é possível pois elas dependem de existir um processo.

# Multithreading vs. Multiprocessamento

:::::{.columns}
::::{.column width=49%}
## Prós:

- Menos tempo para criar um thread do que um processo filho.
- Menos tempo para finalizar um thread do que um processo.
- A troca de contexto é mais rápida entre threads do mesmo processo.
- Mais eficiência no compartilhamento de dados através da memória compartilhada dentro de um mesmo processo.

::::
::::{.column width=49%}

## Contras:

- Menos proteção da área de memória entre os threads.
    - Por padrão, processos não têm acesso a área de memória de outros.
- Programador deve proteger dados que não podem ser manipulados simultaneamente.
    - Esforço de programação.
- Por definição, threads de um mesmo processo não podem executar em máquinas diferentes.
::::
::::{.column width=2%}
::::
:::::

# Exemplos Reais de Uso de Threads

- Navegador Web
    - Um thread para exibir imagens ou texto.
    - Outro thread para recuperar dados da rede.
- Processador de textos
    - Um thread para exibir gráficos/reformatar um texto.
    - Outro para ler sequência de teclas do usuário.
    - Outro para verificação ortográfica e gramatical.
    - Outro para salvamento automático.
- Servidores com threads.
- ...

# Exemplos Reais: Servidor com Threads

:::::{.columns}
::::{.column width=50%}
- Facilita implementação.
- Explora paralelismo.
    - Real (sistema multinúcleos) ou
    - Aproveitamento de ociosidade de CPU.
        - Devido a acesso a disco, por exemplo.
- Servidor faz chamadas de sistema bloqueantes.
    - Mas apenas a thread que fez a chamada é bloqueado.
    - Outras threads continuam executando.
::::
::::{.column width=50%}
![](imagens/threadsServidor.svg){#threadsServidor width=80%}
::::
:::::

# Exemplo de um Programa com Threads

- Objetivo do programa é contar o número de palavras em um ficheiro.
- Podemos dividir o ficheiro em N partes.
- Atribuímos cada parte para uma contagem por uma thread.
- Se as threads executam em paralelo, tempo de processamento tende a reduzir.
- Reduzir para quanto?
    - Ideal é reduzir em N.
    - Mas pode ser maior devido à sobrecargas.

# Multithreading em Python 3

:::::{.columns}
::::{.column width=50%}
- Módulo é chamado **multithreading**.
    - `import multithreading`
- Thread é criada com uma função associada.
    - Tal função é o código que o thread irá executar.
    - Pode ter qualquer nome.
    - Deve ser implementada.
    - Aceita parâmetros.
    - Apresenta seu próprio escopo (local) e pode acessar escopo global.
::::
::::{.column width=50%}
![](imagens/escopoThread.png){#escopo width=80%}
::::
:::::

# Thread em Python: Definir

~~~{#thread .python style="font-size: 20pt;"}
import threading

# Função que a thread irá executar.
def meu_thread():
    print('Sou um thread')

# Thread (processo) principal irá criar 5 threads.
for i in range(5):
    # Cria thread.
    t = threading.Thread(target=meu_thread)
    # Inicia execução do thread.
    t.start()
~~~

# Thread em Python: Identificar

~~~{#threadsId .python style="font-size: 20pt;"}
import threading

# Função que a thread irá executar.
def meu_thread(id):
    print('Sou um thread de id', id)

# Thread (processo) principal irá criar 5 threads.
for i in range(5):
    # Cria thread com argumento i para identificar.
    t = threading.Thread(target=meu_thread, args=(i,))
    # Inicia execução do thread.
    t.start()
~~~

# Thread em Python: Esperar Término

:::::{.columns}
::::{.column width=40%}
- Programa principal pode esperar pelo término de um thread.
    - Geralmente é uma boa prática!
    - Muitas vezes é necessário!
- Uso do método join() de uma thread.
::::
::::{.column width=60%}

~~~{#threadsJoin .python style="font-size: 18pt;"}
# ...
# Programa principal
t_lista = []
for i in range(5):
    t = threading.Thread(target=meu_thread, args=(i,))
    t.start()
    # Guarda objeto da thread criada.
    t_lista.append(t)

# Espera todos os threads.
for thread in t_lista:
    thread.join()

print("Todos as threads terminaram")
~~~

::::
:::::

# Exercício I

**Objetivo**: Implementar um programa concorrente, com duas threads (além do thread principal), para incrementar de 1 cada elemento de um vetor de N elementos.

1. Inicializar o vetor no thread principal e imprimir seus valores iniciais.
2. Distribuir trabalho entre os threads para incremento dos dados do vetor.
    - Pode ser simplesmente um if (são 2 threads apenas).
3. Imprimir os valores atualizados do vetor no thread principal.

# Exercício II

**Objetivo**: Implementar um programa concorrente, com T threads (além do thread principal), para incrementar de 1 cada elemento de um vetor de N elementos.

1. Inicializar o vetor no thread principal e imprimir seus valores iniciais.
2. Distribuir trabalho entre os threads para incremento dos dados do vetor.
3. Imprimir os valores atualizados do vetor no thread principal.

Como dividir as tarefas entre as threads?

# Dica para Exercício II

- Exemplo com N=15 e T=4.

::::{.center}
![](imagens/dicaThread.png){#escopo width=90%}
::::

