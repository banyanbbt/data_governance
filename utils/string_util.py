# coding=utf-8

# Tips
# utf8 下，每个汉字占据3个字符位置，正则式为[\x80-\xff]{3}

import re


def brand_regexp(content):
    # type: (string) -> string
    """
    匹配中文符合 【 xxx 】中间的品牌名称。

    """
    pattern = r"【.+】"
    result = re.search(pattern, content)
    if result is not None:
        brand_str = result.group(0)
        if brand_str is not None:
            brand_name = brand_str[1:-1]
            print(brand_name)
            return brand_name


def date_regexp(content):
    # type: (string) -> string
    """
    匹配日期。格式如下：
    2017年06月26日  \d{4}年\d{2}月\d{2}日
    2017-07-30     \d{4}-\d{2}-\d{2}
    2017.07.30     \d{4}.\d{2}.\d{2}
    06月26日        \d{2}月\d{2}日
    06-26          \d{2}-\d{2}
    06.26          \d{2}.\d{2}

    """
    # pattern = ur"\d{4}?[\u5e74-.]?\d{2}[\u6708-.]\d{2}\u65e5?"
    result = re.search("\d{4}年\d{2}月\d{2}日", content)
    if result is not None:
        print(result.group(0))
    else:
        result = re.search("\d{4}[-|\.]\d{2}[-|\.]\d{2}", content)
        if result is not None:
            print(result.group(0))
        else:
            result = re.search("\d{2}月\d{2}日", content)
            if result is not None:
                print(result.group(0))
            else:
                result = re.search("\d{2}[-|\.]\d{2}", content)
                if result is not None:
                    print(result.group(0))
                else:
                    print("no date matched")


def price_regexp(content):
    # type: (string) -> string
    """
    匹配日期。格式如下：
    99元     (\d+)元
    99.99元  (\d+.\d+)元

    """
    # pattern = ur"(\d+.\d+)元"
    r = re.compile("(\d+.\d+)元")
    result = r.search(content)
    if result is not None:
        print(result.group(0))
        # print(result.group(1)
    else:
        print("no price matched")
