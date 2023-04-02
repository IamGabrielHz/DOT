#2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
#de números negativos e a soma dos números positivos dessa lista.
import random
numeros = []
for i in range(10):
    numeros.append(round(random.uniform(-10, 10),2))
qtd_neg = 0
soma = 0
for i in numeros:
    if i < 0:
        qtd_neg += 1
    else:
        soma += 1 
print(f'A quantidade de números negativos presentes nessa lista é {qtd_neg}.')
print(f'A soma dos números positivos dessa lista é {soma}.')
