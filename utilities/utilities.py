import os

class Utilities():
    def __init__(self):
        pass

    def clearTerminal(self):
        return os.system('cls' if os.name == 'nt' else 'clear')