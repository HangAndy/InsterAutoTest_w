#!/usr/bin/env python 
# encoding: utf-8 
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   demo03
    Author:      Hang
    Date:        2020/4/13/013
    description: 参数化
   ==============================================

"""
import pytest


class TestDemo:
    data_list = ["小明", "xiaoming"]
    data_list2 = [("xiaoming", "123456"), ("xiaohong", "456123")]

    # @pytest.mark.parametrize("name", data_list)
    # def test_a(self, name):
    #     print("test_a", name)
    #     assert 1

    @pytest.mark.parametrize(("name", "password"), data_list2)
    def test_a(self, name, password):
        print("test_a", name, password)
        assert 1


if __name__ == '__main__':
    pytest.main(["-s", "demo03.py"])
