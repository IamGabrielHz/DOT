#9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
#uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
import random
lista_x = list(random.sample(range(1, 101), 5))
lista_y = list(reversed(lista_x))
print(f'{lista_x}\n{lista_y}')
