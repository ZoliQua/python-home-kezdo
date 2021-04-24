
import xlwings as xw
import datetime as dt


app = xw.Book(r"data/Book1.xlsx")

sheet = app.sheets[0]
# print(sheet.range('A1').value, sheet.range('B1').value, sheet.range('C1').value, sheet.range('D1').value)
print(sheet.range('A1:C40').value)
# sheet.range('A1').value = 1
# sheet.range('A2').value = 'Hello'
# sheet.range('A3').value is None
# sheet.range('A4').value = dt.datetime(2000, 1, 1)
