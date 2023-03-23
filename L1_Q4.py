# Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).
def media(nt1,nt2):
    rst = (nt1 + nt2)/2
    return rst
def main():
    nt1 = int(input())
    nt2 = int(input())
    rst = media(nt1,nt2)
    if rst >= 6:
        print(f'{rst}\nPARABÉNS!Você foi aprovado!')
    else:
        print(f'{rst}\nVocê foi reprovado!')
if __name__ == '__main__':
    main()