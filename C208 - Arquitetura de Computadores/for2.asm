# for j=1; j<10; j++
#     print ("INATEL")
#     print(j)
.data
f: .asciiz "INATEL\n"
.text
la $a0, f
li $v0, 4
li $t1, 1 #    j=1
loop:
    syscall
    addi $t1, $t1, 1    # j++
    blt $t1, 10, loop   # j < 10