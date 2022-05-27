function tratar_recv(data){
	$("#msg").text("Ficheiros armazenados com sucesso!");
  console.log("data.success: " + data.success);
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

