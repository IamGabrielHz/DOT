#17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
#valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
#aparece.
#Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.
W = []
for i in range(10):
    W.append((int(input())))
V = int(input())
ocorrencias = 0
positions = []
for i in range(len(W)):
    if W[i] == V:
        ocorrencias += 1
        positions.append(i)
if ocorrencias > 0 :
    print(f'O valor {V}, ocorre {ocorrencias} vezes na lista W\nNas posições: {positions}')
elif ocorrencias == 0 :
    print(f'O valor {V} não ocorre nenhuma vez na lista W.')