---
author:
- |
  Fernanda Passos \<nandagooliveira\@gmail.com\>\
  \
  Baseado nos slides da profa. Laura Assis -- CEFET-RJ Petrópolis
date: 04 de Agosto de 2015
title: Linguagem de Programação
---

# Introdução à Programação Orientada a Objetos (POO)

-   Paradigma de linguagens de programação imperativo.

    -   A linguagem expressa uma sequência de comandos.

-   Uma **evolução do paradigma estruturado** para se trabalhar com
    dados.

-   Introduz a noção de **objetos** e **classes**.

    -   Veremos com mais detalhes a seguir.

# Programação Estruturada

-   Também é um paradigma de linguagens de programação imperativo.

-   Prévio ao paradigma de orientação a objetos.

-   Faz uso das estruturas:

    -   **sequência**,
    -   **seleção** e
    -   **repetição**.

-   Faz uso também de **procedimentos**: abstração de controle.

# Programação Estruturada (II)

::::{.center}

![](img/estruturado.png){width="75%"}

::::

# O Que São Objetos?

- []{.listTable align=lr}
-   No mundo real, tudo aquilo que podemos dar um nome é objeto.
-   Objetos do mundo real: carro, cachorro, mesa, televisão, bicicleta,
    professor, aluno.

<!-- -->

- []{.listTable align=lr}
-   No mundo real, tudo aquilo que podemos dar um nome é objeto.
-   Objetos do mundo real: carro, cachorro, mesa, televisão, bicicleta,

<!-- -->

-   Esses objetos tem duas características básicas:
    -   estado e
    -   comportamento.
-   Identificar o estado e o comportamento dos objetos é a melhor
    maneira para começar a pensar em POO.

# Teste (Apagar!!!!)

:::{.center}

- []{.listTable align=lrc}
- [Atributo]{.listTableRight}
    - Preço
    - [ID]{.multicol cols=2}
    - Quantidade
- [Valor]{.listTableLeft .multicol cols=2}
    - R$ 30,00
    - 
    - 500
- 
    - [qweqwe]{.multirow rows=3}
    - 
- 

:::

# Objeto do Mundo Real

:::::{.block .centered}

:::::::{.blocktitle}

Objeto: um cão

:::::::

::::{.center}

![](img/objeto_cao.png){width="100%"}

::::

[Fonte: Aulas do professor Fábio Usberti -- IC -- Unicamp.]{.footnotesize}

:::::

# Objeto do Mundo Real (II)

:::::{.block .centered}

:::::::{.blocktitle}

Objeto: uma bicicleta

:::::::

::::{.center}

![](img/objeto_bicicleta.png){width="100%"}

::::

[Fonte: Aulas do professor Fábio Usberti -- IC --
Unicamp.]{.footnotesize}

:::::

# Exemplos de Objetos

::::{.center}

  **Objetos**             **Não-objetos**
  ----------------------- -----------------------------
  Caneta                  40% da caneta
  Teclado de computador   O ar envolta do computador
  Sapato                  A cor ou material do sapato
  Mouse                   O som do clique do mouse

::::

-   O que os objetos têm em comum?

# Características de Objetos

-   Um objeto concreto é feito de algum **material**.

    -   Uma caneta é feita de plástico, metal, tinta, ...
    -   Existem ainda objetos abstratos, como uma conta bancária.

-   Um objeto se **mantém unido** como um todo.

    -   Caneta é um todo e não corresponde a partes dela.

-   Um objeto possui **propriedades**.

    -   Cor da caneta, localização, a espessura que escreve, ...

-   Um objeto pode **fazer coisas** e pode ter as **coisas sendo
    feitas** para ele.

# Características de Objetos (II)

-   As características de um objeto possuem nomes específicos:

    -   Um objeto tem **identidade**:

        -   cada objeto é um indivíduo distinto.

    -   Um objeto tem **estado**:

        -   várias propriedades que podem mudar.

    -   Um objeto tem **comportamento**:

        -   pode fazer coisas e ter coisas sendo feitas para o objeto.

# Definição de Objetos

-   De maneira geral definimos objetos como um **conjunto de variáveis e
    métodos**, que representam seus **estados** e **comportamentos**;
-   Tudo que um objeto possui (**estados**) e tudo que ele pode fazer
    (**comportamento**) está contido no próprio objeto.
-   No exemplo da bicicleta tem-se métodos para mudar a marcha, a
    cadência, etc;
-   A utilização desses métodos **altera os valores do estado**.

# Definição de Objetos (II)

-   Objetos diferentes possuem complexidades diferentes.

-   [Lanterna:]{style="color: blue"}

    -   Estados: ligado, desligado;
    -   Comportamentos: ligar e desligar.

