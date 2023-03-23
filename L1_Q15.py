# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)


def expand(t):
    x = 2
    y = 4
    soma = 0
    while x/y <= (t**2+1)/(t+3):
        soma += x/y
        x += 3
        y += 1 
    return soma


def main():
    N = int(input())
    result = expand(N)
    print(result)


if __name__ == '__main__':
    main()