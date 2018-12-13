# coding=utf-8


class BaseService:
    def __init__(self, content):
        self.content = content

    def sender(self):
        self.content['sender']

    def brand_name(self):
        self.content['brand_name']

    def receiver_time(self):
        self.content['receiver_time']
