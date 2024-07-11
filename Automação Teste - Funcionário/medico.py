from funcionario import Funcionario

class Medico(Funcionario):
    def calcular_salario(self):
        dados = self.obter_dados()
        qtdHoras = float(dados['qtdHoras'])
        valorHora = float(dados['valorHora'])
        
        salario_base = qtdHoras * valorHora
        bonus = salario_base * 0.25
        return salario_base + bonus
