class Aluno:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.lanche = True
        self.aula = False
        self.xp = 0
        self.conhecimento = 100
        self.estudo
    
    def __str__(self):  
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.aula else "não ")+"assistiu a aula. Você adquiriu "+str(self.conhecimento)+" em sua vida de DEV."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.aula = False
        