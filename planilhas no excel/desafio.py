import openpyxl

book = openpyxl.Workbook("")
book.create_sheet("Computadores")
Computadores_page = book["Computadores"]
Computadores_page.append(["Computador","Ram","Preço"])
Computadores_page.append(["Computador 1", "8Gb","R$2500"])
Computadores_page.append(["Computador 2", "8Gb","R$2500"])
Computadores_page.append(["Computador 3", "8Gb","R$2500"])

book.save("Computadores.xlsx")