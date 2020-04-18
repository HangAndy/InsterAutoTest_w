#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   ExcelDate
    Author:      Hang
    Date:        2020/4/15/015
    description: 获取Excel中需要执行的测试用例
   ==============================================

"""
from utils.ExcelUtil import ExcelReader

from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig


class Data:
    def __init__(self, testcase_file, sheet_name):
        # 1、使用excel工具类，获取结果list
        # self.reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
        self.reader = ExcelReader(testcase_file, sheet_name)

    # print(reader.data())

    # 2、列是否运行内容，y
    def get_run_data(self):
        """
        根据是否运行列==y，获取执行测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                # print(line)
                # 3、保存要执行结果，放到新的列表。
                run_list.append(line)
        return run_list





if __name__ == '__main__':
    data = Data("../data/testdata.xlsx", 0)
    print(data.get_run_data())