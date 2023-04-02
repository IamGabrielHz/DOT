#1)Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
#a) Mostre a quantidade de números pares;
#b) Grave uma lista somente com os números pares e mostre a lista;
#c) Mostre a quantidade de números ímpares;
#d) Grave uma lista somente com os números ímpares e mostre a lista.
lista = list(range(101))
soma_par = 0
soma_impar = 0
par = []
impar = []
for i in lista:
	if i % 2 == 0 :
		soma_par += 1
		par.append(i)
print(f'A quantidade de numero pares é {soma_par}.')
print(par)
for i in lista:
	if i % 2 != 0 :
		soma_impar += 1
		impar.append(i)
print(f'A quantidade de numero impares é {soma_impar}.')
print(impar)