# coding=gbk
import time
import unittest



suite = unittest.TestSuite()  # 初始化套件对象

# 调用方法组装测试用例
suite.addTest(unittest.makeSuite(TestApplyForLogin))
# 关闭浏览器退出方法
DriverUtil.change_quit_status(False)
# TODO: 生成测试报告(需要注释掉 TextTestRunner() 方法)
now_time = time.strftime('%Y%m%d_%H%M%S')  # 获取当前时间
# 初始化测试执行对象并调用方法
unittest.TextTestRunner().run(suite)
# 设置报告存放信息

time.sleep(20)
