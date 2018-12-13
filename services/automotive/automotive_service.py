# coding=utf-8

from services.base import BaseService


class AutomotiveService(BaseService):

    @classmethod
    def process_file(cls, content):
        # TIPs
        # 新建行业文件夹
        # 创建独立子文件，写入识别的内容，保留原文本
        print('automotive service process...')
