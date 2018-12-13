# coding=utf-8

from services.base import BaseService


class TourismService(BaseService):

    @classmethod
    def process_file(cls, content):
        print('tourism service process...')
