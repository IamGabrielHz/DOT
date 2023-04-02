#12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
#prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
#Para isso são dados:
#o cartão gabarito;
#o número de alunos da turma;
#o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
def contar_acertos(gabarito, respostas):
    return sum([1 for i in range(30) if gabarito[i] == respostas[i]])

def main():
    gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    num_alunos = 2
    cartao_resposta = [
    ['1', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    ['2', 'A', 'D', 'C', 'E', 'A', 'A', 'B', 'C', 'D', 'C', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    ]
    for i in range(num_alunos):
        numero_aluno = cartao_resposta[i][0]
        respostas = cartao_resposta[i][1:]        
        acertos = contar_acertos(gabarito, respostas)
        print(f'O aluno {numero_aluno} acertou {acertos} questões.')

if __name__ == '__main__':
    main()