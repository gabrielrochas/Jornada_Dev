from projetos.projeto_1_detetive import Detective
from projetos.projeto_2_jokenpo import Jokenpo
from utilities.utilities import Utilities
from time import sleep


if __name__ == '__main__':
    clear = Utilities()
    # Start Detective Project
    startDective = Detective()
    startDective.colors()
    print(startDective.startGame())
    questions = startDective.questions()
    clear.clearTerminal()
    count = c = 0
    for q in questions:
        print(f'\n{c+1}ª Pergunta')
        qs = input(f'{q}').strip().lower()[0]
        for p in '...': print(p, end= ' '), sleep(0.5)
        c += 1
        if qs == 's': 
            count += 1
        sleep(0.5)

    print(startDective.verdict(count))
    # End Detective Project

    # Start Jokenpo
    jokenpoGame = Jokenpo()
    jokenpoGame.welcome()
    for p in '...': print(p, end=' '), sleep(0.6)
    print()
    clear.clearTerminal()
    name = jokenpoGame.userName()
    jokenpoGame.start(name)
    sleep(2)
    # End Jokenpo