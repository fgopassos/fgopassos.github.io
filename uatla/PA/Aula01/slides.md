---
author: Fernanda Passos
note: Programação Avançada
date: 
subtitle: Aula 01 
title: Introdução ao Curso
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---

# Estrutura da Unidade Curricular

- Nome: Programação avançada.
- Foco em programação em redes e de sistemas.
- Objetivos:
	1. Compreender os conceitos de arquitetura cliente-servidor, para a par (P2P)  e híbridas.
	2. Desenvolver aplicações cliente-servidor  web.
	3. Desenvolver a capacidade de implementação de serviços web na nuvem.
	4. Desenvolver programas de computadores em qualquer tipo de arquitetura de redes utilizando *sockets* UDP e TCP.
	5. Compreender os princípios de concorrência e paralelismo computacional.
	6. Desenvolver programas paralelos multiprocessados.

# Informações Gerais

::::::{.block .centered}
:::{.blocktitle}
Horário e Sala
:::
- Dois dias:
	- Segundas de 20:30h às 22:30h
	- Terças de 20:30h às 22:30h (nos dias de 12/10 a 31/11)
- Sala: Lab 3
::::::

::::::{.block .centered}
:::{.blocktitle}
Contato
:::
* fpassos@uatlantica.pt
* Moodle:
  * Calendário.
  * Material didático e Listas de Exercícios.
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
- Arquiteturas P2P e Híbridas
- Programação em Sockets (UDP e TCP)
- Princípios de Programação Concorrente e Paralela


# Ferramentas de Aprendizado

- Utilizaremos a linguagem de programação Python 3.
	- Seu funcionamento, elementos sintáticos e estruturas de dados serão introduzidos.
- Framework de desenvolvimento Flask: para aplicações Web.
	- Cliente com HTML5, CSS e JavaScript.
	- Servidor com Python.
- Nuvem da Azure.
	- Como incluir uma aplicação web operacional na nuvem.
- Programação paralela em Python pelas bibliotecas *multithreading* e *multiprocessing*.
	- Diferença entre ambas.
	- Desempenho.
- Programação com *sockets* em Python.
	- Arquiteturas P2P e híbridas.

# Material de Apoio (I)

::::::{.block .centered}
:::{.blocktitle}
Livros:
:::
- Menezes, N. N. C. (2019). *Introdução à programação com Python: Algoritmos e lógica de programação para iniciantes.* Edição 3. Novatec.
- Kurose, J. F., and Ross, K. W. (2017). *Redes de Computadores, Uma Abordagem Top-Down.* Edição 7. Pearson.
- Grinberg, M. (2018). *Flask web development: developing web applications with Python.*  O'Reilly Media, Inc.	
::::::

# Material de Apoio (II)

::::::{.block .centered}
:::{.blocktitle}
Links:
:::
- Pallets Organization. *Flask documentation*. Acessado em setembro de 2021. https://flask.palletsprojects.com/en/2.0.x/
- Microsoft. *Documentação do Serviço de Aplicações*. Acessado em setembro de 2021. https://docs.microsoft.com/pt-pt/azure/app-service/
- Python Software Foundation. *The Python Tutorial, 2021*. Acesso em setembro de 2021. https://docs.python.org/3/tutorial/
::::::


# Avaliação

* 3 trabalhos individuais de implementação.
	* T1: Programa paralelo e relatório de análise de desempenho.
	* T2: Desenvolvimento de aplicação par a par (P2P) ou híbrida usando sockets.
	* T3: Desenvolvimento de aplicação web simples usando Flask e na nuvem.
* Todos com apresentação do programa e resultados (20% da nota).
* Nota final: T1*20% + T2*40% + T3*40%.
* Exame Final:
	* Em caso da nota final abaixo de 50%.

# Visão Geral do Curso

- Atualmente, existem diversas formas de programação.
	- Várias linguagens,
	- vários *frameworks* de desenvolvimento, ...
- Programação na Web é fundamental!
	- Há diversos *frameworks* que facilitam!
	- JavaScript no lado cliente e Python no lado servidor.
	- Python é uma linguagem de programação com muitos recursos!
- Programação paralela:
	- como desenvolver programas *multithreading*?
	- e multiprocessados?

# Visão Geral do Curso (II)

- Programação de outras aplicações em redes.
	- Desenvolver programas na rede (uso de *sockets*);
		- Mais genérico!
		- Podemos programar qualquer coisa em redes!
	- Internet das coisas: programação de dispositivos ubíquos conectados;
	- ...
- Como podemos explorar as nuvens de computadores?
	- Quais são as plataformas e o que podemos fazer?
	- Tema relevante: iremos criar aplicações Web rodando na nuvem.

# Introdução ao Python{.part}

# Surgimento da Linguagem Python

- Criada por Guido Van Rossum em 1989.
	- No Instituto de Pesquisa Nacional para Matemática e Ciência da Computação (CWI).
	- Lançada em 1991.
- Versões 1, 2 (em 2000) e 3 (em 2008).
- Projetada para diminuir o esforço de programação.
	- Prioriza legibilidade, velocidade (?).
	- Mais produtiva.
- Origem do nome em homenagem ao grupo humorístico britânico *Monty Python*.

# Características da Linguagem Python

:::::{.columns}
::::{.column width=70%}
- Interpretada: trechos de códigos são traduzidos por vez.
- Multiparadigma:
	- Imperativa: comandos são ações.
	- Orientada a objetos: abstração de dados.
	- Programação concorrente e paralela.
	- Programação funcional: notação *lambda*.
- Tipagem dinâmica e forte:
	- Não há declaração e tipo de variáveis é definido em tempo de execução.
	- *Duck typing: "If it walks like a duck and it quacks like a duck, then it must be a duck."*
	- É forte porque exige tipo do valor igual ao tipo da variável.
::::
::::{.column width=30%}
:::::::{.center}
<br><br><br>
![](img/Python_logo.svg){#id width=80%}
:::::::
::::
:::::

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

- **Versão 2:**
    - Ainda usada, pois existem programas escritos nela!
- **Versão 3:**
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
	- <a href="https://www.python.org/downloads/" target="_blank"> Instalador do Python 3</a>.
	- Escreve código diretamente nele ou executa em linha de comando.
	- No Windows, é instalado o interpretador IDLE (*prompt*).
	- Sugestão de editor de código: <a href="https://code.visualstudio.com" target="_blank"> Visual Studio Code</a>.
- Uso de IDE (Ambiente de Desenvolvimento Integrado):
	- Editor de texto com interpretador embutido, além de outras ferramentas.
	- <a href="https://www.jetbrains.com/pycharm-edu/" target="_blank">PyCharm Edu</a> é um exemplo.
- O aluno pode escolher o que achar melhor.

# Escrevendo o Primeiro Programa

- O famoso *Olá mundo!*:

~~~{#primeiroProg .python}
print('Olá mundo!')
~~~

- Muito simples: apenas uma linha de código!
- Duas formas de executar:
	- No interpretador.
	- Gerando um documento **.py** e executando em linha de comando.
		- `python3 meuPrograma.py`

# Atividade

- Preparar ambiente de desenvolvimento.
- Duas opções (pelo menos):
	1) python 3 + Visual Studio Code.
	2) IDE PyCharm.