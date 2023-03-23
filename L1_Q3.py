# Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5
def celcius(temp):
    c = ((temp - 32)/9) * 5
    return c
def main():
    temp_f = float(input())
    print(f'{celcius(temp_f):.0f}')
if __name__  == '__main__':
    main()