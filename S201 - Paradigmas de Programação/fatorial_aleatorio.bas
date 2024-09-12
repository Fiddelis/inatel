20 LET numero = INT(RND(TIMER)*10)
30 PRINT "O número aleatório é: ", numero

40 LET fatorial = numero
45 LET num = numero - 1
50 FOR i = 1 TO numero
60    LET fatorial = fatorial * num
65    LET num = num - 1
70 NEXT i
80 PRINT "O fatorial de ", numero," é ", fatorial
