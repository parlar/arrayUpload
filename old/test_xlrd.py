import sys
import os
import csv
import xlrd

path = "C:/Users/parlar/Documents/test.xls"

print(path)
book = xlrd.open_workbook(path, 'r')
sheet = book.sheet_by_index(0)