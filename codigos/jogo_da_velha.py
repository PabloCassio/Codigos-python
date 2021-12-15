partidas = 0
jogador1win = 0
jogador2win = 0
velhas = 0

velha = [[0 for num in range(3)] for x in range(3)]


def menu():
    continuar = 1
    global partidas
    global jogador1win
    global jogador2win
    global velhas
    global velha

    while continuar == 1:
        if partidas == 0 and continuar == 1:
            continuar = (input('Bem-vindo ao Jogo da Velha!!!\n'
                               '_____________________________\n'
                               'Digite:\n'
                               '1- Jogar\n'
                               '0- Sair\n'))
        if continuar == '1':
            jogo()
        if continuar == '0':
            print('Até a próxima!')
            break
        elif continuar != '1' and continuar != '0':
            print('Digite apenas os valores indicados!')
        if partidas > 0:
            continuar = (input(f"Vitórias do jogador 1: {jogador1win}\n"
                               f"Vitórias do jogador 2: {jogador2win}\n"
                               f"Velhas: {velhas}\n"
                               f"Deseja continuar?\n"
                               f"1- Sim\n"
                               f"0- Não\n"))
            if continuar == '1':
                velha = [[0 for num in range(3)] for y in range(3)]
                jogo()
            if continuar == '0':
                print('Até a próxima!')
                partidas = 0
                continuar = 0
                break
            elif continuar != '0' and continuar != '1':
                print('DIGITE APENAS OS VALORES ESPECIFICADOS.')


def jogo():
    jogadas = 0
    global partidas
    global jogador1win
    global jogador2win
    global velhas
    while ganhador() == 0 and jogadas < 9:
        mostra_x_o()

        print(f'\nJogador {jogadas % 2 + 1} escolha:')
        try:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if 0 < linha < 4 and 0 < coluna < 4:
                if velha[linha - 1][coluna - 1] == 0:
                    if jogadas % 2 + 1 == 1:
                        velha[linha - 1][coluna - 1] = 1
                        jogadas += 1
                    else:
                        velha[linha - 1][coluna - 1] = -1
                        jogadas += 1
                else:
                    print('Essa posição não está vazia! Selecione outra.')
            else:
                print('Posição inválida. Verifique os valores selecionados.')
        except ValueError:
            print('Essa posição não é válida! Selecione outra.')

        if ganhador():
            mostra_x_o()
            a = jogadas % 2
            if a == 1:
                jogador1win += 1
                print(f"Jogador 1 ganhou após {jogadas} rodadas")
            if a == 0:
                jogador2win += 1
                print(f"Jogador 2 ganhou após {jogadas} rodadas")
            partidas += 1
            menu()

    if jogadas == 9 and ganhador() == 0:
        print('DEU VELHA!')
        velhas += 1
        partidas += 1
        menu()


def ganhador():
    """verificando linhas"""
    i = 0
    while i <= 2:
        soma = velha[i][0] + velha[i][1] + velha[i][2]
        if soma == 3 or soma == -3:
            return 1
        else:
            i += 1
    """verificando colunas"""
    for j in range(3):
        soma = velha[0][j] + velha[1][j] + velha[2][j]
        if soma == 3 or soma == -3:
            return 1
    """verificando diagonais"""
    diagonal1 = velha[0][0] + velha[1][1] + velha[2][2]
    diagonal2 = velha[2][0] + velha[1][1] + velha[0][2]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def mostra_x_o():
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 0:
                print("_", end=' ')
            elif velha[i][j] == 1:
                print("X", end=' ')
            elif velha[i][j] == -1:
                print("O", end=' ')
        print()


menu()
