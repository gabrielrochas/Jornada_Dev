class Relogio: # criação da class relogio.
    def __init__(self): # Método construtor da Class Relogio.
        self.__horas = 6
        self.__minutos = 0
    
    def __str__(self): # Método para contabilizar as horas e os minutos da jornada.
        return f"{self.__horas:02d}:{self.__minutos:02d}"

# Utilização do Getter e Setter para acessar variaveis protegidas.    
    @property
    def horas(self):
        return self.__horas
    
    @horas.setter
    def horas(self, horas):
        self.__horas = horas
    
    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, minutos):
        self.__minutos = minutos
    
    def avancaTempo(self, minutos): # Método para transformação de 60 minutos em 1 hora.
        self.__minutos += minutos
        while(self.__minutos >= 60):
            self.__minutos -= 60
            self.__horas += 1