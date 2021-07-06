class Escolha:
    def __init__(self, opcao):
        self.__opcao = opcao

    def __str__(self):
        return f"{self.__opcao}"

    @property
    def opcao(self):
        return self.__opcao

    @opcao.setter   
    def opcao(self, opcao):
        if(opcao =="1"):
            aluno.sujo = False
            tempo.avanca(30)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe = True
            else:
                print("Não há comida em casa.")
            tempo.avanca(10)
        elif(opcao == "3"):
            if(aluno)
            
                
        self.__opcao = opcao
        return self.__opcao




        