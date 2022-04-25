"""

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (A+B+abs(A-B))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
Entrada

O arquivo de entrada contém três valores inteiros.
Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""


entrada = (input()).split()
var1, var2, var3 = entrada
calc1 = (int(var1) + int(var2) + abs(int(var1) - int(var2))) / 2
calc2 = (int(calc1) + int(var3) + abs(int(calc1) - int(var3))) / 2

print("%0.00f" % calc2,  "eh o maior")