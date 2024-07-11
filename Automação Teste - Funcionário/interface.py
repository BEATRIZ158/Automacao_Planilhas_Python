from tkinter import Tk, messagebox, Label, Frame, Entry, StringVar, Radiobutton, Button
from funcionario import Funcionario
from medico import Medico
from enfermeiro import Enfermeiro
from adicionar_dados import *
from openpyxl import load_workbook

class InterfaceAplicação(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Salário: Médico e Enfermeiro")
        self.criando_widgets()
        self.geometry("400x350")
        self.resizable(False, False)
        
    def criando_widgets(self):
        self.main_menu = Frame(self)
        self.main_menu.pack(padx=20, pady=20)
        
        Label(self.main_menu, text="Cálculo do Salário: Médico e Enfermeiro").grid(row=0, columnspan=4)
        Label(self.main_menu, text="Nome: ").grid(row=1, column=0, sticky="e")
        self.nome_entry = Entry(self.main_menu)
        self.nome_entry.grid(row=1, column=1, padx=5, pady=5)
        
        Label(self.main_menu, text="Idade: ").grid(row=2, column=0, sticky="e")
        self.idade_entry = Entry(self.main_menu)
        self.idade_entry.grid(row=2, column=1, padx=5, pady=5)
        
        Label(self.main_menu, text="Cargo: ").grid(row=3, column=0, sticky="e")
        self.cargo_var = StringVar()
        self.cargo_var.set("Médico") 
        
        self.medico_button = Radiobutton(self.main_menu, text="Médico", variable=self.cargo_var, value="Médico")
        self.medico_button.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        
        self.enfermeiro_button = Radiobutton(self.main_menu, text="Enfermeiro", variable=self.cargo_var, value="Enfermeiro")
        self.enfermeiro_button.grid(row=3, column=2, sticky="w", padx=5, pady=5)
        
        Label(self.main_menu, text="Horas trabalhadas: ").grid(row=4, column=0, sticky="e")
        self.qtdHoras_entry = Entry(self.main_menu)
        self.qtdHoras_entry.grid(row=4, column=1, padx=5, pady=5)
        
        Label(self.main_menu, text="Valor da hora: ").grid(row=5, column=0, sticky="e")
        self.valorHora_entry = Entry(self.main_menu)
        self.valorHora_entry.grid(row=5, column=1, padx=5, pady=5)
        
        Button(self.main_menu, text="Calcular Salário", command=self.calcular_salario).grid(row=6, columnspan=4, pady=10)
        
        self.salario_label = Label(self.main_menu, text="Salário calculado: ")
        self.salario_label.grid(row=7, column=0, pady=5, padx=5)
        
        Button(self.main_menu, text="Salvar dados!", command=self.salvar_dados).grid(row=8, columnspan=4, pady=10)
        
    def salvar_dados(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        cargo = self.cargo_var.get()
        qtdHoras = self.qtdHoras_entry.get()
        valorHora = self.valorHora_entry.get()
        
        adicionar_dados(nome, idade, cargo, qtdHoras, valorHora)
        messagebox.showinfo("Salvo com sucesso!","Dados salvos com sucesso")
        self.limpar_campos()
        
    def limpar_campos(self):
        self.nome_entry.delete(0, 'end')
        self.idade_entry.delete(0, 'end')
        self.qtdHoras_entry.delete(0, 'end')
        self.valorHora_entry.delete(0, 'end')
        self.salario_label.config(text="Salário calculado: ")
    
    def calcular_salario(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        cargo = self.cargo_var.get()
        qtdHoras = self.qtdHoras_entry.get()
        valorHora = self.valorHora_entry.get()
        
        if cargo == "Médico":
            funcionario = Medico(nome, idade, cargo, qtdHoras, valorHora)
        elif cargo == "Enfermeiro":
            funcionario = Enfermeiro(nome, idade, cargo, qtdHoras, valorHora)
        else:
            funcionario = None
        
        if funcionario:
            salario = funcionario.calcular_salario()
            self.salario_label.config(text="Salário calculado: " + str(salario))
        else:
            self.salario_label.config(text="Cargo inválido!")

app = InterfaceAplicação()
app.mainloop()
