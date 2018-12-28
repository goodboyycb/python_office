# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:06:31 2018

@author: goodboyycb
"""

import xlrd
import xlwt
help (xlrd)
book=xlrd.open_workbook("E:/jsdmcdy.xls")
sheets=book.sheets()
for sheet in sheets:
    print(sheet.name)
    
    
sheet=book.sheets()[0]
rows=sheet.get_rows()
for row in rows:
   ## print
    print(row[1].value,row[2].value)