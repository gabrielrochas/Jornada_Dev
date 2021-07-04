from projetos.projeto_1_detetive import Detective

# from art import *
from time import sleep
import os


if __name__ == '__main__':
    # Start Detective Project
    startDective = Detective()
    startDective.colors()
    print(startDective.startGame())
    questions = startDective.questions()
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
    count = n = 0
    for q in questions:
        print(f'\nPergunta {n+1}')
        qs = input(f'{q}').strip().lower()[0]
        for i in '...': print(i, end= ' '), sleep(0.5)
        n += 1
        if qs == 's': 
            count += 1
        sleep(0.5)

    print(startDective.verdict(count))
    # End Detective Project