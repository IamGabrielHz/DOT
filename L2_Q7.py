#7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
#outro valor dado pertence ou não à lista.
import random
lista = list(random.sample(range(1, 101), 10))
verif = int(input('Insira o valor que quer verificar se está na lista: '))
if verif in lista:
    print(f'O número {verif} está na lista.')
else:
    print(f'O número {verif} não está na lista.')
