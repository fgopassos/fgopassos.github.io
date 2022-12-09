---
author: Fernanda Passos
subtitle: Linguagem de Programação
title: Javascript e *Document Object Model*
institute: Universidade Atlântica
logo: ../atlantica_logo2.svg
---


# Tags HTML {.part}


# Revisão de HTML: Estrutura de um Documento (I)

- No nível mais alto de abstração, documento HTML contém duas seções:
	- `head`: 
		- Metadados.
		- Configurações.
		- Definições gerais.
	- `body`:
		- O conteúdo textual propriamente dito.


```{.html .numberLines style="width: 40%; position: absolute; right: 60px; bottom: 80px; font-size: 80%;"}
<html>
	<head>
		...
	</head>

	<body>
		...
	</body>
</html>
```

# Revisão de HTML: Estrutura de um Documento (II)

:::::{.columns}
:::{.column width=60%}

- Documento organizado de forma hierárquica (em árvore).
- Cada nó da hierarquia corresponde a uma _tag_.
	- Exemplo: `<nomeDaTag> filhos </nomeDaTag>`.
- _Tags_ são aninhadas, criando a hierarquia.

```{.html .numberLines style="font-size: 70%;"} 
<html>
	<head>
	</head>

	<body>
		<h1>Um tutorial sobre HTML</h1>

		<p>Este documento <i>web</i> estabelece alguns...</p>
	</body>
</html>
```

:::
:::{.column width=40%}
- Hierarquia:

![](imagens/HTMLHierarquia.svg){style="width: 90%;"}

:::
:::::

# HTML: _Tags_ Aplicáveis ao `head`

| Nome da _Tag_ | Propósito                                            |
| ------------- | ---------------------------------------------------- |
| `script`      | Carrega ou define _script_ executado sobre a página  |
| `title`       | Define um título para a página                       |
| `style`       | Define estilos aplicados aos elementos da página     |
| `meta`        | Define metadados sobre a página                      |
| `link`        | Carrega algum recurso externo à página (_e.g._, CSS) |

# HTML: _Tags_ Típicas de Formatação (I)

<!--:::::{.columns}
:::{.column width=40%}-->
::::{.center style="font-size: 50%; line-height: 90%; padding-top: 2%;"}
| Nome da _Tag_         | Propósito                                                    |
| --------------------- | ------------------------------------------------------------ |
| `h1`, `h2`, ..., `h6` | Definir cabeçalhos (_e.g._, de seções)                       |
| `i`, `b`, `s`, `u`    | Fonte em itálico, negrito, tachado, sublinhado               |
| `p`                   | Define um parágrafo                                          |
| `table`               | Define uma tabela                                            |
| `th`                  | Define a linha de cabeçalho de uma tabela                    |
| `tr`                  | Define uma linha normal de tabela                            |
| `td`                  | Define uma célula em uma linha de tabela                     |
| `br`                  | Quebra uma linha                                             |
| `span`                | Define um trecho de texto (_e.g._, para formatação especial) |
| `a`                   | Cria um hiperlink para outro documento                       |
| `ul`, `ol`            | Criam listas de itens (sem ou com numeração)                 |
| `li`                  | Cria um item em uma lista.                                   |

::::

<!--
:::
:::{.column width=60%}-->

# HTML: _Tags_ Típicas de Formatação (II)

```{.html .numberLines style="font-size: 60%;"}
<html>
	<head>
	</head>
	<body>
		<h1>Título</h1>
        <h2>Seção</h2>
        Uma <b>tabela</b>:<br>
		<table>
            <tr><th>Col 1</th><th>Col 2</th></tr>
            <tr><td><s>val 1</s></td><td><u>val 2</u></td></tr>
            <tr><td><a href="outraPagina.html">val 3</a></td><td>val 4</td></tr>
        </table>
		<ul><li>Um item</li><li>Segundo item</li></ul>
	</body>
</html>
```

::::{style="position: absolute; width: 35%; bottom: 130px; right: 20px;"}
<iframe src="iframes/Exemplo1.html" style="width: 100%; height: 280px;">

</iframe>
::::

<!--
:::
::::: -->

# Exercício (I)

1\. Usando as tags html, head, body, p, h1 a h6, escreva uma página HTML similar ao exemplo abaixo:

::::{.center}
<iframe src="iframes/exercicios/ex1.html" style="width: 80%; height: 330px;">

