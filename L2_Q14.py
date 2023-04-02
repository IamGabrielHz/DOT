#14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
#Escrever a lista C modificada.
C = []
for i in range(10):
    C.append((int(input())))
for i in range(len(C)):
    if C[i] < 0:
        C[i] = 0
print(C)