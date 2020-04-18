# 1、创建类
import logging
import os
from datetime import datetime

# 定义日志级别的映射
from config.Conf import get_log_path, ConfigYaml

log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "error": logging.ERROR
}


class Logger:
    # 2、定义参数 文件名称 日志名称 日志级别
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level
        # 3、编写输出控制台和文件的handler
        # 1、设置self.logger名称
        self.logger = logging.getLogger(self.log_name)
        # 2、设置log级别日志
        self.logger.setLevel(log_l[self.log_level])
        # 在创建handler之前判断存不存在
        if not self.logger.handlers:
            # 3、创建handler,用于输出控制台或写入文件
            fh_stream = logging.StreamHandler()  # 这是输出到控制台的handler
            fh_file = logging.FileHandler(self.log_file)  # 这是用于写入文件的handler
            # 4、设置日志级别(区别于第二步，用于差异化打印。)
            fh_stream.setLevel(log_l[self.log_level])  # 给控制台handler单独设置日志界别
            fh_file.setLevel(log_l[self.log_level])  # 给文件handler单独设置日志界别
            # 5、定义handler的输出格式
            formatter = logging.Formatter(' %(asctime)s --%(levelname)s-- %(name)s  %(message)s')
            fh_stream.setFormatter(formatter)
            fh_file.setFormatter(formatter)
            # 6、添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 初始化参数数据
# 日志文件名称,日志文件级别
# 日志文件名称 = log目录 + 时间 + 扩展名
log_path = get_log_path()
# 当前时间
current_time = datetime.now().strftime("%Y-%m-%d")
# 扩展名
log_extension = ConfigYaml().get_conf_log_extension()
# 合并成名字
logfile = os.path.join(log_path, current_time + log_extension)
# 日志文件级别
loglevel = ConfigYaml().get_conf_log()


# 提供对外访问的方法

def log(log_name=__file__):
    return Logger(logfile, log_name, loglevel).logger


if __name__ == '__main__':
    log().debug("这是一个debug")
