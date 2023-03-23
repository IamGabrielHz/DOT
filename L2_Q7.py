import random
lista = list(random.sample(range(1, 101), 10))
verif = int(input('Insira o valor que quer verificar se está na lista: '))
if verif in lista:
    print(f'O número {verif} está na lista.')
else:
    print(f'O número {verif} não está na lista.')
