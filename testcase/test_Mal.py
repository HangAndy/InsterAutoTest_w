#!/usr/bin/env python
# encoding: utf-8
"""
   ==============================================
    objectName： InsterAutoTest_w
    fileName：   test_Mal
    Author:      Hang
    Date:        2020/4/8
    description:
    login_5	登录	登录用户名或密码错误	/authorizations/
    POST	json	{"username":"python","password"	无法使用提供的认证信息登录	n	400
   ==============================================

"""
import pytest
import requests

from utils.AssertUtils import AssertUtil
from utils.RequesteUtil import Requests


class Test_shopping:
    def test_login(self):
        print("\ntest_login执行了\n")
        # 定义数据
        url = "http://211.103.136.242:8064/authorizations/"
        data = {"username": "python", "password": "12345678"}
        # 发送请求
        r = Requests().post(url, json=data)
        print(r)

    def test_info(self):
        print("\ntest_info执行了\n")
        # 1、参数
        url = "http://211.103.136.242:8064/user/"
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODY0MDg5NTksInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.OLD7s2nLKV65WsjLywh73bqdSz885Dqhtg7WKHzyras"
        headers = {
            'Authorization': 'JWT ' + token
        }
        r = Requests().get(url, headers=headers)
        print(r)

    def test_goods_list(self):
        pass
        # 1、参数
        print("\ngoods_list执行了\n")
        url = "http://211.103.136.242:8064/categories/115/skus/"
        data = {
            "page": "1",
            "page_size": "10",
            "ordering": "create_time"
        }
        # 发送请求
        r = requests.get(url, json=data)
        AssertUtil().assert_code(r.status_code, "200")


if __name__ == '__main__':
    pytest.main(["test_Mal.py"])
