function tratar_recv(data){
  console.log("data.sucesso: " + data);
  if (data['success'] == false){
	  $("#msgErro").text("Nome de utilizador e palavra-passe não correspondem! Tente novamente!");
  }
  else{
    //window.location.href = data['redirect'];
    $(location).prop('href', data['redirect']);
  }
}

function submeter_form(){
	valor_usr = $('input[name="username"]').val();
	valor_pwd = $('input[name="password"]').val();
	json_send = {user: valor_usr, pwd: valor_pwd};
  console.log(json_send);
  $.post($SCRIPT_ROOT + '/login', json_send, tratar_recv, 'json');
  /*$.ajax({
    url: $SCRIPT_ROOT + '/login',
    type: 'POST',
    dataType: 'json',
    data: json_send,
    success: tratar_recv
  });*/
	return false;
}

$(function() {
    $('#btnEnviar').click(submeter_form);
});

