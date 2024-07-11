from trator import Trator

class acervo:
    def __init__(self):
        self.tratores = {}
    
    def adicionar_trator(self, numero, km, data_entrada, abastecimento):
        if numero in self.tratores:
            raise ValueError("Trator com essa numeração já cadastrado!")
        novo_trator = Trator( numero, km, data_entrada, abastecimento)
        self.tratores[numero] = novo_trator