-   [Rádio:]{style="color: blue"}

    -   Estados: ligado, desligado, volume, estação;
    -   Comportamentos: ligar, desligar, aumentar volume, diminuir
        volume, procurar estação, sintonizar.

# Objetos de Software

-   Objetos do mundo real podem ser representados por programas de
    computador.

    -   Podemos chamar de [objetos de *software*]{style="color: blue"}.

    -   Exemplos:

        -   um livro (objeto concreto),
        -   uma conta bancária (objeto abstrato).

-   Objetos de *software* também possuem **identidades**, **estados** e
    **comportamentos**.

-   Um objeto de *software* armazena seu estado em
    [atributos]{style="color: blue"} (**variáveis**) e assumem
    comportamentos através de [métodos]{style="color: blue"}
    (**funções**).

# Objetos de Software (II)

-   Considere um objeto de **uma conta corrente** em um sistema
    bancário.
-   Através dos métodos pode-se realizar transações bancárias.
-   Além dos métodos responsáveis pelo serviço, o objeto deve conter
    dados.

::::{.center}

![](img/objeto_software.png){width="60%"}

::::

Fonte: *Programação Básica em Java*, Apostila de Patrícia Augustin
Jaques. Disponível em:
<http://professor.unisinos.br/pjaques/papers/Programacao%20Basica%20em%20Java_homepage.pdf>.
Acessado em Julho de 2015

# Exercício 1

1.  Defina atributos e métodos para os seguintes objetos do mundo real:

    a)  escada,
    b)  livro.

2.  Defina atributos e métodos para os seguintes objetos de *software*:

    a)  correio eletrônico,
    b)  arquivo de música.

# Exercício 1: Respostas

1.  a)  escada:

        -   Atributos: número de degraus, peso, altura, distância entre
            degraus.
        -   Métodos: subirDegrau(), descerDegrau().

    b)  livro:

        -   Atributos: título, autor, editora, número de páginas,
            dimensões, peso, número de capítulos, capítulos.
        -   Métodos: abrir(), fechar(), irParaPagina(numeroPagina),
            irParaCapitulo(numeroCapitulo).

2.  a)  correio eletrônico:

        -   Atributos: nome, número de emails, emails lidos, emails não
            lidos, contatos.
        -   Métodos: checar(), enviar(contato, mensagem),
            apagarEmail(id).

    b)  arquivo de música:

        -   Atributos: título, autor, tempo de duração.
        -   Métodos: tocar(), pausar(), parar(), irParaTempo(tempo).

# Relacionamento entre Objetos

-   Um objeto sozinho não é muito útil.

-   Em um programa orientado a objetos temos muitos **objetos se
    relacionando entre si**.

-   Os **métodos** de um objeto operam sobre seu estado interno e são os
    principais mecanismos de **intercomunicação entre objetos**.

-   A interação entre objetos é feita através dos métodos.

-   **Um objeto chama os métodos do outros objetos** para interagir com
    eles.

-   Os métodos podem permitir **passagem de informação** para outro
    objeto.

    -   **Passagem de parâmetros**.

# Componentes para Interação entre Objeto

-   Existem três componentes que fazem parte da interação entre objetos:

    -   O **objeto** para o qual a mensagem é dirigida.

        -   Exemplo: uma bicicleta.

    -   Um **método** a ser executado.

        -   Exemplo: `mudaMarcha()`.

    -   **Parâmetros** necessários para execução do método.

        -   Exemplo: `mudaMarcha(1)`.

# Encapsulamento de Objetos

-   Outra **característica** de POO.
-   [Encapsulamento]{style="color: blue"}: refere à possibilidade de
    **esconder** o estado interno de um objeto e **obrigar** que todas
    as interações com um objeto sejam realizadas por métodos.

::::{.center}

  -------------------------------------------- ------------------------------------------------------
   ![](img/objeto_conceito.png){width="40%"}   ![](img/objeto_conceito_bicicleta.png){width="30%"}
  -------------------------------------------- ------------------------------------------------------

::::

