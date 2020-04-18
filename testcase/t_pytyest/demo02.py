#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   demo01
    Author:      Hang
    Date:        2020/4/13/013
    description:  基础使用
   ==============================================

"""

# 1、创建简单的测试方法
#

# 普通方法
import pytest


def fun(x):
    x + 1


class TestFunc:

    def setup_class(self):
        print("--setup_class--")

    def setup(self):
        print("--setup--")

    def teardown(self):
        print("--teardown--")

    def teardown_class(self):
        print("--teardown_class--")

    # 断言方法
    def test_a(self):
        print("test_a")

    # 断言方法
    def test_b(self):
        print("test_b")


# 2、pytest运行
"""
1、Pycharm代码
2、命令行
"""
# 1
if __name__ == '__main__':
    pytest.main(["-s", "demo02.py"])
# 2
# 命令行下 执行 pytest  demo01.py
