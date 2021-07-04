# Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
#
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer
# • Ler a minha escolha (Pedra, papel ou tesoura)
# • Decidir de forma aleatória a decisão do computador
# • Mostrar quantas rodadas cada jogador ganhou
# • Determinar quem foi o grande campeão de acordo com a quantidade de 
#   vitórias de cada um (computador e jogador)
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
#   de quantidade de rodadas, se não finalize o programa.
from utilities.utilities import Utilities
from random import randrange
from art import *
from time import sleep
### Rock Paper Scissors ###


class Jokenpo:
    
    def welcome(self):
        tprint('Vamos jogar', font='small')
        tprint('JoKenPo?')
        sleep(3)

    def userName(self):
        print('|================================')
        self.__userName = str(input('| Por favor, me diga o seu nome: ')).strip().capitalize()
        return self.__userName
    
    def start(self, userName):
        clear = Utilities()
        self.__userName = userName
        options = ['Pedra','Papel','Tesoura'] # Jokenpo options
        while True:
            # Show options to user and let him/her to pick one
            # Execute until user do enter a numeric value
            while True:
                print('|','='*len(self.__userName),'======================================|')
                rounds = str(input(f'| {self.__userName}, digite quantas rodadas deseja jogar: ')).strip()
                if rounds.isnumeric(): # check if user enter a numeric value
                    if rounds == '0': break
                    if int(rounds) > 5: # avoid to the choice a huge number of rounds
                        print('-'*55)
                        check = str(input(f'Você tem certeza que quer jogar {int(rounds)} rodadas [Sim ou Não]? ')).strip().lower()[0]
                        if check == 's':
                            for p in '...': print(p),sleep(0.5)
                            break
                        else:
                            print('Tente novamente\n')
                            for p in '...': print(p),sleep(0.5)
                            clear.clearTerminal()
                            continue
                    else:
                        for p in '...': print(p),sleep(0.5)
                        break
                else:
                    print('Opção inválida. Você deve digitar um número inteiro\n')
                    for p in '...': print(p),sleep(0.8)
            clear.clearTerminal()
            draws = wins = losts = 0 
            # Execute until the number of rounds informed above
            for y in range(int(rounds)):
                # Execute until user do the rigth choice
                while True:
                    tprint(f'Round - {y+1}',font='small')
                    if y > 0: 
                        tprint(f'{userName} - {wins}', font='small')
                        tprint(f'Computador - {losts}', font='small')
                    print('|================================|')
                    print('| Escolha uma das opções abaixo  |')
                    print('|================================|')
                    i = 0
                    # Show options
                    for option in options:
                        i += 1
                        print(f'| Digite {i} para: ', end=' ')
                        for opt in option:
                            print(opt, end='')
                        print('\n')
                    print('|================================|')
                    # Pick up user choice
                    choice = str(input('| Digite a sua escolha: ')).strip().lower()[0]
                    computerChoice = randrange(0,len(options)) #Computer choice
                    # If user do not pick up a rigth coiche
                    if choice not in '123':
                        print(' Opção inválida. Você deve digitar 1, 2 ou 3 de acordo com as opções abaixo.\nTente novamente.\n')
                        for p in '...': print(p),sleep(1)
                        clear.clearTerminal()
                    else:
                        userChoice = int(choice)-1
                        print('|================================|')
                        print(f'| A sua escolha foi: {options[userChoice].upper()}')
                        print('|================================|')
                        print(f'| O computador escolheu: {options[computerChoice].upper()}')
                        print('|================================|')
                        for p in '...': print(p),sleep(1)
                        print('|================================|')
                        if userChoice == computerChoice:
                            tprint('Empate')
                            draws += 1
                        elif userChoice == 0 and computerChoice == 2:
                            tprint('Ponto para voce')
                            wins += 1
                        elif userChoice == 1 and computerChoice == 0:
                            tprint('Ponto para voce')
                            wins += 1
                        elif userChoice == 2 and computerChoice == 1:
                            tprint('Ponto para voce')
                            wins += 1
                        else:
                            tprint('Ponto para o computador')
                            losts += 1
                        # print('|================================|')
                        for p in '...': print(p), sleep(1)
                        clear.clearTerminal()
                        break
            # Who wins?
            if wins == losts: winner = 'Deu empate!' # Draw
            elif wins > losts: winner = 'Voce ganhou!!!' # User wins
            else: winner = 'Computador ganhou!' # Computer wins
            # 
            if rounds == '0':
                tprint('Jogo encerrado')
                for p in '...': print(p), sleep(0.6)
                clear.clearTerminal()
                break
            tprint(f'{userName} {wins} x {losts} Computador', font='small')
            tprint(f'{winner}')
            # Ask if user want to play again
            print('|===================================|')
            playAgain = str(input('| Deseja jogar novamente Sim ou Não? ')).strip().lower()[0]
            if playAgain != 's':
                tprint('Jogo encerrado')
                for p in '...': print(p), sleep(0.6)
                clear.clearTerminal()
                break
            for p in '...': print(p, end=' '), sleep(0.6)
            clear.clearTerminal()
            # rounds = '0' # Reset rounds number just in case the user restart the game and give up to play again

