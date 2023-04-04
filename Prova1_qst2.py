def somar(n1,n2):
    soma = 0
    for i in range(n1,n2+1):
        soma += i 
    return soma
while True:
    try:
        n1 = int(input('Insira um número 1:'))
        n2 = int(input('Insira um número 2:'))
        if n1 < n2:
            print(somar(n1,n2))
            break
        else:
            print('O número 1 deve ser maior que o número 2. Digite novamente!')
    except ValueError:
        print('Valor inválido. Digite novamente!')


if __name__ == '__main___':
    somar()