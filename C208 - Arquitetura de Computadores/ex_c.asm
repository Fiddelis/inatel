# c)	leia dois valores numericos inteiros e, em seguida, a operação a ser realizada entre eles (soma, subtração, divisão, ou multiplicação),
# 	Caso o usuario digite "O", o programa deverá ser encerrado.

.data
f1: .asciiz "Entre com o primeiro valor: "
f2: .asciiz "Entre com o segundo valor: "
f3: .asciiz "Entre com a operacao (1=soma, 2=subtracao, 3=divisao, 4=multiplicacao): "
res: .asciiz "Resultado: "
.text
la $a0, f1		# print("Entre com o primeiro valor: ")
li $v0, 4
syscall

li $v0, 5
syscall
add $t0, $0, $v0	# read(a)

la $a0, f2		# print("Entre com o segundo valor: ")
li $v0, 4
syscall

li $v0, 5
syscall
add $t1, $0, $v0	# read(b)

la $a0, f3		# print("Entre com a operacao (1=soma, 2=subtracao, 3=divisao, 4=multiplicacao): ")
li $v0, 4
syscall

li $v0, 5
syscall
add $t2, $0, $v0	# read(operacao)

la $a0, res		# print("Resultado: ")
li $v0, 4
syscall

li $v0, 1
beq $t2, 1, soma
beq $t2, 2, subt
beq $t2, 3, divi
beq $t2, 4, multi

j fim
soma:	add $a0, $t0, $t1
	syscall
	j fim
subt:	sub $a0, $t0, $t1
	syscall
	j fim
divi:	div $a0, $t0, $t1
	syscall
	j fim
multi:	mul $a0, $t0, $t1
	syscall
fim: 	li $v0, 10
	syscall