# coding=utf-8

# 二、编码规则：公民身份号码是特征组合码，由十七位数字本体码和一位校验码组成。排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码，可以用字母表示如为ABCDEFYYYYMMDDXXXR。其含义如下：
# 1. 地址码（ABCDEF）：表示编码对象常住户口所在县(市、旗、区)的行政区划代码，按GB/T2260的规定执行。
# 2.出生日期码（YYYYMMDD）：表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日分别用4位、2位（不足两位加0）、2位（不足两位加0）数字表示，之间不用分隔符。
# 3.顺序码（XXX）：表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。
# 4．校验码（R），一位数字，通过前17位数字根据一定计算得出，检验码分别是“0、1、2、……10”共11个数字，当检验码为“10”时，为了保证公民身份证号码18位，所以用“X”表示。
# 三、15位身份证号码：当今的身份证号码有15位和18位之分。1985年我国实行居民身份证制度，当时签发的身份证号码是15位的，1999年签发的身份证由于年份的扩展（由两位变为四位）和末尾加了效验码，就成了18位。这两种身份证号码将在相当长的一段时期内共存。15位身份证号码的排列为ABCDEFYYMMDDXXX，其含义基本与18位的身份证号码的含义相同，只是年份是2位表示，且没有校验码。


import os, sys
from datetime import date, datetime


city_dict = {'110000':'北京市','110100':'北京市市辖区','110101':'北京市东城区','110102':'北京市西城区'}


def parse_birthday(account, account_len):
    birthday = ''
    if account_len == 18:
        birthday = account[6:14]
    elif account_len == 15:
        birthday = account[6:12]
    return birthday


def parse_gender(account, account_len):
    gender = ''
    if account_len == 18:
        gender = account[16:17]
    elif account_len == 15:
        gender = account[13:14]
    if int(gender) % 2 == 0:
        return '女'
    else:
        return '男'


def parse_city(account, account_len):
    city = '未知'
    city_str = account[0:6]
    if city_str in city_dict:
        city = city_dict[city_str]
    return city


def calculate_age(today, birthday, account_len):
    if account_len == 18:
        born = datetime.strptime(birthday, "%Y%m%d").date()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    else:
        born = datetime.strptime("19{}".format(birthday), "%Y%m%d").date()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def  jiaquan(n):
    w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s=0
    for i in range(17):
        s+=n[i]*w[i]
    return s


def last_num(n):
    s = jiaquan(n)
    y = s%11
    zidian = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
    return zidian[y]


def is_validate(account, account_len):
    if account_len == 18:
        n = []
        for i in account[:-1]:
            n.append(int(i))
        last = last_num(n)
        if last == account[-1]:
            return '正确'
        else:
            return '错误'
    elif account_len == 15:
        return '正确'
    else:
        return '错误'


def process(source_file):
    print('Start process source files...')

    today = date.today()
    with open(source_file) as tf:
        for line in tf:
            content = line.rstrip('\n')
            if content != '' and content != None:
                user = content.split(',')
                account = user[0].strip()
                name = user[1].strip()
                account_len = len(account)
                if account_len == 18 or account_len == 15:
                    birthday = parse_birthday(account, account_len)
                    age = calculate_age(today, birthday, account_len)
                    gender = parse_gender(account, account_len)
                    birth_city = parse_city(account, account_len)

    print('End process source files...')



