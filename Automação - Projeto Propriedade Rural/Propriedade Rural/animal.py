class Animal:
    def __init__(self, numero_brinco, peso, data_entrada, numero_piquet, preco_racao, preco_silo, racao, silo, nome_medicamento, valor_medicamento):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        self.numero_brinco = numero_brinco
        self.peso = peso
        self.data_entrada = data_entrada
        self.pesagens = [peso]
        self.datas = [data_entrada]  # Adiciona a data de entrada à lista de datas
        self.numero_piquet = numero_piquet
        self.preco_racao = preco_racao
        self.preco_silo = preco_silo
        self.racao = racao
        self.silo = silo
        self.piquet = [numero_brinco]  # Inicializa a lista de piquet com o número do brinco do animal
        self.nome_medicamento = nome_medicamento # Pega o nome do medicamento
        self.valor_medicamento = valor_medicamento # Pega o valor do medicamento

    @staticmethod
    def calcular_racao(peso):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        return peso * 0.018

    @staticmethod
    def calcular_preco_racao(valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor

    def adicionar_pesagem(self, peso, data):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        self.pesagens.append(peso)
        self.datas.append(data)
        self.racao = self.calcular_racao(peso)
      
    @staticmethod
    def calcular_silo(peso):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        return peso * 0.020
   
    @staticmethod
    def calcular_preco_silo(valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor      
    
    def ultima_pesagem(self):
        return self.pesagens[-1] if self.pesagens else None

    def ultima_racao(self):
        return self.racao

    def ultima_data(self):
        return self.datas[-1] if self.datas else None

    def adicionar_animal_piquet(self, brinco):
        self.piquet.append(brinco)

    def remover_animal_piquet(self, brinco):
        if brinco in self.piquet:
            self.piquet.remove(brinco)
            return "Animal retirado do piquet!"
        return "Animal não encontrado no piquet."
