import random
alfabeto = 'abcdefghijklmnopqrstuvwxyz'.lower()
letras_aleatorias = []
for i in range(10):
    letra = random.choice(alfabeto)
    letras_aleatorias.append(letra)
verif = 'a'
if verif in letras_aleatorias:
    print('A letra "a" está presente nessa lista.')
else:
    print('A letra "a" não está presente nessa lista.')