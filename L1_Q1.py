# Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
def par(n1):
    verif = bool(0)
    if n1 % 2 == 0:
        verif = True
    else:
        verif = False
    return verif
def main():
    num = int(input())
    print(par(num))
if __name__ == '__main__':
    main()