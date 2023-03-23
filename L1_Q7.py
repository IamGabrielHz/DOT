# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.
def fato(num):
    resultado = 1
    count = 1

    while count <= num:
        resultado *= count
        count += 1
    return resultado


def main():
    num = int(input())
    print(fato(num))


if __name__ == '__main__':
    main()