</iframe>
::::

# Exercício (II)

2\. Escreva uma página HTML que apresente a seguinte tabela:

::::{.center width=80%}
Caracter | Permissão
:--------|:---------
r        | Permissão de leitura (*read*)
w        | Permissão de escrita (*write*)
x        | Permissão de execução (*execute*)
  -      | Permissão desabilitada
::::

- Note os nomes em itálico na segunda coluna.

# HTML: _Tags_ de Elementos Multimídia

:::::{.columns}
:::{.column width=50%}

| Nome da _Tag_ | Propósito          |
| ------------- | ------------------ |
| `img`         | Inserção de imagem |
| `video`       | Inserção de vídeo  |
| `audio`       | Inserção de áudio  |

:::
:::{.column width=50%}

```{.html .numberLines style="font-size: 14px;"}
<html>
	<head>
	</head>
	<body>
		<img src="teste.svg"></img>
	</body>
</html>
```

<iframe src="iframes/Exemplo2.html" style="width: 90%; height: 220px;">

</iframe>

:::
:::::

# HTML: Campos das _Tags_

- Várias _tags_ recebem parâmetros através de seus **campos**.
- Os campos são do tipo `nomeCampo="valor"` e aparecem após o nome da _tag_.
	- Exemplo: `<img src="teste.svg">`
	- Campo `src` define o caminho da imagem a ser exibida.
- Cada _tag_ tem seus campos possíveis padronizados.
	- Alguns exemplos típicos:

::::{.center style="font-size: 15px; line-height: 80%;"}
| Nome do campo | Propósito                                    | Algumas _tags_ às quais se aplica |
| ------------- | -------------------------------------------- | --------------------------------- |
| `src`         | Caminho do recurso associado ao elemento     | `img`, `audio`, `video`, `script` |
| `id`          | Define identificador do elemento             | Muitos                            |
| `class`       | Associa elemento a uma classe                | Muitos                            |
| `style`       | Altera características de estilo do elemento | Muitos                            |
| `width`       | Configura a largura do elemento              | Muitos                            |
| `height`      | Configura a altura do elemento               | Muitos                            |
::::

# HTML: Campos das _Tags_ (Exemplo)

:::::{.columns}
:::{.column width=50%}

```{.html .numberLine style="font-size: 16px;"}
<html>
	<head>
	</head>
	<body>
        <table class="tipoTabela" id="tab1" width="50px">
            <tr><th>Col 1</th><th>Col 2</th></tr>
            <tr><td><s>val 1</s></td><td><u>val 2</u></td></tr>
            <tr><td>val 3</td><td>val 4</td></tr>
        </table>

        <table class="tipoTabela" id="tab2" style="width: 150px">
            <tr><th>Col 1</th><th>Col 2</th></tr>
            <tr><td><s>val 1</s></td><td><u>val 2</u></td></tr>
            <tr><td>val 3</td><td>val 4</td></tr>
        </table>

    </body>
</html>
```

:::
:::{.column width=50%}

<iframe src="iframes/Exemplo3.html" style="width: 90%; height: 220px;">

</iframe>

:::
:::::

# Exercício (III)

3\. Adicione uma imagem a uma das páginas criadas nos exercícios anteriores.

4\. Adicione um link na página do exercício I para a página do exercício II.


# HTML: A _Tag_ `div`


::::{}
- Um `div` é um elemento que agrega outros elementos.
	- Cria uma **divisão** no documento contendo uma parte do conteúdo.
- São muito úteis para organizar logicamente o documento.
- Em certas situações, permitem também aplicar regras de estilo a vários elementos de uma só vez.
	- Os elementos filhos do `div`.

::::

:::::{.columns}
:::{.column width=50%}

```{.html .numberLine style="font-size: 16px;"}
<html>
	<head>
	</head>
	<body>
        <div style="color: red; border: 1px solid;">
            <p>Primeiro parágrafo</p>
            <p>Segundo parágrafo</p>
        </div>
    </body>
</html>
```


:::
:::{.column width=50%}

<iframe src="iframes/Exemplo4.html" style="width: 90%; height: 220px;">

</iframe>

:::
:::::

# HTML: Formulários (I)

- Criados com a _tag_ `form`.
- Permitem obter entradas do usuário.
	- Em geral, para envio ao servidor.
