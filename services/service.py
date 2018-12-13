# coding=utf-8

import utils.string_util as string_util
import utils.brand_rules as brand_rules
from services.automotive.automotive_service import AutomotiveService
from services.insurance.insurance_service import InsuranceService
from services.tourism.tourism_service import TourismService

class Service:

    @classmethod
    def process_file(cls, content):
        # TIPs
        # 初步解析内容的重要字段
        # 写入行业、品牌的独立文件内
        # 识别出品牌名称 brand name，品牌价格 brand price
        brand_name = string_util.brand_regexp(content)
        if brand_name is not None:
            if brand_name in brand_rules.brand_rules['automotive']:
                AutomotiveService.process_file(content)
            elif brand_name in brand_rules.brand_rules['insurance']:
                InsuranceService.process_file(content)
            elif brand_name in brand_rules.brand_rules['tourism']:
                TourismService.process_file(content)
            else:
                print('Unknown brand name %s' % brand_name)
            # search date
            string_util.date_regexp(content)
            # search price
            string_util.price_regexp(content)

