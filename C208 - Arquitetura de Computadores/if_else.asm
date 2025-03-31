.data
f1: .asciiz "$t2 maior que $t1"
f2: .asciiz "$t1 maior que $t2"
.text
li $t1, 0x20
li $t2, 0x10
bge $t2, $t1, maior # if($t2 > $t1)
    la $a0, f2
    li $v0, 4
    syscall
    j fim
maior:
    la $a0, f1
    li $v0, 4
    syscall
fim:
    li $v0, 10
    syscall