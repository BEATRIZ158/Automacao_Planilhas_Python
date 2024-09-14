class Animal:
    def __init__(self, numero_brinco, peso, data_entrada, numero_piquete, preco_racao, preco_silo, racao, silo, nome_medicamento, valor_medicamento):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        self.numero_brinco = numero_brinco
        self.peso = peso
        self.data_entrada = data_entrada
        self.pesagens = [peso]
        self.datas = [data_entrada]  # Adiciona a data de entrada à lista de datas
        self.numero_piquete = numero_piquete
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
        return peso * 0.180

    @staticmethod
    def calcular_silo(peso):
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        return peso * 0.200

    @staticmethod
    def _validar_numero(numero):
        try:
            return int(numero)
        except ValueError:
            raise ValueError("O número do brinco deve ser um número inteiro")

    @staticmethod
    def _validar_peso(peso):
        try:
            peso_float = float(peso)
            if peso_float <= 0:
                raise ValueError("O peso deve ser maior que zero")
            return peso_float
        except ValueError:
            raise ValueError("O peso deve ser um valor numérico válido")

    @staticmethod
    def _validar_numero_piquete(numero_piquete):
        try:
            return int(numero_piquete)
        except ValueError:
            raise ValueError("O número do piquete deve ser um número inteiro")

    @staticmethod
    def _validar_preco_racao(preco_racao):
        try:
            preco = float(preco_racao)
            if preco <= 0:
                raise ValueError("O preço da ração deve ser maior que zero")
            return preco
        except ValueError:
            raise ValueError("O preço da ração deve ser numérico")

    @staticmethod
    def _validar_preco_silo(preco_silo):
        try:
            preco = float(preco_silo)
            if preco <= 0:
                raise ValueError("O preço do silo deve ser maior que zero")
            return preco
        except ValueError:
            raise ValueError("O preço do silo deve ser numérico")

    @staticmethod
    def _validar_nome_medicamento(nome_medicamento):
        if nome_medicamento:
            return str(nome_medicamento)
        else:
            return 'NENHUM'

    @staticmethod
    def _validar_valor_medicamento(valor_medicamento):
        if valor_medicamento:
            try:
                return float(valor_medicamento)
            except ValueError:
                raise ValueError("O valor do medicamento deve ser numérico")
        else:
            return 0.0

    @staticmethod
    def validar_numero(numero):
        return Animal._validar_numero(numero)

    @staticmethod
    def validar_peso(peso):
        return Animal._validar_peso(peso)

    @staticmethod
    def validar_numero_piquete(numero_piquete):
        return Animal._validar_numero_piquete(numero_piquete)

    @staticmethod
    def validar_preco_racao(preco_racao):
        return Animal._validar_preco_racao(preco_racao)

    @staticmethod
    def validar_preco_silo(preco_silo):
        return Animal._validar_preco_silo(preco_silo)

    @staticmethod
    def validar_nome_medicamento(nome_medicamento):
        return Animal._validar_nome_medicamento(nome_medicamento)

    @staticmethod
    def validar_valor_medicamento(valor_medicamento):
        return Animal._validar_valor_medicamento(valor_medicamento)
