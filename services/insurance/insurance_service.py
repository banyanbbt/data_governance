# coding=utf-8

from services.base import BaseService


class InsuranceService(BaseService):

    @classmethod
    def process_file(cls, content):
        print('insurance service process...')
