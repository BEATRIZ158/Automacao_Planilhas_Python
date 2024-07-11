import openpyxl

def salvar_em_excel(animal):
    try:
        wb = openpyxl.load_workbook('dados_animais.xlsx')
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Número do Brinco", "Peso", "Data de Entrada", "Número do Piquet", "Preço Ração (Kg)", "Preço Silo (Kg)" "Ração", "Silo"])
    else:
        ws = wb.active
    
    ws.append([animal.numero_brinco, animal.peso, animal.data_entrada, animal.numero_piquet, animal.preco_racao, animal.preco_silo, animal.racao, animal.silo])
    wb.save('dados_animais.xlsx')
