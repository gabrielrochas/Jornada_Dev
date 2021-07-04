from art import *
from time import sleep
import colorama
import os

class Detective:
    
    def __init__(self, answer = 0):
        self.__answer = answer

    def colors(self):
        colorama.init()

        self.__blue = '\033[94m' # Print in BLUE color
        self.__cyan = '\033[96m' # Print in CYAN color
        self.__green = '\033[92m' # Print in GREEN color
        self.__yellow = '\033[93m' # Print YELLOW color
        self.__red = '\033[91m' # Print in RED color
        self.__beginBold = '\u001b[1m' # Start BOLD
        self.__endBold = '\u001b[0m' # End BOLD
        self.__resetColor = '\033[39m' # Reset to default color
        self.__underline = '\u0332' # underline

        self.__draw = '#'


    def startGame(self):
        tprint('DETETIVE', font='small') # ASCII print art
        sleep(2)
        detective = self.__underline.join('Sherlock Holmes') # You can change the name of the detective
        return f'{self.__blue}{self.__draw * 65}\nOlá, eu sou o detetive {detective}.\nVou fazer cinco perguntas e quero respostas simples: {self.__beginBold}SIM ou NÃO{self.__endBold}{self.__blue}.\nVamos começar!\n{self.__draw * 65}{self.__resetColor}'


    def questions(self):
        sleep(3)
        question = [
        'Você telefonou para a vítima? SIM ou NÃO: ',
        'Você esteve no local do crime? SIM ou NÃO: ',
        'Você mora perto da vítima?: SIM ou NÃO: ',
        'Você devia para a vítima?: SIM ou NÃO: ',
        'Você já trabalhou com a vítima?: SIM ou NÃO: ']

        return question

    def verdict(self, count):
        print('\nEstamos processando as suas respostas...\n')
        sleep(3)
        self.__count = count

        if self.__count > 0 and self.__count <= 2:
            ver = f'{self.__cyan}{self.__draw * 65}\n\nVocê é considerado como {self.__beginBold}SUSPEITO{self.__endBold}{self.__cyan} do crime\n\n{self.__draw * 65}'
        elif self.__count > 2 and self.__count <= 4:
            ver = f'{self.__yellow}{self.__draw * 65}\n\nVocê é considerado como {self.__beginBold}CÚMPLICE{self.__endBold}{self.__yellow} do crime\n\n{self.__draw * 65}'
        elif self.__count == 5:
            ver = f'{self.__red}{self.__draw * 65}\n\nVocê é considerado como {self.__beginBold}CULPADO{self.__endBold}{self.__red} do crime\n\n{self.__draw * 65}'
        else:
            ver = f'{self.__green}{self.__draw * 65}\n\nVocê é {self.__beginBold}INOCENTE{self.__endBold}{self.__green} do crime!\n\n{self.__draw * 65}'

        return ver
    
