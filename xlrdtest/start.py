# _*_coding:utf-8 _*_
import xlrd
"""
xlrd 急速入门
"""


def test():
    # 打开excel
    data = xlrd.open_workbook('test.xls')

    # 查看sheet names
    print data.sheet_names()

    # 获取工作表的几种方法
    table = data.sheets()[0]
    table2 = data.sheet_by_index(0)

    print table==table2
    print table.row_values(0)
    print table.nrows
    print table.ncols
