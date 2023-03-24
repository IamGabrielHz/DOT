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