#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
def main():
    num = int(input())
    count = 1
    som = 1
    while num > count:
        count += 1
        som += count
    print(som)


if __name__ == '__main__':
    main()
