; Programa que realiza divis�es inteiras
; Assume dividendo na posi��o 100 e divisor 
; na posi��o 104. Quociente � guardado em 108.
; Resto em 112.
; Assume que registradores est�o zerados.
; Utiliza processo de subtra��es sucessivas.

; Carregar um ponteiro com endere�o base dos
; operandos.
addi $0, $0, 100

; Ler valores dos operandos
; Durante a execu��o:
;  - $1 acumula o quociente.
;  - $2 guarda o dividendo.
;  - $3 guarda o divisor.
;  - $4 � usado para compara��es.
;  - $5 � usado como 0 para refer�ncia.
lw $2, 0($0)
lw $3, 4($0)

TESTE:
; Teste: dividendo � menor que divisor?
slt $4, $2, $3
beq $4, $5, SUBTRACAO

; Fim do algoritmo. Vamos salvar o quociente e o resto.
sw $1, 8($0)
sw $2, 12($0)
FIM:
j FIM ; loop infinito no final do programa

SUBTRACAO:
; Aqui, subtra�mos o dividendo do divisor e 
; voltamos para o teste.
sub $2, $2, $3
addi $1, $1, 1
j TESTE
