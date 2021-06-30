from openpyxl import Workbook
wb = Workbook()
ws = wb.active


f = open('test8 2001-3001.txt', 'r+', encoding='utf-8')

data = f.readlines()
spaces = ""
for i in range(len(data)):
    row = data[i].split(" ")  
    ws.append(row)
wb.save("testval2000-3000.xlsx") 