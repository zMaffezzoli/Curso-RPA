from openpyxl import Workbook, load_workbook

# Openpyxl MANTÈM gráficos e fórmulas em células

tabela = load_workbook('Produtos.xlsx')

aba_ativa = tabela.active

for celula in aba_ativa["C"]:
    if celula.value == 'Serviço':
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

tabela.save('Produtos_openpyxl.xlsx')