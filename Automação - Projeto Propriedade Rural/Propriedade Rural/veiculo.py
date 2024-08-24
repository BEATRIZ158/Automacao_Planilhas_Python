class Veiculo:
    def __init__(self, numero, km, data_entrada, nome_combustivel, valor_litro, litros):
        self.numero = numero # Recebe o número do veículo
        self.km = km # Salva o Km do momento
        self.data_entrada = data_entrada # Salva a data de abastecimento
        self.nome_combustivel = nome_combustivel
        self.valor_litro = valor_litro
        self.litros = litros
        
    def _validar_numero(self, numero):
        try:
            return int(numero)
        except ValueError:
            raise ValueError("O número do brinco deve ser um número inteiro")
    
    def _validar_km(self, km):
        try:
            return float(km)
        except ValueError:
            raise ValueError("O km deve ser um valor númerico")
    
    def _validar_nome_combustivel(self, nome_combustivel):
        try:
            return str(nome_combustivel)
        except ValueError:
            raise ValueError("O nome do combustível não pode ser um número")
    
    def _validar_valor_litro(self, valor_litro):
        try:
            return float(valor_litro)
        except ValueError:
            raise ValueError("A quantidade de litros deve ser numérica")
    
    def _validar_litros(self, litros):
        try:
            self.litros = float(litros)
        except ValueError:
            raise ValueError("A litragem precisa ser um número")
    
    # Métodos públicos de validação
    def validar_numero(self, numero):
        return self._validar_numero(numero)
    
    def validar_km(self, km):
        return self._validar_km(km)
   
    def validar_nome_combustivel(self, nome_combustivel):
        return self._validar_nome_combustivel(nome_combustivel)

    def validar_valor_litro(self, valor_litro):
        return self._validar_valor_litro(valor_litro)
    
    def validar_litros(self, litros):
        return self._validar_litros(litros)
