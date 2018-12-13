# coding=utf-8

import os, sys
import xlsxwriter


class OutputWriter:

    @classmethod
    def write_to_txt(cls, file, data):
        print('tourism service write to TXT...')
        result_file = open(file, mode='w')
        result_file.write("{},{}\n".format(data['tourism_brand'], data['tourism_price']))
        result_file.close()

    @classmethod
    def write_to_excel(cls, file, data):
        print('tourism service write to Excel...')
        # 生成Excel
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        # 标题
        worksheet.write(0, 0, '旅游品牌')
        worksheet.write(0, 1, '旅游价格')
        # 数据
        line_number = 1
        worksheet.write(line_number, 0, data['tourism_brand'])
        worksheet.write(line_number, 1, data['tourism_price'])
        workbook.close()

