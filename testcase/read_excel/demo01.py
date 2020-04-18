#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   demo01
    Author:      Hang
    Date:        2020/4/15/015
    description: 读取excel
   ==============================================

"""

# 导入xlrd模块
import xlrd
# 创建workbook对象
book = xlrd.open_workbook("testdata.xlsx")
# sheet对象(索引(从0开始)/名称)
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name("美多商城接口测试")
# 获取行数和列数
rows = sheet.nrows
cols = sheet.ncols
# 读取每行的内容
# for r in range(rows):
#     r_values = sheet.row_values(r)
#     print(r_values)
# 读取每列的内容
# for c in range(cols):
#     c_values = sheet.col_values(c)
#     print(c_values)
# 读取固定的内容
print(sheet.cell(0,0))
