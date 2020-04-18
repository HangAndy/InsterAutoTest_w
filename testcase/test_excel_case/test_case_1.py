#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   test_case_1
    Author:      Hang
    Date:        2020/4/15/015
    description: 
   ==============================================

"""
import os

from common.ExcelDate import Data
from config.Conf import ConfigYaml
from utils.LogUtil import log
from common import ExcelConfig

#
# case_file = os.path.join("../data", ConfigYaml().get_excel_file())
sheet_index = ConfigYaml().get_excel_sheet()
run_list = Data("../../data/testdata.xlsx", int(sheet_index)).get_run_data()
log = log()


class TestExcel:
    def test_run(self):
        data_key = ExcelConfig.DataConfig
        url = ConfigYaml().get_conf_url() + run_list[0][data_key.url]0
        print(url)


TestExcel().test_run()
