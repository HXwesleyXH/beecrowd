"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""


saque = int(input())

dinheiro = saque
cem = cinquenta = vinte = dez = cinco = dois = um = 0

if int(saque/100) >= 1:
    cem = int(saque/100)
    saque -= cem*100

if int(saque/50) >= 1:
    cinquenta = int(saque/50)
    saque -= cinquenta*50

if int(saque/20) >= 1:
    vinte = int(saque/20)
    saque -= vinte*20

if int(saque/10) >= 1:
    dez = int(saque/10)
    saque -= dez*10

if int(saque/5) >= 1:
    cinco = int(saque/5)
    saque -= cinco*5

if int(saque/2) >= 1:
    dois = int(saque/2)
    saque -= dois*2

if int(saque/1) >= 1:
    um = int(saque/1)
    saque -= um*1

print("%d" % dinheiro)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinquenta)
print("%d nota(s) de R$ 20,00" % vinte)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cinco)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)