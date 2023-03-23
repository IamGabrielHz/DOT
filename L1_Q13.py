# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.


def calc(n):
    S = 1 + (1/2) + (1/3) + (1/4) + (1/5) + (1/n)
    return S


def main():
    N = int(input())
    result = calc(N)
    print(result)


if __name__ == '__main__':
    main()