- Podem conter elementos como botões, entradas de texto, _checkboxes_, _radiobuttons_, ...
	- Criados com a _tag_ `input`, variando-se o campo `type`.
	- Exemplos:

::::{.center style="font-size: 15px; line-height: 80%;"}
| `type`     | Propósito              | Exemplo                                        |
| ---------- | ---------------------- | ---------------------------------------------- |
| `button`   | Cria um botão          | `<input type="button" value="Carregue aqui!">` |
| `text`     | Cria uma caixa de text | `<input type="text">`                          |
| `checkbox` | Cria um _checkbox_     | `<input type="checkbox" value="opcao1">`       |
::::


# HTML: Formulários (II)

::::{}
- Na maioria dos casos, um `input` pode/deve ter um `label` associado.
	- Associa um texto ao `input`.
- Exemplo:

::::

:::::{.columns}
:::{.column width=50%}

```{.html .numberLines style="font-size: 16px;"}

<html>
	<head>
	</head>
	<body>
        <form>
            <label for="fname">Nome:</label>
            <input type="text" id="nome"><br><br>
            <label for="lname">Apelido:</label>
            <input type="text" id="apelido"><br><br>            
            <input type="checkbox" id="pais1" value="Angola">
            <label for="pais1">Nasci em Angola</label><br>
            <input type="checkbox" id="pais2" value="Brasil">
            <label for="pais2">Nasci no Brasil</label><br>
            <input type="checkbox" id="pais3" value="Portugal">
            <label for="pais3">Nasci em Portugal</label>
        </form> 
	</body>
</html>

```

:::
:::{.column width=50%}

<iframe src="iframes/Exemplo5.html" style="width: 90%; height: 220px;">

</iframe>

:::
:::::

# HTML: Submetendo um Formulário

::::{}
- Informações de formulário são geralmente submetidas a algum objeto HTTP.
	- Um _software_ do _backend_ responsável por processá-lo.
- No HTML, isso é feito em duas partes:
	1. Preenchimento do campo `action` do elemento `form`.
	2. Inclusão de um `input` de tipo `submit`.
::::

:::::{.columns}
:::{.column width=50%}

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
	</head>
	<body>
        <form action="/processaForm.php">
            <label for="nome">Nome:</label>
            <input type="text" id="nome"><br><br>
            <label for="apelido">Apelido:</label>
            <input type="text" id="apelido"><br><br>            
            <input type="checkbox" id="pais1" value="Angola">
            <label for="pais1">Nasci em Angola</label><br>
            <input type="checkbox" id="pais2" value="Brasil">
            <label for="pais2">Nasci no Brasil</label><br>
            <input type="checkbox" id="pais3" value="Portugal">
            <label for="pais3">Nasci em Portugal</label><br>
            <input type="submit" value="Enviar">
          </form> 
	</body>
</html>
```


:::
:::{.column width=50%}
<iframe src="iframes/Exemplo6.html" style="width: 90%; height: 220px;">

</iframe>
:::
:::::

# HTML: Criando um Simples Botão

- Botão é útil para criar interação com o utilizador e disparar eventos.
- Existe input com o type="button".

```{.html .numberLines style="font-size: 18px;"}
	        <input type="button" value="Clique aqui");">

```

- Existem também a _tag_ **button**.

```{.html .numberLines style="font-size: 18px;"}
			<button type="button">Clique aqui!</button>
