# coding=utf-8

import os
import re
import jieba
import json


class BaseAnalyzer:
    def __init__(self, content):
        self.content = content

    def cut_text(self, text, cuts):
        left = 0
        result = []
        cuts += [len(text)]
        cuts.sort()
        for c in cuts:
            tmp = text[left:c]
            if tmp:
                result += [tmp]
                left = c
        return result

    def scene(self, scene_code):
        self.scene_code = scene_code

    def segment(self, text):
        self.content['brand_name']
        cuts = [0]
        segs = [i for i in jieba.cut(text)]
        for i in range(len(segs)):
            cuts.append(cuts[i] + len(segs[i]))
        result = self.cut_text(text, cuts)
        return result

    def mark(self, split_content, mark_content):
        self.split_result = json.dumps(split_content, ensure_ascii=False)
        self.mark_result = json.dumps(mark_content, ensure_ascii=False)
