#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   AssertUtils
    Author:      Hang
    Date:        2020/4/15/015
    description: 
   ==============================================

"""
from utils.LogUtil import log


class AssertUtil:
    def __init__(self):
        self.log = log("AssertUtil")

    def assert_code(self, code, expected_code):
        """
        判断code相等
        :param code: 带比较的值
        :param expected_code: 预期的
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            self.log.info("validating response code, validation successful")
            return True
        except:
            self.log.error("code error, code is %s, but the expected code is %s" % (code, expected_code))
            raise