```

# Javascript e DOM {.part}

# Javascript e DOM

- DOM: _Document Object Model_.
	- Representação do HTML da página criada pelo _browser_.
	- A partir do _parse_ do documento.
	- Árvore em que os nós são os elementos/_tags_ do documento.
- Javascript disponibiliza funções para interagir com o DOM:
	- Navegar pela hierarquia.
	- Acessar, modificar, remover e adicionar novos nós.

::::::{.block .centered}
:::{.blocktitle}
Utilidades
:::
- Código Javascript pode alterar conteúdo e estilo da página mostrada ao usuário.
- Código Javascript pode ler valores introduzidos pelo usuário em campos de formulário.
::::::

# Javascript e DOM: O Objeto `document`

- Acesso ao DOM pode ser feito pelo objeto `document`.
	- Implicitamente disponível.
	- Representa o documento HTML.
	- Contém (entre outras) a propriedade `documentElement`.
		- Elemento correspondente à _tag_ `<html>`.
		- Ou seja, a raiz da árvore.
- Cada nó do DOM possui (entre outras) as propriedades.
	- `childNodes`: vetor com os seus filhos no DOM.
	- `parentNode`: seu pai no DOM.
	- `nodeName`: identificador do tipo de nó na árvore DOM.

# Javascript e DOM: Navegando através do `document`

- Podemos, portanto, navegar o DOM começando no `document`. Exemplo:

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
            function retornaNoEFilhos(no, nivel) {
                var s = "", i;
                if (nivel > 0) {
                    for (i = 0; i < nivel - 1; i++) s += "      ";
                    s += "+---- "
                }
                s += no.nodeName + "\n";
                for (i = 0; i < no.childNodes.length; i++) 
                    s += retornaNoEFilhos(no.childNodes[i], nivel + 1);
                return(s);
            }
        </script>
	</head>
	<body>
		<h1>Título</h1>
        <h2>Seção</h2>
        Uma <b>tabela</b>:<br>
		<table>
            <tr><th>Col 1</th><th>Col 2</th></tr>
            <tr><td><s>val 1</s></td><td><u>val 2</u></td></tr>
            <tr><td><a href="outraPagina.html">val 3</a></td><td>val 4</td></tr>
        </table>
        <input type="button" value="Gerar DOM" onclick="alert(retornaNoEFilhos(document.documentElement, 0));">
	</body>
</html>
```

::::{style="position: absolute; width: 40%; bottom: 150px; right: 50px;"}
<iframe src="iframes/Exemplo9.html" style="width: 90%; height: 300px; background-color: white;">

</iframe>


::::

# Javascript e DOM: A Família de Métodos `getElementBy*`

- Podemos encontrar um elemento no DOM fazendo uma busca na árvore.
- Mas há métodos (do objeto `document`) já disponíveis para isso:

::::{.center style="font-size: 15px; line-height: 80%;"}
| Nome                      | Retorno                                        |
| ------------------------- | ---------------------------------------------- |
| `getElementById()`        | Primeiro (único?) elemento com id especificado |
| `getElementByTagName()`   | Todos os elementos daquela _tag_               |
| `getElementByName()`      | Todos os elementos com aquele nome             |
| `getElementByClassName()` | Todos os elementos pertencentes aquela classe  |
::::

- Note: para o `getElementByClassName()`, múltiplas classes podem ser especificadas separadas por espaço.
	- Retorno: elementos que pertencem a ambas **simultaneamente**.

```{.javascript .numberLines style="font-size: 16px;"}
var el1 = document.getElementById('meuDiv');
var el2 = document.getElementByTagName('div');
var el3 = document.getElementByClass('minhaClasse1 minhaClasse2');
```

# Javascript e DOM: Modificar Conteúdo de Elementos

- Pode ser feito com a propriedade `innerHTML`:

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
			var vezesCarregado = 0;
            function carregaBotao() {
				vezesCarregado++;
				var el = document.getElementById("saida");
				if (vezesCarregado == 1)
					el.innerHTML = "Botão foi carregado 1 vez";
				else
					el.innerHTML = "Botão foi carregado " + String(vezesCarregado) +" vezes";
			}
        </script>
	</head>
	<body>
		<h1>Vezes carregado</h1>
		<p id="saida">Botão foi carregado 0 vezes</p>
        <input type="button" value="Carregar" onclick="carregaBotao();">
	</body>
</html>
```

::::{style="position: absolute; width: 40%; bottom: 50px; right: 20px; padding-right: 10px;"}
<iframe src="iframes/Exemplo10.html" style="width: 90%; height: 150px; background-color: white;">

</iframe>
::::

# Javascript e DOM: Modificar Estilo de Elementos

- Pode ser feito com a propriedade `style`:

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
			var indiceCor = 0;
            var cores = ["", "blue", "red", "green", "orange"];
            function alteraCor() {
				indiceCor = (indiceCor + 1) % cores.length;
				var el = document.getElementById("meuElemento");
				el.style.color = cores[indiceCor];
			}
        </script>
	</head>
	<body>
		<h1>Mudança de cor</h1>
		<p id="meuElemento">Um texto qualquer</p>
        <input type="button" value="Alterar cor" onclick="alteraCor();">
	</body>
</html>
```

