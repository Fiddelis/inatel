# a = 10
# b = 20
# x = 1
# while(a != b) {
#    a++;
#    b--;
#    print("Iteração: " + x)
#    x++;
# }

.data
f: .asciiz "iteracao: "
n: .asciiz "\n"
.text
li $t0, 10	# a = 10
li $t1, 20	# b = 20
li $t2, 1	# x = 1

volta:
bne $t0, $t1, while	# condição do while
j fim

while: 	addi $t0, $t0, 1	# a++
	addi $t1, $t1, -1	# b--
    
    	la $a0, f		# print("Interacao: ")
    	li $v0, 4
    	syscall
    
    	add $a0, $0, $t2	# print(x)
    	li $v0, 1
    	syscall
    
    	la $a0, n		# print("\n")
    	li $v0, 4
    	syscall
    
    	addi $t2, $t2, 1	# x++
    	j volta

fim:	li $v0, 10
    	syscall
    