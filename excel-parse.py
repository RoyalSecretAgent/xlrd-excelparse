__author__ = 'Administrator'
import xlrd

wb = xlrd.open_workbook("excel.xlsx")

first_index = wb.sheet_by_index(0)
ncol = first_index.ncols
nlow = first_index.nrows

list = first_index.row_values(0)
print (list)
i = 1
while i < nlow:
    print (str(first_index.row_values(i)))
    i+=1