::::{style="position: absolute; width: 40%; bottom: 50px; right: 20px; padding-right: 10px;"}
<iframe src="iframes/Exemplo11.html" style="width: 90%; height: 150px; background-color: white;">

</iframe>
::::

# Exercício Rápido (I)

1. Experimentos os códigos HTML + JS de ambos os slides anteriores.
	- Cada um é uma página HTML distinta (separada).

# Javascript e DOM: Inserindo Novos Elementos

- **Objetivo**: criar um novo elemento em determinado ponto do documento.
	- _e.g._, colocar uma tabela dentro de um `div`.
- Técnicamente, pode ser feito com o `innerHTML`:
	1. Acha-se o elemento do DOM correspondente ao `div`.
	2. Adiciona-se o código HTML da tabela ao `innerHTML` do `div`.

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
            function adicionaTabela() {
				var el = document.getElementById("meuDiv");
				el.innerHTML += "<table><tr><th>Col 1</th><th>Col 2</th></tr>";
				el.innerHTML += "<tr><td>Dado 1</td><td>Dado 2</td></tr></table>";
			}
        </script>
	</head>
	<body>
		<h1>Tabela Dinâmica</h1>
		<div id="meuDiv"></div>
        <input type="button" value="Adiciona Tabela" onclick="adicionaTabela();">
	</body>
</html>
```

# Javascript e DOM: Inserindo Novos Elementos (II)

- No entanto, Javascript fornece uma API para esse fim.
	- Torna código mais legível.
- Métodos relevantes:

::::{.center style="font-size: 15px; line-height: 80%;"}
| Método                      | Propósito                                                             | Exemplo                                 |
| --------------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| `document.createElement()`  | Cria novo elemento DOM do tipo especificado                           | `document.createElement("table")`       |
| `document.createTextNode()` | Cria novo nó do tipo `text` (_i.e._, conteúdo de tag)                 | `document.createElement("Novo texto!")` |
| `el.appendChild()`          | Acrescenta novo filho ao elemento (como último filho)                 | `el.appendChild(novoDiv)`               |
| `el.insertBefore()`         | Acrescenta novo filho ao elemento (antes de outro filho especificado) | `el.insertBefore(novoDiv, outroFilho)`  |
::::


- **Nota**: na tabela, `el` denota algum elemento/nó **já existente** no DOM.


# Javascript e DOM: Exemplos de Inserção

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
            var elementosAdicionados = 0;
            function adicionaLinha() {
				var el = document.getElementById("minhaTabela");
                var tr = document.createElement("tr");
                var td1 = document.createElement("td");
                var td2 = document.createElement("td");
                var text1 = document.createTextNode("Texto célula " + String(++elementosAdicionados));
                var text2 = document.createTextNode("Texto célula " + String(++elementosAdicionados));
                td1.appendChild(text1);
                td2.appendChild(text2);
                tr.appendChild(td2);
                tr.insertBefore(td1, td2); // td1 inserido antes do td2!
                el.appendChild(tr);
			}
        </script>
	</head>
	<body>
		<h1>Tabela Dinâmica (II)</h1>
		<table id="minhaTabela">
            <tr><th>Col 1</th><th>Col 2</th></tr>
        </table>
        <input type="button" value="Nova linha ao final" onclick="adicionaLinha();">
	</body>
</html>
```

