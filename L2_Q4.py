#4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
#a) O maior elemento da lista e em que posição esse elemento se encontra;
#b) O menor elemento da lista e em que posição esse elemento se encontra.
import random
numeros = []
for i in range(15):
    numeros.append(round(random.uniform(-10, 10),2))
print(numeros)
maior = numeros[0]
posicao_maior = 0
menor = numeros[0]
posicao_menor = 0

for i in range(1, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao_maior = i
    if numeros[i] < menor:
        menor = numeros[i]
        posicao_menor = i

print(f'O maior número é {numeros[posicao_maior]} e sua posição é {posicao_maior}.')
print(f'O menor número é {numeros[posicao_menor]} e sua posição é {posicao_menor}.')
