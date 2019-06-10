#! python3
# UpdateProduce.py - Corrects costs in produce sales spreadsheet.

import xlrd

wb = xlrd.open_workbook('updatedProduceSales.xlsx')
sheet = wb.sheet_by_name('Population by Census Tract')

PRICE_UPDATES = {'Garlic' : 3.07,
                 'Celery': 1.19,
                 'Lemon' : 1.27}

row = sheet.max_row
column = sheet.max_column


for rowNum in range(2, row):
    produceName = sheet.cell(row=rowNum, column=1).value
    if produceName in PRICE_UPDATES:
        sheet.cell(row=rowNum, column=2).value = PRICE_UPDATES[produceName]

