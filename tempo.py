class Tempo:
    def __init__(self):
        self.horas = 7
        self.minutos = 0
    
    def avanca(self, minutos):
        self.minutos += minutos
        while(self.minutos <= 60):
            self.minutos -= 60
            self.horas += 1

