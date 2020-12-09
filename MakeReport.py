# coding:utf-8
# 我是main
import os
from time import sleep
import datetime
import shutil
import glob
import logging
from dateutil.relativedelta import relativedelta
import win32com.client as win32
import openpyxl
from openpyxl.styles import Font, numbers, Border, Side, PatternFill
import MyMainDialog

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
# FileHandler 将日志输出到文件log.log
file_handler = logging.FileHandler('log.log', encoding='utf8')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logging.info('打印日志')
logging.info('我是main')
