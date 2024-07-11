class Trator:
    def __init__(self, numero, km, data_entrada, abastecimento):
        self.numero = numero
        self.kilometragens = [km]
        self.datas = [data_entrada]
        self.abastecimento = abastecimento
    
    def adionar_km(self, km):
        if km < 0:
            raise ValueError("O peso não pode ser negativo.")
        self.kilometragens.append(km)
