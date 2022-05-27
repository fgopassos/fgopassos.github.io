function tratar_sucesso(data){
	$("#resultado").text(data.resultado);
}

function calcular_server(){
	valor_a = $('input[name="a"]').val();
	valor_b = $('input[name="b"]').val();
	json_send = {a: valor_a, b: valor_b};
	//$.getJSON($SCRIPT_ROOT + '/soma', json_send, tratar_sucesso);
	$.ajax({
		url: $SCRIPT_ROOT + '/soma',
		dataType: "json",
		data: json_send,
		type: "GET",
		success: tratar_sucesso
	});
}

$(function() {
	$('#botaoSoma').click(calcular_server);
});

