from random import randint # Rantint para escolher as 3 opções de self.__cansado.

class Personagem:
    def __init__(self): # Método construtor da Class Personagem.
        self.__fome = True
        self.__cansado = ' ' 
        self.__descansar = randint(0,2) # 0 não cansado, 1 pouco cansado, 2 muito cansado
        self.__experiencia = ' '
        self.__xp = 0

# Utilização do Getter e Setter para acessar variaveis protegidas.
    @property
    def descansar(self):
        return self.__descansar    
    @descansar.setter
    def descansar(self, valor):
        self.__descansar -= valor
    
    @property
    def xp(self):
        return self.__xp
    @xp.setter
    def xp(self, xp):
        self.__xp += xp
    
    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self, valor):
        self.__fome = valor

# Retorna randint de self.__cansado e contabiliza XP em programação do personagem.
    def __str__(self):
        if self.__descansar == 0:
            self.__cansado = 'não está cansado'
        elif self.__descansar == 1:
            self.__cansado = 'está pouco cansado'
        else:
            self.__cansado = 'está muito cansado'

        if self.__xp == 0:
            self.__experiencia = 'não tem experiência em programação'
        else:
            self.__experiencia = 'você tem ' + str(self.__xp) + '% de experiência em programação '          
# Mensagem incial do programa.
        return 'Você acabou de chegar do trabalho, ' + str(self.__cansado) + ', está'+(' com fome' if self.__fome else ' sem fome') + ' e ' + str(self.__experiencia)

