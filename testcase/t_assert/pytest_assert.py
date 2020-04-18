#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   pytest_assert
    Author:      Hang
    Date:        2020/4/15/015
    description: 断言
   ==============================================

"""
import pytest


def test_1():
    a = True
    assert a


def test_2():
    a = True
    assert not a


if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])
