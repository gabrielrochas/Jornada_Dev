from random import randint # Randint para self.__listaMsg do professor.
class Msg():
    def __init__(self): # Método construtor da Class Msg.       
        self.__listaMsg = ['Vai dar bom \U0001F605', 'Tudo bem até aí, galera? \U0001F60E', 'Blá blá blá \U0001F61D', 'Uérever \U0001F92A'] # Lista de Mensagens.
        i = (len(self.__listaMsg) - 1) # Organiza a lista de mensagens de acordo com o tamanho da string.
        self.__msg = randint(0, i) # Escolhe a mensagem aleatoriamente dentro da lista.
    
    def __str__(self): # Método para retornar a mensagem escolhida da lista.
        return self.__listaMsg[self.__msg]