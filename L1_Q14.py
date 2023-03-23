# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!


def fato(num):
    resultado = 1
    count = 1

    while count <= num:
        resultado *= count
        count += 1
    return resultado


def calc(n):
    s = 1 + (1/fato(2)) + (1/fato(3)) + (1/fato(46)) + (1/fato(5)) + (1/fato(n))
    return s


def main():
    N = int(input())
    result = calc(N)
    print(result)


if __name__ == '__main__':
    main()