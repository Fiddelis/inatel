10 PRINT "Digite os valores de a, b e c:"

20 INPUT "a:"a
30 INPUT "b:"b
40 INPUT "c:"c

50 LET delta = b^2 - 4 * a * c
60 IF delta < 0 THEN
70    PRINT "A equação não possui raízes reais."
80 ELSEIF delta = 0 THEN
90   LET x = -b / (2 * a)
100   PRINT "A equação possui uma raiz real: ", x
110 ELSE
120   LET x1 = (-b + SQR(delta)) / (2 * a)
130   LET x2 = (-b - SQR(delta)) / (2 * a)
140   PRINT "A equação possui duas raízes reais: ",x1," e ",x2
150 END IF