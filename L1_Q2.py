# Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;
import math
def area(raio):
    ar = math.pi * (2 ** raio)
    return ar
def perimetro(raio):
    pr = math.pi * 2 * raio
    return pr
def main():
    raio = int(input())
    print(f'{area(raio):.2f}')
    print(f'{perimetro(raio):.2f}')
if __name__ == '__main__':
    main()