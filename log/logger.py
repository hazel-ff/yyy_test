# 时间：2023/12/18 10:24
import logging
import os.path
import time


class logger():
    def logger(self,level,msg):
        logger = logging.getLogger()
        logger.setLevel("INFO")
        # 创建一个输出到控制台的渠道
        ch = logging.StreamHandler()
        # 获取当前目录的绝对路径
        root_path = os.path.abspath(os.path.dirname(__file__)).split('shippingSchedule')[0]
        # 创建输出到文件的路径
        fh = logging.FileHandler(root_path+'/log.txt',encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s-'
            '%(levelname)s-'
            '%(filename)s-'
            '%(name)s:'
            '%(message)s'
        )
        # 设置控制台 文件打印格式
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 设置收集级别
        ch.setLevel('INFO')
        fh.setLevel('INFO')

        # 日志收集器与输出渠道对接
        logger.addHandler(ch)
        logger.addHandler(fh)
        if level=='INFO':
            logger.info(msg)
        elif level=='WARNING':
            logger.warning(msg)
        elif level=='ERROR':
            logger.error(msg)
        else:
            logger.critical(msg)

        # 每次收集日志后移除日志收集器
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # logger.removeFilter(ch)
        # logger.removeFilter(fh)
        ch.close()
        fh.close()

    def info(self,msg):
        self.logger('INFO',msg)

    def warning(self,msg):
        self.logger('WARNING',msg)

    def error(self,msg):
        self.logger('ERROR',msg)

if __name__ == '__main__':
    log = logger()
    # log.info(111)
    # time.sleep(2)
    log.info(222)


