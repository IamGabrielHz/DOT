def cubo():
    while True:
        num = int(input('Insira um número que queira que deseja elevar ao cubo: '))
        resposta = input(f'O número {num} ao cubo é {num**3}\nDeseja continuar? S ou N? ').upper()
        if resposta == 'S':
            continue
        elif resposta == 'N':
            break
        else:
            print('Caractere inválido. Digite novamente.')
if __name__ == '__main__':
    cubo()