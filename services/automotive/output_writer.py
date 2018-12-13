# coding=utf-8

import os, sys
import xlsxwriter


class OutputWriter:

    @classmethod
    def write_to_txt(cls, file, data):
        print('automotive service write to TXT...')
        result_file = open(file, mode='w')
        result_file.write("{},{}\n".format(data['car_brand'], data['car_price']))
        result_file.close()

    @classmethod
    def write_to_excel(cls, file, data):
        print('automotive service write to Excel...')
        # 生成Excel
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        # 标题
        worksheet.write(0, 0, '汽车品牌')
        worksheet.write(0, 1, '汽车价格')
        # 数据
        line_number = 1
        worksheet.write(line_number, 0, data['car_brand'])
        worksheet.write(line_number, 1, data['car_price'])
        workbook.close()

