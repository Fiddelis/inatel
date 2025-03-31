.data
frase1: .asciiz "Entre com o primeiro numero: "
frase2: .asciiz "Entre com o segundo numero: "
frase3: .asciiz "Media = "
.text
################ ENTRADA DO 1° VALOR ################
la $a0,frase1 	# carregando a frase
li $v0,4 	# carregando o código de serviço print_string
syscall
li $v0,5 	# carrega o código de serviço read_int
syscall
add $s0,$0,$v0
################ ENTRADA DO 2° VALOR ################
la $a0,frase2 	# carregando a frase
li $v0,4 	# carregando o código de serviço print_string
syscall
li $v0,5 	# carrega o código de serviço read_int
syscall
add $s1,$0,$v0
################ PROCESSAMENTO ################
add $t1,$s0,$s1
srl $t2,$t1,1
################ SAIDA DE DADOS ################
la $a0,frase3
li $v0,4
syscall
add $a0,$0,$t2
li $v0,1
syscall
