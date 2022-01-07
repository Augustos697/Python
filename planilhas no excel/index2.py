import openpyxl
#Carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')
#Selecionando uma Página
frutas_page = book['Frutas']
#Imrpimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2):
    for cell in rows: 
        print(cell.value ,end=" ")
        