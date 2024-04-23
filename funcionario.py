class Funcionario:
    def __init__(self, nome, idade, cargo, qtdHoras, valorHora):
        self.dados = {
            'nome': nome,
            'idade': idade,
            'cargo': cargo,
            'qtdHoras': qtdHoras,
            'valorHora': valorHora
        }

    def calcular_salario(self):
        qtdHoras = float(self.dados['qtdHoras'])
        valorHora = float(self.dados['valorHora'])
        salario_base = qtdHoras * valorHora
        bonus = salario_base * 0.05
        return salario_base + bonus

    def obter_dados(self):
        return self.dados

    def atualizar_dados(self, dados):
        self.dados.update(dados)
