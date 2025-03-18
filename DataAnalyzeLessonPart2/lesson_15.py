# 17.03.2025

import openpyxl

wb = openpyxl.Workbook()

sh = wb.active
sh.title ='student_Info'
sh.append(['Name','telefon','city'])

sh.append(['Dennis','1052002','Enger'])
sh.append(['Feuerwehr','112','Enger'])
sh.append(['Laura','105255521','Enger'])

wb.save('1.xlsx')