#16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
#elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
#elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
#Escrever as listas X e Y.
X = []
for i in range(10):
    X.append((int(input())))
Y = list(range(10))
for i in range(len(Y)):
    if i % 2 == 0:
        Y[i] = X[i]/2
    elif i % 2 != 0:
        Y[i] = X[i]*3
print(f'{X}\n{Y}')