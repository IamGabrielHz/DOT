#18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
#uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
X = []
for i in range(10):
    X.append((int(input())))
R = []
for i in range(len(X)):
    if X[i] < 0:
        R.append(X[i])
print(f'Lista X: {X}\nLista R: {R}')