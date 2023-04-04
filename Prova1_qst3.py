def perfect():
    num = int(input('Insira um número para verificar se ele é perfeito: '))
    divisores = 0 
    for i in range(0,num):
        if num % i == 0:
            divisores += 1
        if divisores == num:
            return True
        else:
            return False
while True:        
    try:
        num = int(input())
        if perfect(num):
            print(f'O número {num} é perfeito.')
        else:
            print(f'O número {num} não é perfeito.')
            break
    except ValueError:
        print('Você inseriu um valor inválido. Digite novamente!')

