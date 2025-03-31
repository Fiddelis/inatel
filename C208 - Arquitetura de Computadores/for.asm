# for j = 1; j < 10; j++
.data
f: .asciiz "."
.text
li $t1, 1
label:
    la $a0, f
    li $v0, 4
    syscall
    addi $t1, $t1, 1
    blt $t1, 10, label