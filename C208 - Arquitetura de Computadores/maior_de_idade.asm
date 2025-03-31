.data
frase0: .asciiz "Digite sua idade:"
frase1: .asciiz "Maior de idade"
frase2: .asciiz "Menor de idade"
.text
addi $s0, $0, 18

la $a0,frase0 	# carregando a frase
li $v0,4 	# carregando o código de serviço print_string
syscall
li $v0,5 	# carrega o código de serviço read_int
syscall
add $s1,$0,$v0

bge $s1, $s0, verdadeiro # if $s1 >= $s0 than

la $a0,frase2 	# carregando a frase
li $v0,4 	# carregando o código de serviço print_string
syscall
j fim		# pula pro final

verdadeiro:
la $a0,frase1 	# carregando a frase
li $v0,4 	# carregando o código de serviço print_string
syscall

fim:
li $v0, 10	# carreg o código de serviço exit
syscall