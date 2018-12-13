# coding=utf-8

import os, sys


class InputParser:

    @classmethod
    def parse_file(cls, file):
        print('automotive service process...')
        with open(file) as tf:
            for line in tf:
                content = line.rstrip('\n')
                if content != '' and content != None:
                    data = content.split(',')
                    car_brand = data[0].strip()
                    car_price = data[1].strip()

