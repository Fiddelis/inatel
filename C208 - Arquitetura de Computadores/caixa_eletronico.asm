.data
f1: .asciiz "valor a ser sacado: "
f50: .asciiz "notas de 50: "
f20: .asciiz "notas de 20: "
f10: .asciiz "notas de 10: "
n: .asciiz "\n"
.text
la $a0,f1
li $v0,4
syscall

li $v0, 5
syscall
add $s0, $0, $v0

loop:
bge $v0, 50, nota50
bge $v0, 20, nota20
bge $v0, 10, nota10
j fim

nota50:	addi $s1, $s1, 1
	addi $v0, $v0, -50
	j loop
nota20:	addi $s2, $s2, 1
	addi $v0, $v0, -20
	j loop
nota10: addi $s3, $s3, 1
	addi $v0, $v0, -10
	j loop

fim:	la $a0, f50
	li $v0, 4
	syscall
	add $a0,$0,$s1
	li $v0, 1
	syscall
	la $a0, n
	li $v0, 4
	syscall
	
	la $a0, f20
	li $v0, 4
	syscall
	add $a0, $0, $s2
	li $v0, 1
	syscall
	la $a0, n
	li $v0, 4
	syscall
	
	la $a0, f10
	li $v0, 4
	syscall
	add $a0, $0, $s3
	li $v0, 1
	syscall
	la $a0, n
	li $v0, 4
	syscall