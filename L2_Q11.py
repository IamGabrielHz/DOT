lista = []
while True:
    select = input('''
        ========MENU========
        1)Cadastar nome
        2)Pesquisar nome
        3)Listar todos os nome
        0) Sair do programa
        ——————–——————–
        Digite sua escolha:_
        ''')
    if select == '1':
        lista.append(input('Insira um nome: '))
        print('O nome foi inserido!')
    elif select == '2':
        lista[int(input('Insira o índice do nome que você deseja consultar: '))]
    elif select == '3':
        for indice,nome in enumerate(lista):
            print (f'Índice: {indice} - Nome: {nome}')
    elif select == '0':
        break