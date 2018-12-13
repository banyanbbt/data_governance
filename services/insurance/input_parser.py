# coding=utf-8

import os, sys


class InputParser:

    @classmethod
    def parse_file(cls, file):
        print('insurance service process...')
        with open(file) as tf:
            for line in tf:
                content = line.rstrip('\n')
                if content != '' and content != None:
                    data = content.split(',')
                    insurance_brand = data[0].strip()
                    insurance_price = data[1].strip()

