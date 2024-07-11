from funcionario import Funcionario

class Enfermeiro(Funcionario):
    def calcular_salario(self):
        dados = self.obter_dados()
        
        qtdHoras = float(dados['qtdHoras'])
        valorHora = float(dados['valorHora'])
        
        salario_base = qtdHoras * valorHora
        bonus = salario_base * 0.05
        return salario_base + bonus
