import random
lancamentos = [random.randint(1, 6) for _2 in range(int(input()))]
ocorrencias = []
for i in range(1,7):
    ocorrencias.append(lancamentos.count(i))
for i in range(6):
    print(f'Face {i+1}: {ocorrencias[i]}')