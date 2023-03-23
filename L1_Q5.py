# Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).
def pesoideal(altura,sexo):
    if sexo == '1':
        pi = (62.1 * altura) - 44.7
    elif sexo == '2':
        pi = (72.7 * altura) - 58
    return pi
def main():
    h = float(input('Insira a sua altura:'))
    sx = input('Insira seu sexo:')
    if sx == 'feminino' or 'f' or 'mulher':
        sx = '1'
    elif sx == 'masculino' or 'm' or 'homem':
        sx = '2'
    psi = pesoideal(h,sx)
    print(f'Seu peso ideal é {psi:.0f}.')
if __name__ == '__main__':
    main()