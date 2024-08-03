import tkinter as tk
from tkinter import Frame, Label, Button, PhotoImage, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from animal import Animal  # Importando a classe Animal
from dados_excel import salvar_em_excel

class MainApplication(tk.Tk):
    
    # Variáveis Globais
    global fonte_grande
    fonte_grande = ("Arial", 12)
    global cor_verde
    cor_verde = 'LightGreen'
    global cor_preta
    cor_preta = 'Black'
    global cor_branca
    cor_branca = 'White'
    global cor_vermelha
    cor_vermelha = 'Red'
    global tamanho_padrao
    tamanho_padrao = "950x700"
    
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Propriedade Rural")
        self.create_widgets()
    
    def create_widgets(self):
        self.main_menu = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        self.main_menu.pack(fill="both", expand=True)
        
        # Caminho para a pasta de imagens
        global caminho_imagens
        caminho_imagens = "Automação - Projeto Propriedade Rural/Propriedade Rural/imagens/"
        
        # Carregar imagens
        self.img_semi_confinamento = ImageTk.PhotoImage(Image.open(caminho_imagens + "confinamento.png"))
        self.img_despesas_gerais = ImageTk.PhotoImage(Image.open(caminho_imagens + "despesas.png"))
        self.img_controle_frota = ImageTk.PhotoImage(Image.open(caminho_imagens + "frota.png"))
        self.img_compra_venda = ImageTk.PhotoImage(Image.open(caminho_imagens + "compra.png"))
 
        tk.Label(self.main_menu, text="AGRO-TECH", anchor="center" ,height=3, width=80, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        tk.Button(self.main_menu, text="SEMI-\nCONFINAMENTO", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 14, "bold"), relief="raised", command=lambda: self.acessar_tela(self.tela_semi_confinamento, self.main_menu), image=self.img_semi_confinamento, compound='top').place(x=90, y=180)
        tk.Button(self.main_menu, text="DESPESAS \nGERAIS", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 14, "bold"), relief="raised",  command=lambda: self.acessar_tela(self.tela_despesas_gerais, self.main_menu), image=self.img_despesas_gerais, compound='top').place(x=290, y=180)
        tk.Button(self.main_menu, text="CONTROLE \nDE FROTA", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 14, "bold"), relief="raised", command=lambda: self.acessar_tela(self.tela_controle_frota, self.main_menu), image=self.img_controle_frota, compound='top').place(x=490, y=180)
        tk.Button(self.main_menu, text="COMPRA \nE VENDA", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 14, "bold"), relief="raised", command=lambda: self.acessar_tela(self.tela_compra_venda, self.main_menu), image=self.img_compra_venda, compound='top').place(x=690, y=180)
        tk.Button(self.main_menu, text="SAIR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=self.fechar_sistema).place(x=415, y=480)
        tk.Label(self.main_menu, text="© Beatriz, Paranapuã 2024", anchor="center", bg=cor_branca, font=("Arial", 11, "bold")).place(x=380,y=650)
        
        self.configure_semi_confinamento()
        self.configure_despesas_gerais()
        self.configure_controle_frota()
        self.configure_compra_venda()
        
        self.geometry(tamanho_padrao)
        self.resizable(False, False)
        
    def fechar_sistema(self):
        tk.messagebox.showinfo("Saindo do Sistema", "Saindo do Sistema\nAté logo!")
        self.destroy()
    
    def acessar_tela(self, frame_para_mostrar, frame_para_esconder):
        frame_para_mostrar.pack(fill="both", expand=True)
        frame_para_esconder.pack_forget()
        
    def retornar_ao_menu(self, frame_atual):
        frame_atual.pack_forget()
        self.main_menu.pack(fill="both", expand=True)
    
    #================================================================================================================================================================
    # Configurando a tela de semi-confinamento
    def configure_semi_confinamento(self):
        self.tela_semi_confinamento = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        
        self.img_lancar_animal = ImageTk.PhotoImage(Image.open(caminho_imagens + "animais.png"))
        self.img_procurar_animal = ImageTk.PhotoImage(Image.open(caminho_imagens + "pesquisar.png"))
        
        tk.Label(self.tela_semi_confinamento, text="SEMI-CONFINAMENTO", anchor="center" ,height=3, width=80, bd=5, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        tk.Button(self.tela_semi_confinamento, text="ADICIONAR ANIMAL", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 13, "bold"), relief="raised", command=lambda: self.acessar_tela(self.tela_adicionar_animal, self.tela_semi_confinamento), image=self.img_lancar_animal, compound='top').place(x=290, y=180)
        tk.Button(self.tela_semi_confinamento, text="RETIRAR ANIMAL", height=120, width=150, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 13, "bold"), relief="raised", image=self.img_procurar_animal, compound='top').place(x=490, y=180)
        tk.Button(self.tela_semi_confinamento, text="VOLTAR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=lambda: self.retornar_ao_menu(self.tela_semi_confinamento)).place(x=415, y=480)
        tk.Label(self.tela_semi_confinamento, text="© Beatriz, Paranapuã 2024", anchor="center", bg=cor_branca, font=("Arial", 11, "bold")).place(x=380,y=650)
        
        self.configure_adicionar_animal()
        
        self.geometry(tamanho_padrao)
        self.resizable(False, False)
    
    #================================================================================================================================================================
    # Configurando a tela de adicionar animal
    def configure_adicionar_animal(self):
        self.tela_adicionar_animal = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        
        fonte_grande = ("Arial", 13)
        
        tk.Label(self.tela_adicionar_animal, text="ADICIONAR ANIMAL", anchor="center", height=3, width=80, bd=5, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        
        # Rótulos e caixas de entrada para número do brinco
        tk.Label(self.tela_adicionar_animal, text="N.º BRINCO:", font=fonte_grande, bg=cor_branca).place(x=10, y=130)
        self.entry_brinco = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_brinco.place(x=110, y=130)

        # Rótulos e caixas de número do piquete
        tk.Label(self.tela_adicionar_animal, text="N.º PIQUETE:", font=fonte_grande, bg=cor_branca).place(x=310, y=130)
        self.entry_numero_piquet = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_numero_piquet.place(x=420, y=130)

        # Rótulos e caixas de entrada para o peso do animal
        tk.Label(self.tela_adicionar_animal, text="PESO (Kg):", font=fonte_grande, bg=cor_branca).place(x=630, y=130)
        self.entry_peso_animal = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_peso_animal.place(x=730, y=130)
        
        #Rótulos e caixa de preço da ração por Kg
        tk.Label(self.tela_adicionar_animal, text="KG RAÇÃO(R$):", font=fonte_grande, bg=cor_branca).place(x=10, y=230)
        self.entry_preco_racao = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_preco_racao.place(x=140,y=230)
        
        #Rótulos e caixa de preço do silo por Kg
        tk.Label(self.tela_adicionar_animal, text="KG SILO(R$):", font=fonte_grande, bg=cor_branca).place(x=340, y=230)
        self.entry_preco_silo = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_preco_silo.place(x=450,y=230)
        
        # Botão para abrir o calendário
        self.btn_abrir_calendario = tk.Button(self.tela_adicionar_animal, text="Selecionar Data", command=self.abrir_calendario, font=fonte_grande)
        self.btn_abrir_calendario.place(x=650, y=230)

        # Label para mostrar a data selecionada
        self.data_selecionada_label = tk.Label(self.tela_adicionar_animal, text="", bg=cor_branca, font=fonte_grande)
        self.data_selecionada_label.place(x=800, y=235)
        
        # Rótulos e caixa de nome do medicamento
        tk.Label(self.tela_adicionar_animal, text="MEDICAMENTO:", font=fonte_grande, bg=cor_branca).place(x=10, y=330)
        self.entry_nome_medicamento = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_nome_medicamento.place(x=140,y=330)
        
        # Rótulos e caixa de valor do medicamento
        tk.Label(self.tela_adicionar_animal, text="R$ MEDICAMENTO:", font=fonte_grande, bg=cor_branca).place(x=340, y=330)
        self.entry_valor_medicamento = tk.Entry(self.tela_adicionar_animal, font=fonte_grande)
        self.entry_valor_medicamento.place(x=500,y=330)
        
        # Botão para abrir o calendário
        self.btn_salvar_animal = tk.Button(self.tela_adicionar_animal, text="SALVAR", height=2, width=10, bd=5, bg=cor_verde, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=self.salvar_animal)
        self.btn_salvar_animal.place(x=340, y=480)
        
        # Botão para voltar
        self.btn_voltar_tela_semi_confinamento = tk.Button(self.tela_adicionar_animal, text="VOLTAR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=lambda: self.acessar_tela(self.tela_semi_confinamento, self.tela_adicionar_animal))
        self.btn_voltar_tela_semi_confinamento.place(x=480, y=480)
        
        tk.Label(self.tela_adicionar_animal, text="© Beatriz, Paranapuã 2024", anchor="center", bg=cor_branca, font=("Arial", 11, "bold")).place(x=380,y=650)

    
        self.geometry(tamanho_padrao)
        self.resizable(False, False)
        
    def salvar_animal(self):    
        # Obter valores dos campos de entrada
        numero_brinco = self.entry_brinco.get().strip()
        peso_str = self.entry_peso_animal.get().strip()
        data_entrada = self.data_selecionada_label.cget("text").strip()
        numero_piquet = self.entry_numero_piquet.get().strip()
        preco_racao_str = self.entry_preco_racao.get().strip()
        preco_silo_str = self.entry_preco_silo.get().strip()
        nome_medicamento = self.entry_nome_medicamento.get().strip()
        valor_medicamento = self.entry_valor_medicamento.get().strip()
        
        try:
            numero_brinco = int(numero_brinco)
        except ValueError:
            tk.messagebox.showerror("Erro", "O número do brinco deve ser um número inteiro")
            return

        try:
            peso = float(peso_str)
        except ValueError:
            tk.messagebox.showerror("Erro", "O peso deve ser um número válido")
            return

        try:
            numero_piquet = int(numero_piquet)
        except ValueError:
            tk.messagebox.showerror("Erro", "O N.º do piquete deve ser um número válido")
            return

        try:
            preco_racao = float(preco_racao_str)
        except ValueError:
            tk.messagebox.showerror("Erro", "O preço da ração deve ser um número válido")
            return

        try:
            preco_silo = float(preco_silo_str)
        except ValueError:
            tk.messagebox.showerror("Erro", "O preço do silo deve ser um número válido")
            return
        
        racao = float(Animal.calcular_racao(peso))
        silo = float(Animal.calcular_silo(peso))
   
        # Validação dos campos opcionais
        if nome_medicamento:
            try:
                nome_medicamento = str(nome_medicamento)
            except TypeError:
                tk.messagebox.showerror("Erro", "O nome do medicamento não pode ser um número.")
                return
        else:
            nome_medicamento = 'NENHUM MEDICAMENTO'

        if valor_medicamento:
            try:
                valor_medicamento = float(valor_medicamento)
            except ValueError:
                tk.messagebox.showerror("Erro", "O valor do medicamento deve ser numérico.")
                return
        
        # Validar os dados, se os campos estão preenchidos
        if not numero_brinco or peso <= 0 or not data_entrada or not numero_piquet or preco_racao <= 0 or preco_silo <= 0 or racao <= 0 or silo <= 0:
            tk.messagebox.showerror("Erro", "Todos os campos obrigatórios devem ser prenchidos (Exceto medicamento)!")
            return
        
        # Criar uma instância de Animal
        animal = Animal(numero_brinco, peso, data_entrada, numero_piquet, preco_racao, preco_silo, racao, silo, nome_medicamento, valor_medicamento)
        
        # Salvar a instância no Excel
        salvar_em_excel(animal)
        
        # Limpar os campos de entrada
        self.entry_brinco.delete(0, tk.END)
        self.entry_peso_animal.delete(0, tk.END)
        self.data_selecionada_label.config(text="")
        self.entry_numero_piquet.delete(0, tk.END)
        self.entry_preco_racao.delete(0, tk.END)
        self.entry_preco_silo.delete(0, tk.END)
        self.entry_nome_medicamento.delete(0, tk.END)
        self.entry_valor_medicamento.delete(0, tk.END)
        
        tk.messagebox.showinfo("Sucesso", "Animal adicionado com sucesso!")    
    def abrir_calendario(self):
        # Cria uma nova janela
        self.calendario_toplevel = tk.Toplevel(self)
        self.calendario_toplevel.title("Selecionar Data")
        self.calendario_toplevel.grab_set()  # Torna esta janela modal

        # Adiciona o calendário nesta janela
        self.calendario = Calendar(self.calendario_toplevel, selectmode='day', date_pattern='dd/mm/yyyy', font=("Arial", 10), width=12, height=8)
        self.calendario.pack(padx=10, pady=10)

        # Botão para confirmar a seleção da data
        tk.Button(self.calendario_toplevel, text="Confirmar", command=self.confirmar_data).pack(pady=5)

    def confirmar_data(self):
        # Obtém a data selecionada e atualiza o label
        data_selecionada = self.calendario.get_date()
        self.data_selecionada_label.config(text=data_selecionada)
        self.calendario_toplevel.destroy()
    #================================================================================================================================================================
    # Configurando a tela de despesas gerais
    def configure_despesas_gerais(self):
        self.tela_despesas_gerais = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        
        tk.Label(self.tela_despesas_gerais, text="DESPESAS GERAIS", anchor="center", height=3, width=80, bd=5, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        tk.Button(self.tela_despesas_gerais, text="VOLTAR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=lambda: self.retornar_ao_menu(self.tela_despesas_gerais)).place(x=415, y=480)
        tk.Label(self.tela_despesas_gerais, text="© Beatriz, Paranapuã 2024", anchor="center", font=("Arial", 11, "bold")).place(x=380,y=650)

        self.geometry(tamanho_padrao)
        self.resizable(False, False)
    #================================================================================================================================================================
    # Configurando a tela de controle_frota
    def configure_controle_frota(self):
        self.tela_controle_frota = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        
        tk.Label(self.tela_controle_frota, text="CONTROLE DE FROTA", anchor="center", height=3, width=80, bd=5, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        tk.Button(self.tela_controle_frota, text="VOLTAR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=lambda: self.retornar_ao_menu(self.tela_controle_frota)).place(x=415, y=480)
        tk.Label(self.tela_controle_frota, text="© Beatriz, Paranapuã 2024", anchor="center", font=("Arial", 11, "bold")).place(x=380,y=650)

        self.geometry(tamanho_padrao)
        self.resizable(False, False)
    #================================================================================================================================================================
    # Configurando a tela de Compra_venda
    def configure_compra_venda(self):
        self.tela_compra_venda = Frame(self, bg=cor_branca, relief="solid", bd=4, highlightbackground=cor_verde)
        tk.Label(self.tela_compra_venda, text="COMPRA E VENDA", anchor="center", height=3, width=80, bd=5, background=cor_verde, fg=cor_branca, font=("Arial", 15, "bold"), relief="raised").place(x=0, y=0)
        tk.Button(self.tela_compra_venda, text="VOLTAR", height=2, width=10, bd=5, bg=cor_vermelha, fg=cor_preta, font=("Arial", 12, "bold"), relief="raised", command=lambda: self.retornar_ao_menu(self.tela_compra_venda)).place(x=415, y=480)
        tk.Label(self.tela_compra_venda, text="© Beatriz, Paranapuã 2024", anchor="center", font=("Arial", 11, "bold")).place(x=380,y=650)

        self.geometry(tamanho_padrao)
        self.resizable(False, False)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
