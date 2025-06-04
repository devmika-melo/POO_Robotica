class Robo:
    def __init__(self, nome):
        self.nome = nome
        self.__bateria = 100
        self.__velocidade = 50
    
    def mover(self):
        if self.__bateria >= 10:
            self.__bateria -= 10

            if self.__velocidade == 0:
                self.__velocidade = 10
                print(f"{self.nome} começou a se mover a {self.__velocidade} km/h. Bateria agora em {self.__bateria}%")
            elif self.__velocidade < 100:
                self.__velocidade += 10
                if self.__velocidade > 100:
                    self.__velocidade = 100
                print(f"{self.nome} acelerou, continua se movendo")
            else:
               print(f"{self.nome} mantém a velocidade, continua se movendo")
        else:
            print(f"{self.nome} está sem bateria!! Por favor, recarregar")
    
    def parar(self):
        self.__velocidade = 0
        print(f"{self.nome} parou completamente!")
        
    def recarregar(self):
        print(f"Recarregando {self.nome}...")
        self.__bateria = 100
        print(f"{self.nome} está totalmente carregado")

    def exibir_status(self):
        return f"Nome: {self.nome}, Bateria: {self.__bateria}%, Velocidade: {self.__velocidade} km/h"


    def verificar_velocidade(self, limite):
        if self.__velocidade >= limite:
            self.__velocidade = limite
            print(f"{self.nome} atingiu o limite de velocidade de {limite} e foi limitado.")
        else:
            print(f"{self.nome} está se movendo a {self.__velocidade} km/h. Bateria agora em {self.__bateria}%")


robo1 = Robo("IngridBot")

print(robo1.exibir_status())

while robo1._Robo__bateria > 0:
    robo1.mover()
    print(robo1.exibir_status())
robo1.parar()


robo1.mover()
robo1.recarregar()
print(robo1.exibir_status())

robo1.verificar_velocidade(limite=100)