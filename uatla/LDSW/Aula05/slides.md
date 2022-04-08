---
author: Fernanda Passos
subtitle: GSC - Laboratório de Desenvolvimento de Sistemas Web
title: Javascript, *Document Object Model* e jQuery
institute: Atlântica - Instituto Universitário
logo: ../atlantica_logo2.svg
---

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

- Podemos encontrar um elemento no DOM fazendo implementando uma busca na árvore.
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

# Javascript e DOM: Modificando Conteúdo de Elementos

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

# Javascript e DOM: Modificando Estilo de Elementos

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

# jQuery {.part}

# Biblioteca jQuery

- Biblioteca de Javascript.
- Apresenta funcionalidades para:
	- Manipular elementos do DOM;
	- Aplicar efeitos e animações ricos (já prontos) em elementos;
	- Capturar eventos e configurar diversas ações sobre elementos;
	- Trabalhar com Ajax (veremos futuramente);
	- ...


# Inclusão do jQuery

- Pode ser feito download em [jQuery.com](https://jquery.com)
	- Extensão .js
- Através de uma ligação da biblioteca neste site:
	- https://code.jquery.com/jquery-3.6.0.min.js
- Através de uma ligação da biblioteca em um CDN, como o Google:
	- https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js

# Inclusão do jQuery: Exemplos

- Incluir no mesmo diretório do html.

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
		<!-- Fazer download em https://jquery.com -->
		<script src="jquery-3.6.0.min.js"></script>
	</head>
	<body> ...
	</body>
</html>
```

- Ligação no CDN do Google.

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	</head>
	<body> ...
	</body>
</html>
```
# Sintaxe do jQuery

- A sintaxe é baseada na seleção de elementos do DOM e ações associadas a ele.
	- $(seletor).acao()
- É necessário o $ ao início.
- Entre parênteses (obrigatório) fica o seletor.
	- Seleciona um elemento na forma de objeto.
- acao() é um método disponível ao elemento.
- Exemplos:
	- `$("p").text("Texto do parágrafo")` - altera o texto dos parágrafos.
	- `$(".teste").text("Texto de teste.")` - altera o texto dos elementos que tem `class="teste"`.
	- `$(this).hide()` - esconde o elemento corrente.

# Executar Comandos jQuery

- Dentro de `<script> </script>` do tipo Javascript.
- Necessário selecionar inicialmente o elemento raiz: *document*.
	- Ação *ready()* indica que página foi totalmente carregada.
	- O argumento do método *ready()* é uma função (geralmente anónima).


```{.html .numberLines style="font-size: 18px;"}
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
        $(document).ready(function(){
			// Comandos aqui
        });
        </script>
    </head>
    <body> ...
    </body>
</html>
```

# Executar Comandos jQuery: Exemplo

```{.html .numberLines style="font-size: 18px;"}
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
        $(document).ready(function(){
			$("h1").click(function(){
				$(this).hide();
			});
        });
        </script>
    </head>
    <body>
        <h1>Carregue aqui para esconder</h1>
    </body>
</html>
```

::::{style="position: absolute; width: 50%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo17_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Seletores do jQuery

- Baseados nos seletores do CSS.

::::{.center style="font-size: 18px; line-height: 80%; width: 95%;"}
| Seletor   | Seleção de elemento HTML por: | Exemplo                 | Descrição do exemplo                         |
|-----------|-------------------------------|-------------------------|----------------------------------------------|
| Elemento  | Nome da tag.                  | `$("p")`                | Seleciona todos os elementos `<p>`.          |
| #id       | Valor do atributo id.         | `$("#teste")`           | Seleciona elemento de id teste.              |
| .class    | Valor do atributo class.      | `$(".teste")`           | Seleciona elementos de class="teste'.        |
| [atr]     | Atributo atr.                 | `$("[href]")`           | Seleciona todos elementos com atributo href. |
| [atr=val] | Atributo atr igual a val.     | `$("a[target='_blank']")` | Seleciona todas as tags `<a>` com target='_blank'.   |
::::

- Para mais, consultar: [https://api.jquery.com/category/selectors/](https://api.jquery.com/category/selectors/)

# Ações ou Eventos

::::{.center style="font-size: 20px; line-height: 80%; width: 95%;"}
| Rato       | Teclado  | Formulário | Documento/Janela |
|------------|----------|------------|------------------|
| click      | keypress | submit     | load             |
| dblclick   | keydown  | change     | resize           |
| mouseenter | keyup    | focus      | scroll           |
| mouseleave |          | blur       | unload           |
::::

- Exemplo:

```{.js .numberLines style="font-size: 18px;"}
        $(document).ready(function(){
			$("h1").dblclick(function(){
				$(this).hide();
			});
        });
```

# Exemplos com Botões

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
        var vezesCarregado = 0;
        $(document).ready(function(){
			$("input[value='Gerar alert()']").click(function(){
				alert("mensagem!");
			});
			$("input[value='Gerar console.log()']").click(function(){
				console.log("mensagem!");
			});
        });
        </script>
	</head>
	<body>
		<input type="button" value="Gerar alert()"><br><br>
		<input type="button" value="Gerar console.log()">
	</body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo8_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Manipular Elementos do DOM com jQuery

- Métodos para obter e alterar elementos (get e set): 
	- **text()** - obtém ou altera texto do elemento selecionado.
	- **html()** - obtém ou altera conteúdo do elemento selecionado.
	- **val()** - obtém ou altera o valor de campos de um elemento de formulário selecionado.
		- elmentos que tem o atributo *value*.
	- **css(propriedade)** - obtém ou altera css do elemento selecionado.
	- **attr()** - obtém valores de atributos (apenas get).
- Para métodos de alteração do elemento (set), um parâmetro a mais é colocado.
	- O valor.

# Manipular Elementos do DOM com jQuery: Exemplos

- Exemplo de get com text():
	- `var texto = $("#idA").text();`
	- A variável `texto` terá o texto do elemento identificado por idA.
- Exemplo de set com text():
	- `$("p").text("Texto do parágrafo");`
- Exemplo de set com css():
	- `$("p").css("color", "blue");`
- Exemplo de get com atr():
	- `var link = $("#a_id").attr("href");`

# Exemplo: Contar Vezes de Botão Carregado

```{.html .numberLines style="font-size: 17px;"}
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
        var vezesCarregado = 0;
        $(document).ready(function(){
			$("input").click(function(){
				vezesCarregado++;
				var texto = "Botão foi carregado ";
				texto += (vezesCarregado == 1)? "1 vez" : String(vezesCarregado) + " vezes";
				$("#saida").text(texto);
			});
        });
        </script>
    </head>
    <body>
        <h1>Vezes carregado</h1>
        <p id="saida"> Botão foi carregado 0 vezes </p>
        <input type="button" value="Carregar">
    </body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo10_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Exemplo (versão 2): Contar Vezes de Botão Carregado

```{.html .numberLines style="font-size: 17px;"}
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
        $(document).ready(function(){
			$("input").click(function(){
                $("#num").text(function(i, num){
					if (num == "0") $("#unid").text("vez");
					else $("#unid").text("vezes");
					return(Number(num) + 1);
				});
			});
        });
        </script>
    </head>
    <body>
        <h1>Vezes carregado</h1>
        <p id="saida">Botão foi carregado <span id="num">0</span> <span id="unid">vezes</span> </p>
        <input type="button" value="Carregar">
    </body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 220px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo10_jQuery_v2.html" style="width: 90%; height: 190px; background-color: white;">

</iframe>
::::

# Exemplo: Alterar Cor de Texto

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
		var indiceCor = 0;
        const cores = ["", "blue", "red", "green", "orange"];
		$(document).ready(function(){
			$("input[type=button]").click(function(){
				indiceCor = (indiceCor + 1) % cores.length;
				$("#meuElemento").css("color", cores[indiceCor]);
			});
        });
        </script>
	</head>
	<body>
		<h1>Mudança de cor</h1>
		<p id="meuElemento">Um texto qualquer</p>
        <input type="button" value="Alterar cor">
	</body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo11_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Inserir e Remover Conteúdos com jQuery

- Para inserir:
	- **append()** - insere conteúdo ao final dos elementos selecionados.
	- **prepend()** - insere conteúdo ao início dos elementos selecionados.
	- **after()** - insere conteúdo após os elementos selecionados.
	- **before()** - insere conteúdo antes dos elementos selecionados.
- Para remover:
	- **remove()** - remove os elementos selecionados e seus filhos.
	- **empty()** - remove os filhos dos elementos selecionados.
		- Descendentes dos filhos também são removidos.
- Para substituir:
	- **replaceWith()** - substitui elementos selecionados por outro (em argumento).

# Exemplo: Tabela Dinâmica

```{.html .numberLines style="font-size: 16px;"}
<html>
	<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
		// Exemplo de tabela estática em JSON:
		const tabDados = {"Título 1": [
			 {"Col 1" : "Dado 1", "Col 2": "Dado 2", "Col 3" : "Dado 3"},
			 {"Col 1" : "Dado 4", "Col 2": "Dado 5", "Col 3" : "Dado 6"}]};	
		$(document).ready(function(){
			$("input[type=button]").click(function(){
				var tabela = $("<table>");
				// Incluir cabeçalho
				var cab = $("<tr>");
				for (let j in tabDados["Título 1"][0])
					cab.append($("<th>").append(j));
				tabela.append(cab);
				// Incluir outras linhas
				for (let i of tabDados["Título 1"]){
					var lin = $("<tr>");
					for (let j in i)
						lin.append($("<td>").append(i[j]));
					tabela.append(lin);
				}
				$("#meuDiv").append(tabela);
			});
        });
        </script>
	</head>
	<body>
		<h1>Tabela Dinâmica</h1>
        <input type="button" value="Adiciona Tabela">
		<div id="meuDiv"></div>
	</body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 110px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo12_jQuery.html" style="width: 90%; height: 300px; background-color: white;">

</iframe>
::::

# Exemplo: Tabela Dinâmica (II)

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
		$(document).ready(function(){
            var elementosAdicionados = 0;
            $("input[type=button]").click(function(){
                var td = $("<td>").text("Texto célula " + String(++elementosAdicionados));
                var nova_lin = $("<tr>").append(td);
                td.after($("<td>").text("Texto célula " + String(++elementosAdicionados)));
                $("#minhaTabela").append(nova_lin);
            });
        });
        </script>
	</head>
	<body>
		<h1>Tabela Dinâmica (II)</h1>
		<table id="minhaTabela">
            <tr><th>Col 1</th><th>Col 2</th></tr>
        </table>
        <input type="button" value="Nova linha ao final">
	</body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo13_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Exemplo: Remoção e Substituição de Elementos

```{.html .numberLines style="font-size: 17px;"}
<html>
	<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript">
		$(document).ready(function(){
            $("#btn_rem").click(function(){
                $("#removido").remove();
            });
            $("#btn_sub").click(function(){
                //$("#substituido").text("Novo item"); // Apenas altera conteúdo
                $("#substituido").replaceWith($("<li>").text("Novo item"));
            });
        });
        </script>
	</head>
	<body>
		<h1>Remoção e Substituição</h1>
		<ul id="lista">
            <li id="substituido">Item 1</li>
            <li>Item 2</li>
            <li id="removido">Item 3</li>
        </ul>
        <input id="btn_rem" type="button" value="Remove"></input>
        <input id="btn_sub" type="button" value="Substitui"></input>
	</body>
</html>
```

::::{style="position: absolute; width: 45%; bottom: 100px; right: 0px; padding-right: 0px;"}
<iframe src="iframes/Exemplo14_jQuery.html" style="width: 90%; height: 200px; background-color: white;">

</iframe>
::::

# Exercício

- Gere uma tabela dinâmica com jQuery.
	- Permita que utilizador adicione e remova linhas.
- Cada célula da tabela (exceto o título) deve ser editável.
	- Use: `<td contenteditable="true">`
- Inclua um botão que "salva" a tabela.
- Salvar significa guardar seu conteúdo em um objeto Javascript.
	- Futuramente pode ser usado para enviar dados da tabela para o servidor.

# Percorrer Árvore do DOM com jQuery

- Existem funções ascendentes:
	- parent(): seleciona o elemento pai de um elemento.
	- parents(): seleciona todos os elementos pais de um elemento.
		- Vai até a raiz `<html> </html>`.
	- parentsUntil("xxx"): seleciona todos os elementos pais de um elemento até o elemento "xxx".
		- "xxx" é um filtro.
- Existem funções descententes:
	- children(): seleciona todos os filhos diretos de um elemento.
		- Vai até 1 nível apenas.
	- children("xxx"): o mesmo que o anterior, mas "xxx" é filtro.
	- find("xxx"): seleciona todos os filhos de um elemento com o filtro "xxx".
		- Procura em todos os níveis descendentes.
		- "*" é o filtro para selecionar todos os filhos.

# Exercícios sobre Funções Ascendentes de Descendentes

- Aceda [https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_parent](https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_parent)
	- Analise o HTML e jQuery.
- Na função do jQuery, a partir do HTML original:
	- Experimente trocar parent() para parents().
	- Experimente trocar parent() para parentsUntil("div").
	- Experimente trocar parent() para parentsUntil("div.ancestors").
	- Experimente trocar seletor "span" para "div" e parent() para children().
	- Experimente trocar seletor "span" para "div" e parent() para find("span").
	- Experimente trocar seletor "span" para "div" e parent() para find("*").

# Efeitos jQuery

- A maioria dos efeitos jQuery tem a seguinte sintaxe:
	- `$(seletor).efeito([velocidade [, callback]]);`
	- velocidade (facultativo): velocidade que ocorre o efeito.
		- Pode ser "slow", "fast" e valores numéricos em milissegundos.
	- callback (facultativo): função que será chamada quando o efeito terminar.
- Alguns efeitos são:
	- Esconder/mostrar:
		- **hide()**: esconder.
		- **show()**: mostrar.
		- **toggle()**: alterna/comuta entre hide() e show().
	- Sliding (deslizar):
		- **slideDown()**: deslizar para baixo.
		- **slideUp()**: deslizar para cima.
		- **slideToggle()**: alterna/comuta entre slideUp() e slideDown().

# Mais Efeitos jQuery

- Fade (aparecer e desaparecer):
	- **fadeIn()**: aparecer um elemento escondido.
	- **fadeOut()**: desaparecer.
	- **fadeToggle()**: alterna/comuta entre fadeIn() e fadeOut().
	- **fadeTo()**: desaparece até um dado nível de opacidade (entre 0 e 1).
		- `$(seletor).fadeTo(velocidade, opacidade[, callback]);`
		- Velocidade e opacidade são obrigatórios.
- Animate (animação): cria animações customizadas.
	- `$(selector).animate(propriedades[,velocidade,callback]);`
	- propriedades (obrigatório): atributo e valor CSS entre { }.
	- Apenas propriedades numéricas podem ser animadas.
		- width/height, left/right, fontSize, opacity, ...