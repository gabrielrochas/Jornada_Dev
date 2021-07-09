class ListaOpcoes: # criação da class ListaOpcoes
    def __init__(self, horas, minutos, descanso): # Método construtor da Class ListaOpcoes
        self.__horas = horas
        self.__minutos = minutos
        self.__descanso = descanso

        # lista incial de opções de ações.
        self.__lista = ['\U0001F372 Vai jantar', '\U0001F4BB Assistir aula', '\U0001F4DA Estudar', '\U0001F3C3 Sair do Jogo']

        # Verifica o nível de cansaço do personagem e altera a lista de acordo com o cansaço
        if self.__descanso == 0:
            self.__lista.insert(0, '\U0001F933 Ver Instagram')
        elif self.__descanso == 1:
            self.__lista.insert(0, '\U0001F634 Descansar um pouco')
        elif self.__horas >= 11 and self.__minutos >= 10:
            self.__lista.insert(0, '\U0001F4A4 Dormir')
        else:
            self.__lista.insert(0, '\U0001F4A4 Dormir')

    # Utilização do Getter e Setter para acessar variaveis protegidas.
    @property
    def descanso(self):
        return self.__descanso

    @descanso.setter
    def descanso(self, valor):
        self.__descanso = valor

    # Retorna  valores da lista
    @property
    def lista(self):
        return self.__lista
    




        