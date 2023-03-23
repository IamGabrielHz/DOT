# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
def main():
    while True:
        num = int(input())
        print(num**3)
        caracter = input() .upper()
        if caracter == 'S':
            continue
        elif caracter == 'N':
            break
        else:
            print('Caractere inválido! Digite novamente.')
            break

if __name__ == '__main__':
    main()
