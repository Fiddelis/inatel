.data
frase1: .asciiz "entrou no IF"
frase2: .asciiz "não entrou no IF"
.text
addi $t1, $0, 30
addi $t2, $0, 20
beq $t1, $t2, verdadeiro 	## if $t1 == $t2 than pula para label(verdadeiro)
la $a0, frase2
li $v0, 4
syscall
j fim

verdadeiro:
la $a0, frase1
li $v0, 4
syscall

fim:
li $v0, 10
syscall
