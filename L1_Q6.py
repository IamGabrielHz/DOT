# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
def poli(lados):
    if lados == 3:
        print(f'TRIÂNGULO\n{3*lados}')
    elif lados == 4:
        print(f'QUADRADO\n{lados*lados}')
    elif lados == 5:
        print(f'PENTÁGONO')


def main():
    lados = int(input('Insira o lado do seu poligono:'))
    poli(lados)


if __name__ == '__main__':
    main()
