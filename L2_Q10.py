import random
lista = list(random.sample(range(1, 101), 15))
maior = lista[0]
menor = lista[0]
indice_maior = 0
indice_menor = 0
for i in range(len(lista)):
    if lista[i] > maior:
        indice_maior = i
        maior = lista[i]
for i in range(len(lista)):
    if lista[i] < menor:
        indice_menor = i
        menor = lista[i]
print(f'O maior número da lista é {maior} e o seu índice é {indice_maior}.\nO menor número da lista é {menor} e o seu índice é {indice_menor}.')
print(lista)
