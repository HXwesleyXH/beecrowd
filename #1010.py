"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
Entrada

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
Saída

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
"""


partOne = input().split()
partTwo = input().split()

cod1, qnt1, price1 = partOne
cod2, qnt2, price2 = partTwo

total = (int(qnt1)) * (float(price1)) + (int(qnt2)) * (float(price2))

print("VALOR A PAGAR: R$ %0.2f" % total)