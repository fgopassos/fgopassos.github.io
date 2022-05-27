---
author: Fernanda Passos
subtitle: GSC - Laboratório de Desenvolvimento de Sistemas Web
title: AJAX e jQuery
institute: Atlântica - Instituto Universitário
logo: ../atlantica_logo2.svg
---

# AJAX {.part}

# Definição

- AJAX = *Asynchronous Javascript And XML*
- É uma técnica de desenvolvimento Web para troca de objetos assincronamente.
	- Não é uma linguagem de programação!
- Por AJAX, podemos enviar e receber dados de/para servidor e atualizar partes da página web.
	- Não precisa recarregar toda a página!
	- Requisições assíncronas são implementadas por Javascript.
	- Troca de dados é realizada por XML, JSON, ...

# Funcionamento do AJAX

::::{.center}
<br>
![](imagens/ajax_work.svg){width=40%}
::::


# AJAX por jQuery e Flask {.part}

# AJAX por jQuery

- jQuery possui uma biblioteca para o AJAX.
	- Download a partir de [jQuery.com](https://jquery.com)
	- Extensão .js

# Alguns Métodos

| Método            | Descrição                                                         |
|-------------------|-------------------------------------------------------------------|
| $.ajax()          | Realiza requisição assíncrona com AJAX.                           |
| $.getJSON()       | Carrega dados no formato JSON de um servidor usando HTTP GET.     |
| $.post()          | Envia dado para o servidor usando uma requisição HTTP POST.       |
| serialize()       | Codifica um conjunto de elementos como uma string para submissão. |

# O método $.ajax()

- É o método mais completo (e baixo nível).
- Sintaxe: `jQuery.ajax( url [, settings ] )`
	- `url`: string que contém a URL a qual a requisição será enviada.
	- `settings`: é opcional e é dado por conjunto de chaves/valores.
		- `data`: dado a ser enviado para o servidor.
		- `type` ou `method`: tipo de requisição (*e.g.*, GET, POST).
		- `dataType`: tipo de dado que se espera receber do servidor.
		- `success`: uma função (*callback*) que será chamada quando a requisição é bem sucedida.
		- `error`: uma função (*callback*) que será chamada quando a requisição falha.
		- `contentType`: indica o tipo de conteúdo do dado a ser enviado.
		- `processData`: indica se dado será processado como uma *query string* (padrão é `true`).
- Consulte a referência: [jQuery.ajax](https://api.jquery.com/jQuery.ajax/)

# Exemplo de Uso com Flask: o Javascript

```{.js .numberLines style="font-size: 20px;"}
// Coloca a resposta no texto do resultado
function tratar_sucesso(data){
	$("#resultado").text(data.resultado);
}
// Calcular soma no servidor assincronamente
function calcular_server(){
	valor_a = $('input[name="a"]').val();
	valor_b = $('input[name="b"]').val();
	json_send = {a: valor_a, b: valor_b};
	$.ajax({
		url: $SCRIPT_ROOT + '/soma',
		dataType: "json",
		data: json_send,
		type: "GET",
		success: tratar_sucesso
	});
}
// Início do jQuery:
$(function() {
	$('#botaoSoma').click(calcular_server);
});
```

# Exemplo de Uso com Flask: o HTML

```{.HTML .numberLines style="font-size: 20px;"}
<html>
<head>
<script type=text/javascript src="{{ url_for('static', filename='jquery.js') }}"> </script>
<script type=text/javascript src="{{ url_for('static', filename='meu_ajax.js') }}"> </script>
<script type=text/javascript>
  $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
</head>
<body>
	<h1>Exemplo de uso de jQuery com AJAX:</h1>
	<p><input type=text size=5 name=a> + </input>
	   <input type=text size=5 name=b> = </input>
	   <span id=resultado> ? </span>
	</p>
	<input id=botaoSoma type=button value='Somar'> </input>
</body>
</html>
```

# Exemplo de Uso com Flask: o Python

```{.Python .numberLines style="font-size: 20px;"}
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/soma')
def soma():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        r = a + b
        print(a, "+", b, "=", r)
        return jsonify(resultado=r)
    except Exception as m:
        return(jsonify(resultado=str(m)))

@app.route('/')
def index():
    return render_template('index.html')

# Inicio do programa:
if __name__ == "__main__":
    app.run(debug=True)
```

# O método $.getJSON()

- Sintaxe: `$.getJSON( url [, data ] [, success ] )`
- É o método facilitador que **substitui**:

```{.js .numberLines style="font-size: 24px;"}
$.ajax({
  url: url,
  type: "GET", // Não precisa pois já é o valor padrão
  dataType: "json",
  data: data,
  success: success
});
```

# Atividades (I)

1. Experimente os exemplos dos slides anteriores para a soma de dois números em Flask + jQuery + AJAX.
	- Incluir os Javascripts no diretório `static`.
	- Incluir o HTML no diretório `templates`.
2. Altere o jQuery para usar o método `jQuery.getJSON()` no lugar de `$.ajax()`.

# O método $.post()

- Sintaxe: `$.post( url [, data ] [, success ] [, dataType ] )`
- É o método facilitador que **substitui**:

```{.js .numberLines style="font-size: 24px;"}
$.ajax({
  type: "POST",
  url: url,
  data: data,
  success: success,
  dataType: dataType
});
```

# Exemplo de Uso do $.post() com Flask: o HTML (I)

- Voltaremos ao exemplo de **login** de um sistema web.
- Primeiramente, adicionar os scripts de jQuery no head.
- Vamos alterar o HTML para remover a tag *form*.

```{.html .numberLines style="font-size: 20px;"}
<html>
    <head>
        <script type=text/javascript src="{{ url_for('static', filename='jquery.js') }}"> </script>
        <script type=text/javascript src="{{ url_for('static', filename='meu_ajax.js') }}"> </script>
        <script type=text/javascript>
            $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
        </script>
    </head>
	<body>...
</html>
```

# Exemplo de Uso do $.post() com Flask: o HTML (II)

- Em seguida, alterar o HTML para remover a tag *form*.
	- Não queremos submiter um *form* do modo convencional!
	- Trocar botão de *submit* para *button*.

```{.html .numberLines style="font-size: 20px;"}
    <body>
        <h1>Bem-vindo ao sistema!</h1>

        Por favor, forneça suas credenciais:<br>
        <div class=container>
            <span id="msgErro" style="color: brown;"> </span> <br>
            <label for="username">Nome de utilizador:</label><br>
            <input type="text" id="username" name="username" value=""><br>
            <label for="password">Palavra-passe:</label><br>
            <input type="password" id="password" name="password" value=""><br><br>
            <input type="button" id="btnEnviar" value="Enviar">
        </div>
    </body>
```

# Exemplo de Uso do $.post() com Flask: o Javascript

```{.js .numberLines style="font-size: 20px;"}
function tratar_recv(data){
	if (data['success'] == false){
		$("#msgErro").text("Nome de utilizador e palavra-passe não correspondem! Tente novamente!");
	}
	else{
		// Redireciona página para valor indicado pelo servidor
    	$(location).prop('href', data['redirect']);
		//window.location.href = data['redirect']; // Sem jQuery
	}
}

function submeter_form(){
	valor_usr = $('input[name="username"]').val();
	valor_pwd = $('input[name="password"]').val();
	json_send = {user: valor_usr, pwd: valor_pwd};
	$.post($SCRIPT_ROOT + '/login', json_send, tratar_recv, 'json');
}

$(function() {
    $('#btnEnviar').click(submeter_form);
});
```

# Exemplo de Uso do $.post() com Flask: o Python

```{.Python .numberLines style="font-size: 20px;"}
@app.route("/login", methods=['GET', 'POST'])
def login():
	# Se utilizador já está logado, apenas redirecionamos para página principal.
    if 'username' in session:
        return redirect(url_for('principal'))
    # Trata mensagem de login do AJAX:
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']
        print(user, pwd)
        if verificaLogin(user, pwd):
            session['username'] = user
            return jsonify({'success':True, 'redirect':url_for('principal')})
        else:
            return jsonify({'success':False})
    return render_template('login.html')
```

# Atividades (II)

1. Incluir comunicação AJAX em seu sistema de login.

# Exemplo de Upload de Ficheiro: Breve Descrição

- No HTML, podemos usar a tag *form*.
	- input com tipo 'file' e atributo *multiple* (permite incluir múltiplos ficheiros).
	- Vamos sobrescrever o *submit* do formulário.
		- `event.preventDefault()` impede que submit padrão seja executado.
- No jQuery + AJAX, o *form* será serializado para enviar para o servidor.
	- Usao do *formData* do Javascript.
	- `serialize()` não funciona para incluir os ficheiros!
- No Python, os dados dos ficheiros podem ser obtidos por `request.files`.
	- `request.files.getlist('input_file_name')`: retorna uma lista com os nomes dos ficheiros.
		- 'input_file_name' corresponde ao nome do input do tipo *file* no formulário do HTML.
	- Usaremos `request.files.saves(nome_ficheiro)` para gravar ficheiro no servidor.

# Exemplo de Upload de Ficheiro: HTML

```{.html .numberLines style="font-size: 20px;"}
<html>
	<head>
		<title> Upload de Ficheiro </title>
		<script type=text/javascript src="{{ url_for('static', filename='jquery.js') }}"> </script>
		<script type=text/javascript src="{{ url_for('static', filename='funcoes.js') }}"> </script>
		<script type=text/javascript>
			$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
		</script>
	</head>
	<body>
		<h1>Upload de ficheiro com jQuery com AJAX:</h1>
		<form id="meu_form">
			<input type="file" name="ficheiros" multiple>
			<input type="submit" id="botaoEnviar" value="Enviar">
		</form>
		<br>
		<span id="msg"> </span>
	</body>
</html>
```

# Exemplo de Upload de Ficheiro: Javascript

```{.js .numberLines style="font-size: 20px;"}
function tratar_recv(data){
	$("#msg").text("Ficheiros armazenados com sucesso!");
}

function upload2server(event){
  event.preventDefault(); // Impede que os comandos padrões do submit aconteçam.
  var formData = new FormData(this); //serialize não funciona para ficheiros
  $.ajax({
    url : $SCRIPT_ROOT + '/upload',
    type : "POST",
    data : formData,
    contentType : false, // necessário para não setar nenhum header
    processData : false, // necessário para não processar objeto como string
    success : tratar_recv
  });
}

$(function() {
    $("#meu_form").submit(upload2server);
});
```

# Exemplo de Upload de Ficheiro: Python + Flask

```{.Python .numberLines style="font-size: 20px;"}
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        for ficheiros in request.files.getlist('ficheiros'):
            print("File", ficheiros.filename)
            if ficheiros.filename != '':
                ficheiros.save(ficheiros.filename)
        return jsonify(success=True)
    except Exception:
        return jsonify(success=False)


@app.route('/')
def index():
    return render_template('index.html')

# Inicio do programa:
if __name__ == "__main__":
    app.run(debug=True)
```

# Atividades (III)

1. Reproduza e teste o exemplo de upload de ficheiro.