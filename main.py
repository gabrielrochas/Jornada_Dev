# Importações das classes para a main.
from relogio import Relogio
from lista import ListaOpcoes
from mensagens import Msg
from personagem import Personagem

from time import sleep #Sleep para temporalizar as mensagens das opções escolhidas.
import os

class Main():
    def clear(self):
        return os.system('cls' if os.name == 'nt' else 'clear') # Os.system para a limpeza do terminal.

    '''Não mexa!!!!'''
    # def loading(self, seg):
    #     print('Carregando', end= ' ')
    #     for p in '...':
    #         print(p, end=' '),sleep(seg)
    #     print()
    '''Deixa desse jeito!!!'''

if(__name__ == '__main__'): # Função main para inicio de execução do projeto.
    clear = Main()

    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    
    checkJanta = True
    while personagem.xp <= 30:
        if personagem.xp == 20: # Contabilização do desempenho do personagem baseado no XP.
            clear.clear()
            print('Muito bem, você passou!!!!')
            sleep(3)
            clear.clear()
            
        else:
            lista = ListaOpcoes(horas = relogio.horas, minutos = relogio.minutos, descanso = personagem.descansar)
            clear.clear()
            print('---')
            print('São '+str(relogio)+' do '+str(dia)+'º dia na Blue. Você tem que estar pronto para assistir a aula até às 07:00 pm.') #Mensagem incial do programa.
            print('---')
            print()
            print(personagem)
            print('---')
            mainLista = lista.lista
            
            # Estrutra de condicionais para execução ordenada de ações do personagem.
            # Executa escolhas de ações, de avanço temporal e printa as ações executas.
            n = 0
            for item in (mainLista):
                if item == '\U0001F3C3 Sair do Jogo':
                    print(f'0 - {item}')
                else:
                    n += 1
                    print(f'{n} - {item}')           
            print('---')
            opcao = input('O que você gostaria de fazer agora? \U0001F4AC  ')
            
            if(opcao == '1'):
                if mainLista[0] == '\U0001F933 Ver Instagram':
                    print('Você viu o insta... \U0001F933')
                    relogio.avancaTempo(20)
                elif mainLista[0] == '\U0001F634 Descansar um pouco':
                    personagem.descansar = 1
                    relogio.avancaTempo(30)
                else:
                    personagem.descansar = 2
                    dia += 1
                    print(f'Você dormiu demais e perdeu a aula... \U0001F9A5')
                sleep(4)
            elif(opcao == '2'):
                if personagem.fome:
                    print('Você jantou... \U0001F60B')
                    personagem.fome = False
                    relogio.avancaTempo(15)
                else:
                    print('Você já está de barriguinha cheia. \U0001F922')
                    relogio.avancaTempo(5)
                sleep(4)
            elif(opcao == '3'):
                if relogio.horas < 7:
                    print('Aguarde Thiago liberar a sala. \U000023F3')
                    relogio.avancaTempo(10)
                elif 8 < relogio.horas < 11:
                    print('Você se atrasou para a aula \U0001F92C')
                    personagem.xp = 6
                    relogio.horas = 11
                    relogio.minutos = 0
                else:
                    if relogio.horas >= 11:
                        print('Oops!! Aula encerrada \U0001F4AA')
                    else:
                        personagem.xp = 10
                        print('Estudando')
                        while relogio.horas <= 11:
                            print(f'\U0001F557 São {relogio.horas} horas')
                            if relogio.horas == 9:
                                print('\U0001F46E Aqui é o tio Thiago passando pra avisar que você não vai ter recreio\n\n')
                                sleep(5)
                            msg = Msg()
                            print(msg)
                            sleep(4)
                            relogio.avancaTempo(60)
                            clear.clear()
                        print('Muito bem, você assistiu a aula \U0001F970')
                        personagem.descansar = 2
                        relogio.horas = 11
                        relogio.minutos = 0
                sleep(4)
            elif(opcao == '4'):
                personagem.xp = 5
                print('Muito bem!! Você estudou...\U0001F469')
                relogio.avancaTempo(30)
                sleep(4)
            elif(opcao == '0'):
                print('Até mais... \U0001F44B')
                sleep(4)
                break
            else:
                print('Opção inválida! \U0001F6A8')
                relogio.avancaTempo(5)
                sleep(4)
    if personagem.xp >= 20:
        print('Até mais... \U0001F44B')
        sleep(3)
        
                
            






