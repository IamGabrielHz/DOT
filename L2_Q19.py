#Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
#cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
#de S. Escrever a lista X.
R = []
for i in range(10):
    R.append((int(input())))
S = []
for i in range(10):
    S.append((int(input())))
X = R + S
print(f'Lista X: {X}')