[Fonte:
[http://docs.oracle.com/javase/tutorial/java/concepts/object.html]](http://docs.oracle.com/javase/tutorial/java/concepts/object.html]@){.footnotesize}

# Programação Orientada a Objetos

:::::{.block .centered}

:::::::{.blocktitle}

Uma definição:

:::::::

A programação orientada a objetos consiste em considerar os sistemas
computacionais como um conjunto de objetos que interagem entre si de
maneira organizada para resolver um problema.

:::::

# Programação Orientada a Objetos (II)

-   Um programa orientado a objetos é estruturado como uma comunidade de
    **agentes que interagem entre si**, denominados
    [objetos]{style="color: blue"}.
-   Cada objeto tem um papel a cumprir.
-   Cada objeto oferece um **serviço** ou **realiza uma ação** que é
    usada por outros membros da comunidade.

# Programação Orientada a Objetos (III)

-   As etapas fundamentais do projeto de um *software* orientado a
    objetos são:

    1.  analisar os **requisitos** que descrevem o sistema desejado;
    2.  determinar os **objetos** necessários para implementar o
        sistema;
    3.  determinar os **atributos** de cada objeto;
    4.  determinar os **comportamentos** que os objetos exibirão;
    5.  especificar como ocorre a **interação entre os objetos** para
        atender aos requisitos do sistema.

# Exercício 2

-   Considere o sistema onde uma pessoa anda de bicicleta.

-   Estabeleça:

    1.  os requisitos do sistema,
    2.  os principais objetos,
    3.  os atributos de cada objeto,
    4.  os comportamentos (métodos) de cada objeto,
    5.  a relação de interação entre os objetos.

# Exercício 2: Resposta

1.  Requisitos:

    -   a pessoa deve subir em uma bicicleta, colocar os pés nos pedais,
        segurar o guidão, escolher a cadência e a marcha, começar a
        pedalar, se equilibrar e frear quando quiser parar.

2.  os principais objetos:

    -   pessoa e bicicleta.

3.  os atributos de cada objeto,

    -   pessoa: nome, sobrenome, altura, peso, data de nascimento.
    -   bicicleta: cor, tamanho, numero de marchas, marcha, velocidade.

4.  os comportamentos (métodos) de cada objeto:

    -   pessoa: obter Nome, obter Sobrenome, calcular Idade(data).
    -   bicicleta: acelerar, mudar marchar, mudar cadencia, frear.

5.  a relação de interação entre os objetos:

    -   pessoa sobe na bicicleta, pessoa pedala, pessoa escolhe marcha,
        pessoa escolhe cadência, pessoa muda velocidade, pessoa vira
        guidão, pessoa frea.

# Objetos e Classes

-   Objetos apresentam:

    -   identidade,
    -   estado e
    -   comportamento.

-   Objetos são compostos de:

    -   atributos: propriedades que possuem valores.
    -   métodos: são procedimentos ou funções que realizam as ações
        próprias do objeto.

# Exemplos de Objetos

::::::{.columns}

:::{.column width="50%"}
 ![](img/beagle.jpg){width="40%"}

  [Atributos]{.multicol cols=2}   
  ----------------------------------- --------
  Nome:                               Cacau
  Raça:                               Beagle
  Gênero:                             Fêmea
  Peso:                               12kg
  [Métodos]{.multicol cols=2}     
  [Latir]{.multicol cols=2}       
  [Deitar]{.multicol cols=2}      
  [Farejar]{.multicol cols=2}     
  [Comer]{.multicol cols=2}       

:::

:::{.column width="50%"}
 ![](img/schnauzer.jpg){width="40%"}

  [Atributos]{.multicol cols=2}   
  ----------------------------------- -----------
  Nome:                               Pluto
  Raça:                               Schnauzer
  Gênero:                             Macho
  Peso:                               10kg
  [Métodos]{.multicol cols=2}     
  [Latir]{.multicol cols=2}       
  [Deitar]{.multicol cols=2}      
  [Farejar]{.multicol cols=2}     
  [Comer]{.multicol cols=2}       

:::

::::::

# Exemplos de Objetos (II)

::::::{.columns}

:::{.column width="50%"}
 ![](img/persa.jpg){width="40%"}

  [Atributos]{.multicol cols=2}   
  ----------------------------------- -------
  Nome:                               Liz
  Raça:                               Persa
  Gênero:                             Fêmea
  Peso:                               5kg
  [Métodos]{.multicol cols=2}     
  [Miar]{.multicol cols=2}        
  [Deitar]{.multicol cols=2}      
  [Ronronar]{.multicol cols=2}    
  [Comer]{.multicol cols=2}       

:::

:::{.column width="50%"}
 ![](img/siames.jpg){width="35%"}

  [Atributos]{.multicol cols=2}   
  ----------------------------------- --------
  Nome:                               Félix
  Raça:                               Siamês
  Gênero:                             Macho
  Peso:                               4kg
  [Métodos]{.multicol cols=2}     
  [Miar]{.multicol cols=2}        
  [Deitar]{.multicol cols=2}      
  [Ronronar]{.multicol cols=2}    
  [Comer]{.multicol cols=2}       

:::

::::::

# Classes

:::::{.block .centered}

:::::::{.blocktitle}

Classe:

:::::::

Representa um conjunto de objetos que possuem características e
comportamentos comuns.

:::::

-   Um **objeto** é uma **instância** de uma **classe**.

-   A classe engloba vários objetos que pertencem a ela.

-   Por exemplo:

    -   A classe **cães** engloba os objetos cães de nome "Cacau" e
        "Pluto".

-   Note que os dois objetos possuem os mesmos atributos e métodos.

-   Descrevemos a **classe** baseada no estado e comportamento de seus
    objetos.

# Exemplo de Classe

::::{.center}

![](img/classeCao.svg){width="55%"}\
Classe Cão.

::::

# Classes e Objetos

::::::{.columns}

:::{.column width="42%"}


-   Uma classe representa um gabarito para os objetos e
-   descreve como estes objetos estão estruturados internamente.

:::

:::{.column width="58%"}


::::{.center}

![](img/ClasseObjeto.jpg){width="90%"}

::::

:::

::::::

# Subclasses e Superclasses

-   Classe cães e gatos tem em comum:

    -   Os atributos e alguns métodos como deitar e comer.

-   Podemos criar uma classe mamífero para agrupar as classes cães e
    gatos.

    -   Nesse caso, mamífero é uma **superclasse**.
    -   Nesse caso, cães e gatos são **subclasses** de mamífero.

-   Superclasse agrupa subclasses.

-   Subclasses pertencem a uma superclasse.

# Exemplo de Subclasses e Superclasse

::::{.center}

![](img/superclasse.svg){width="80%"}

::::

# Hierarquia de Classes

::::::{.columns}

:::{.column width="30%"}


-   Subclasses e superclasses formam uma **hierarquia de classes**.

:::

:::{.column width="70%"}
 ![](img/hierarquiaClasses.png){width="90%"}

:::

::::::

# Herança

-   Subclasses descendem de sua superclasse.

    -   As superclasses são chamadas "ancestrais" de cada subclasse.
    -   Exemplo: a superclasse mamífero é ancestral da subclasse gatos.

-   Subclasses **herdam** atributos e métodos de seus ancestrais.

    -   A classe cães herda os métodos "sentar" e "amamentar" de
        mamíferos e também os métodos "comer" e "dormir" de animais.
    -   A classe cães também herda os atributos "cor de pelos" e
        "comprimento dos pelos" da classe mamíferos e "nome", "idade",
        "peso" e "cor dos olhos" da classe animais.

# Herança (II)

-   Um dos conceitos mais interessantes na POO é a **reutilização** de
    código.

    -   Mas o programador deve conseguir mais do que simplesmente copiar
        e alterar códigos já prontos.

-   O programador deve ser capaz de **criar uma nova classe usando outra
    classe já existente**.

-   A herança ocorre quando se deseja utilizar o objeto existente para
    criar uma versão mais especializada deste objeto.

-   Particularmente em Java, uma classe pode ter uma única superclasse
    (imediata) e cada superclasse pode ter um número indefinido de
    subclasses.

# Exemplo de Herança

-   Suponha que uma concessionária de veículos venda apenas carros e
    motos.

-   Vamos criar a classe [veículos]{style="color: blue"}:

    -   possui os atributos: Motor, preço, marca, nome do comprador,
        quantos quilômetros fazem com 1 litro de combustível.
    -   possui os métodos: atualizaPreço(), insereComprador().

-   Precisamos de dois tipos especiais do objeto:
    [carros]{style="color: blue"} e [motos]{style="color: blue"}.

    -   Carros:

        -   Atributos (além): número de portas, banco de couro,
            ar-condicionado.
        -   Métodos (além): atualizaBancoCouro(),
            atualizaArCondicionado().

    -   Motos:

        -   Atributos: número de rodas, cilindrada.
        -   Sem métodos especializados.

# Exemplo de Herança (II)

-   Facilita utilizar a classe [veículos]{style="color: blue"} como um
    modelo.

    -   Podemos gerar as subclasses [carros]{style="color: blue"} e
        [motos]{style="color: blue"} usando a classe
        [veículos]{style="color: blue"}.

-   As classes [carros]{style="color: blue"} e
    [motos]{style="color: blue"} **herdam** todos os atributos e métodos
    da classe [veículos]{style="color: blue"}.

::::{.center}

![](img/exemploHeranca.svg){width="45%"}

::::

# Instanciação

-   As classes apenas definem os objetos.

-   Somente os **objetos** têm existência.

    -   Um objeto é uma **instância** de uma classe.

-   A classe serve de modelo para a criação de novos objetos.

::::{.center}

![](img/instancia.svg){width="50%"}

::::

# Exercício

-   Defina os objetos da classe veículo:

    -   Ferrari: um carro.
    -   Fusca: um carro.
    -   Kawasaki: uma moto.

-   Pode inventar os valores dos atributos.

-   Suponha que toda vez que um item do carro é alterado (por exemplo,
    inclusão de ar-condicionado), o preço aumenta ou diminui (remoção do
    item).

    -   Implemente, usando pseudo-código, os métodos atualizaPreço(),
        atualizaBancoCouro() e atualizaArCondicionado().
