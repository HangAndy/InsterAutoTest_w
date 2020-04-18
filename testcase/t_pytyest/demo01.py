#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   demo01
    Author:      Hang
    Date:        2020/4/13/013
    description: 
   ==============================================

"""


# 1、创建简单的测试方法
#

# 普通方法
import pytest


def fun(x):
    x + 1


# 断言方法
def test_a():
    print("test_a")
    assert fun(3) == 5  # 失败用例


# 断言方法
def test_b():
    print("test_a")
    assert 1  # 成功用例


# 2、pytest运行
"""
1、Pycharm代码
2、命令行
"""
# 1
if __name__ == '__main__':
    pytest.main(["demo01.py"])
# 2
# 命令行下 执行 pytest  demo01.py
