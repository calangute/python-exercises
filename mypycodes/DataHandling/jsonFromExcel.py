import requests, time
import logging
import json
import ast
import xlrd
from xlrd import open_workbook

book = open_workbook('param.xlsx')

sheet = book.sheet_by_index(0)
keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

print keys

dict_list = []

for row_index in xrange(1, sheet.nrows):
     d = {keys[col_index]: sheet.cell(row_index,col_index).value for col_index in xrange(1,sheet.ncols)}
     dict_list.append(d)

jsonium = json.dumps(dict_list)

print "\n",jsonium
# num_rows = sheet.nrows
# num_cols = sheet.ncols
# header = [sheet.cell_value(0, cell).lower() for cell in range(num_cols)]
#
# for row_id in xrange(1, num_rows):
#    row_cell = [sheet.cell_value(row_id, col_id) for col_id in range(num_cols)]
#    print dict(header, row_cell)

