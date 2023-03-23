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