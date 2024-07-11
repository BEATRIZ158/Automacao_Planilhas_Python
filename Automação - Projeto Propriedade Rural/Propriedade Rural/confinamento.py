from animal import Animal
from tkinter import messagebox

class Confinamento_animais:
    def __init__(self):
        self.animais = {}

    def adicionar_animal(self, brinco, peso_entrada, data_entrada, silo, preço_silo, piquet):
        if brinco in self.animais:
            raise ValueError("Animal com esse brinco já cadastrado!")
        novo_animal = Animal(brinco, peso_entrada, data_entrada, silo, preço_silo, piquet)
        self.animais[brinco] = novo_animal

    def procurar_animal(self, brinco):
        return self.animais.get(brinco)
    
    def remover_animal(self, brinco):
        if brinco in self.animais:
            del self.animais[brinco]
        else:
            raise KeyError("Animal não encontrado!")
        
    #Função para adicionar novas pesagens que deve ser chamada após procurar animal
    def lançar_pesagem(self, animal, peso, data, silo, preço_silo):
        if animal:
            try:
                animal.adicionar_pesagem(peso, data)
                animal.adicionar_silo(silo)
                messagebox.showinfo("Sucesso", "Pesagem adicionada com sucesso!")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Animal não encontrado!")
