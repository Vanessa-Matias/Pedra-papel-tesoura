#biblioteca para fazer o computador sortear números aleatórios
from random import randint

#biblioteca para fazer a interação do jokenpoo aparecer com time de 1 segundo de delay
from time import sleep

#biblioteca para colocar emojis na interação
import emoji

while True:
    itens = ('PEDRA', 'PAPEL','TESOURA')
    computador = randint(0,2)
    print('{:=^55}'.format(' PEDRA-PAPEL-TESOURA '))
    print(emoji.emojize('Suas opções:\n[ 0 ] \033[1;35mPEDRA\033[m 🤛' ))
    print(emoji.emojize('[ 1 ] \033[1;33mPAPEL\033[m 🫲'))
    print(emoji.emojize('[ 2 ] \033[1;36mTESOURA\033[m ✌️'))
    jogador = int(input('Qual é a sua jogada: '))

    #verificar se a jogada do usuário é válida entre 0,1 ou 2
    if jogador not in (0,1,2):
        print('\033[1;31mJOGADA INVÁLIDA!\nJOGUE NOVAMENTE\033[m')
        continue
    else:
        # Exibe a interação JO KEN POO!!!
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print(emoji.emojize('POO!!!'))
        print('.' * 30)
        print('Computador jogou: {}'.format(itens[computador]))
        print('Jogador jogou: {}'.format(itens[jogador]))
    print('.' * 30)

    # computador jogou PEDRA
    if computador == 0:
        if  jogador == 0:
            print('\033[1;33mEMPATE!\033[m')
            print(emoji.emojize('😐'))
        elif jogador == 1:
            print('\033[1;32mJOGADOR(A) VENCEU!\033[m')
            print(emoji.emojize('😃'))
        elif jogador == 2:
            print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
            print(emoji.emojize('😭'))

    #computador jogou PAPEL
    elif computador == 1:
        if jogador == 0:
            print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
            print(emoji.emojize('😭'))
        elif jogador == 1:
            print('\033[1;33mEMPATE!\033[m')
            print(emoji.emojize('😐'))
        elif jogador == 2:
            print('\033[1;32mJOGADOR(A) VENCEU!\033[m')
            print(emoji.emojize('😄'))

    #computador jogou TESOURA
    elif computador == 2:
        if jogador == 0:
            print('\033[1;32mJOGADOR(A) VENCEU!\033[m')
            print(emoji.emojize('😃'))
        elif jogador == 1:
            print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
            print(emoji.emojize('😭'))
        elif jogador == 2:
            print('\033[1;33mEMPATE!\033[m')
            print(emoji.emojize('😐'))
    #loop interno para fazer o usuário digitar a opção de escolha certa
    while True:
        #perguntar se o jogador deseja porsseguir jogando
        jogar_novamente = input('''\nVocê deseja jogar novamente?
        [ 1 ] \033[1;32mSim\033[m
        [ 2 ] \033[1;31mNão\033[m ''')
        print('.' * 30)

        #validação de escolha do úsuario se é sim ou não
        if jogar_novamente not in ("1", "2"):
            print('\033[1;31mOPÇÃO INVÁLIDA!.\nTente novamente.\033[m')
        else:
            break

    #encerramento do jogo
    if jogar_novamente != "1":
        print(emoji.emojize('\033[1;35mObrigado(a) por jogar comigo!\nAté a próxima!\033[m 👋'))
        print('=' * 30)
        break


