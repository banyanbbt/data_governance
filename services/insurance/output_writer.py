# coding=utf-8

import os, sys
import xlsxwriter


class OutputWriter:

    @classmethod
    def write_to_txt(cls, file, data):
        print('insurance service write to TXT...')
        result_file = open(file, mode='w')
        result_file.write("{},{}\n".format(data['insurance_brand'], data['insurance_price']))
        result_file.close()

    @classmethod
    def write_to_excel(cls, file, data):
        print('insurance service write to Excel...')
        # 生成Excel
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        # 标题
        worksheet.write(0, 0, '保险品牌')
        worksheet.write(0, 1, '保险价格')
        # 数据
        line_number = 1
        worksheet.write(line_number, 0, data['insurance_brand'])
        worksheet.write(line_number, 1, data['insurance_price'])
        workbook.close()

