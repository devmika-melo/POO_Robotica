class Robo:
    def __init__(self, nome):
        self.nome = nome
        self.bateria = 100
    
    def exibir_status(self):
        print(f"Nome do Robô: {self.nome}")
        print(f"Bateria Atual: {self.bateria}")
    
    def diminuir_bateria(self, valor):
        if self.bateria - valor >= 0:
            self.bateria -= valor
            print(f"Bateria reduzida em: {valor}")
        
        else:
            self.bateria = 0
            print(f"Descarregado (0%).")


robo1 = Robo("BotMika")
robo1.exibir_status()

robo1.diminuir_bateria(30)

robo1.exibir_status()
