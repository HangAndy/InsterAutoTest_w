# coding=gbk
import time
import unittest



suite = unittest.TestSuite()  # ��ʼ���׼�����

# ���÷�����װ��������
suite.addTest(unittest.makeSuite(TestApplyForLogin))
# �ر�������˳�����
DriverUtil.change_quit_status(False)
# TODO: ���ɲ��Ա���(��Ҫע�͵� TextTestRunner() ����)
now_time = time.strftime('%Y%m%d_%H%M%S')  # ��ȡ��ǰʱ��
# ��ʼ������ִ�ж��󲢵��÷���
unittest.TextTestRunner().run(suite)
# ���ñ�������Ϣ

time.sleep(20)
