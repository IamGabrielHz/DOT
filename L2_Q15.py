#15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
#inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
#por diante. Escrever todo a lista D e todo a lista E.
D = []
for i in range(10):
    D.append((int(input())))
E = list(reversed(D))
print(f'{D}\n{E}')