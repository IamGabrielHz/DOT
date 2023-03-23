#Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
def main():
    num = int(input())
    count = 1
    div = 0
    while count <= num:
        if num % count == 0:
            div += 1
            count += 1
        else:
            count += 1
    print(div)


if __name__ == '__main__':
    main()