::::{style="position: absolute; width: 25%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo13.html" style="width: 90%; height: 350px; background-color: white;">

</iframe>
::::

# Exercício (IV)

- Gere um ficheiro HTML com o exemplo do slide anterior.
	- Interaja com o botão e observe seu comportamento.
- Agora, edite seu ficheiro HTML e adicione dois campos de formulário com _id_ formCol1 e formCol2, respectivamente.
	- Posicione-os lado a lado, entre a tabela e o botão.
	- Use a tag `<br>` para quebrar a linha entre os elementos.
- Faça com que o valor preenchido de ambos os campos do formulário sejam incluídos como uma linha da tabela.

# Javascript e DOM: Remoção e Substituição

- Por vezes, é útil removermos ou substituirmos um elemento do DOM.
- API provê métodos para isso:

::::{.center style="font-size: 15px; line-height: 80%;"}
| Método              | Propósito                                          | Exemplo                         |
| ------------------- | -------------------------------------------------- | ------------------------------- |
| `el.removeChild()`  | Remove filho especificado do elemento              | `el.removeChild(elFilho)`       |
| `el.replaceChild()` | Substitui filho especificado do elemento por outro | `el.replaceChild(novo, antigo)` |
::::

# Javascript e DOM: Exemplos de Remoção e Substituição

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
            function substitui() {
				var lista = document.getElementById("lista");
				var item = document.getElementById("substituido");
                var novo = document.createElement("li");
                novo.appendChild(document.createTextNode("Novo item"));
                lista.replaceChild(novo, item);
			}
            function remove() {
				var lista = document.getElementById("lista");
				var item = document.getElementById("removido");
                lista.removeChild(item);
			}
        </script>
	</head>
	<body>
		<h1>Remoção e Substituição</h1>
		<ul id="lista">
            <li id="substituido">Item 1</li>
            <li>Item 2</li>
            <li id="removido">Item 3</li>
        </ul>
        <input type="button" value="Remove" onclick="remove();">
        <input type="button" value="Substitui" onclick="substitui();">
	</body>
</html>
```

::::{style="position: absolute; width: 25%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo14.html" style="width: 90%; height: 350px; background-color: white;">

</iframe>
::::

# Javascript: Eventos

- Um dos principais usos de Javascript é **responder a eventos**.
	- Carregamento de botões.
	- Estouro de temporizadores.
	- Término de carregamento da página.
	- Mudança em campo de formuário.
	- ...
- Paradigma de **Programação Orientada a Eventos**.

::::::{.block .centered}
:::{.blocktitle}
_Callback_
:::
- Conceito básico do paradigma.
- Função chamada quando determinado evento ocorre.
::::::

# Javascript: Eventos do DOM

- Boa parte dos elementos HTML suporta vários eventos.
- Propriedades `on*` associam eventos a códigos Javascript.
- Eventos comuns:

::::{.center style="font-size: 15px; line-height: 80%;"}
| Propriedade   | Evento                                     | Observações                 |
| ------------- | ------------------------------------------ | --------------------------- |
| `onclick`     | Usuário carrega no elemento                |                             |
| `onload`      | Página é carregada                         | Usado com elemento `body`   |
| `onunload`    | Usuário deixa a página                     | Usado com elemento `body`   |
| `onchange`    | Campo de formulário tem valor alterado     | Usado com elementos `input` |
| `onmouseover` | Cursor está sobre elemento                 |                             |
| `onmouseout`  | Cursor deixa área do elemento              |                             |
| `onmousedown` | Botão do rato é pressionado sobre elemento |                             |
| `onmouseup`   | Botão do rato é liberado sobre o elemento  |                             |
::::

# Javascript: Eventos de Temporização

- Em alguns casos, queremos executar após um determinado tempo.
- Para isso, criamos um **temporizador**, associamos uma duração e uma _callback_.
	- Feito com a função `setTimeout()`.
	- Retorna um objeto representando o temporizador.
- Podemos cancelar o temporizador criado usando a função `clearTimeout()`.

# Javascript: Exemplo de Temporizador

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script type="text/javascript">
            var timer;
            function iniciar() {
				var botao = document.getElementsByTagName("input")[0];
                botao.value = "Parar";
                botao.onclick = parar;  // Altera callback do botão.
                timer = setTimeout(timerCallback, 1000);
			}
            function parar() {
				var botao = document.getElementsByTagName("input")[0];
                botao.value = "Iniciar";
                botao.onclick = iniciar;  // Altera callback do botão.
                clearTimeout(timer);
			}
            function timerCallback() {
                var el = document.getElementById("titulo");
                if (el.style.color == "red") el.style.color = "";
                else el.style.color = "red";
                timer = setTimeout(timerCallback, 1000);
            }
        </script>
	</head>
	<body>
		<h1 id="titulo">Temporizador</h1>
        <input type="button" value="Iniciar" onclick="iniciar();">
	</body>
</html>
```

::::{style="position: absolute; width: 25%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo16.html" style="width: 90%; height: 350px; background-color: white;">

</iframe>
::::

# Exercício (V)

1. Crie um ficheiro em HTML + JS que mostre imagens diferentes a cada 10 s.
	- Baseie-se no slide anterior para isso e inclua botões para iniciar e parar.
	- No JS, crie um vetor ou objeto para armazenar os caminhos das imagens.
	- Use o campo _value_ da caixa de texto do formulário para obter o seu conteúdo.
