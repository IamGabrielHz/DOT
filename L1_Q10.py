#Escreva um programa composto de uma função Max e o programa principal como segue:
import random


def max(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return random(n1, n2)


def main():
    for n in range(4):
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        num_ab = max(a,b)
        num_cd = max(c,d)
        final = max(num_ab,num_cd)
        print(final)


if __name__ == '__main__':
    main()
