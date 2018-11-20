#-*- coding:utf-8 -*-
# author: Wang Xu
import logging
from config import settings

class Logger(object):
    def __init__(self):
        self.log_file_path = settings.LOG_FILE_PATH

        file_handler = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s:  %(message)s")
        file_handler.setFormatter(fmt)


        self.logger = logging.Logger('s1', level=logging.INFO)
        self.logger.addHandler(file_handler)
    def info(self,msg):
        self.logger.info(msg)

    def error(self,msg):
        self.logger.error(msg)

logger = Logger()