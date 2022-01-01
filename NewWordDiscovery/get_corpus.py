# -*- coding: utf-8 -*-
"""
******* 文档说明 ******
获取语料程序，以迭代器方式返回， 数据预处理模块

Time:     2020/11/26 21:46
Author:   ChenXin
Version:  V 0.1
File:     bulletDensity.py
Describe:  Github link: https://github.com/Chen-X666
"""
import logging
import re
import csv
import os
from collections import Counter

from NewWordDiscovery.langconv import *
from NewWordDiscovery.initialCorpus import getEmojiCorpus,getModernCorpus,getNewWordCorpus
from NewWordDiscovery.tool.flashText import *
import pandas as pd

logger = logging.getLogger('NLP')

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

#输出颜文字新词
def toEmojisCsv(emojis,file_name):
    csv_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')), 'NewWordResult',
                            'NewWordResult_%s.csv' % (file_name))
    with open(csv_path, 'w',encoding='utf-8') as f_csv:
        # 打印标题
        print('NewWord', file=f_csv)
        for i in emojis:
            print(i, file=f_csv)
    logger.info("NewWordResult path:  {}  ".format(csv_path))

# 文本数据读取 迭代器 【更换训练文本数据时，请对应修改此函数代码】
def get_corpus(file, data_col=None, txt_sep=None, encoding='utf8', clean=True, Tra2Sim=True, emojiCorpus=None, file_name=None):
    """
    :param file:         文件路径
    :param data_col:     提取文本的列序号 【从 0 开始】
    :param txt_sep:     非csv文件的切分字符
    :param encoding:    默认'utf8'
    :param clean:    正则清洗，只提取汉字、数字、字母   默认 True 【新词发现时必须为True模式】
    :return:   会话文本，迭代器
    """
    # 输入文件名时，默认其存放路径为 .\NLP\Data'
    logger.info('DataPretreatment——————————loading file——————————DataPretreatment')
    if not os.path.isfile(file):
        #  当前文件路径 的上层路径， 'NLP' 所在目录   'C:\Users\Chen\Desktop\NLP'
        cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
        file = os.path.join(cwd, 'Data', file)

    # csv 文件第 data_col 列为文本数据
    bulletTexts = pd.read_csv(file, encoding=encoding, index_col=0)[data_col]
    #print(bulletTexts)
    # 颜文字新词发现
    logger.info('DataPretreatment——————————building emojis adTrie——————————DataPretreatment')
    actree = build_actree(getEmojiCorpus(emojiCorpus))
    # 颜文字新词发现，只匹配已有字典
    emojis = ac_detect(actree=actree, text=bulletTexts.to_string())
    emojis = Counter(emojis)
    toEmojisCsv(emojis=emojis,file_name=file_name)
    logger.info('DataPretreatment——————————emojis discovery finished——————————DataPretreatment')
    logger.info('DataPretreatment——————————Starting Clean(tra2sim+cap2low)——————————DataPretreatment')
    # 正则清洗，只提取汉字、数字、字母
    if clean:
        # 正则表达式转换，只提取汉字、数字、字母
        re_clean = re.compile('[^\u4e00-\u9fa5 a-zA-Z0-9 \n]')
        # 将多个空格 替换成一个空格
        re_sub = re.compile(' +')

        # 读取 CSV 文件数据
        if file[-3:] == 'csv':
            for line_data in bulletTexts:
                # 若文本长度大于0， 则通过迭代器输出
                if len(line_data) > 0:
                    # 正则清洗
                    line_data = re.sub(re_clean, '\n', line_data)
                    if Tra2Sim:
                        #繁体转简体 大写转小写
                        line_data = Traditional2Simplified(line_data.lower())
                        line_data = re.sub(re_sub,'\n', line_data)
                        line_data = line_data + '\n'
                    yield line_data

        # 读取 其它 文件数据
        else:
            for line_data in bulletTexts:
                # 若文本长度大于0， 则通过迭代器输出
                if len(line_data) > 0:
                    # 正则清洗
                    line_data = re.sub(re_clean, '\n', line_data)
                    if Tra2Sim:
                        #繁体转简体 大写转小写
                        line_data = Traditional2Simplified(line_data.lower())
                        line_data = re.sub(re_sub, '\n', line_data)
                    yield line_data

    # 提取原文、标签
    else:
        # 读取 CSV 文件数据
        if file[-3:] == 'csv':
            for line_data in bulletTexts:
                yield line_data

        # 读取 其它 文件数据
        else:
            for line_data in open(file, encoding=encoding, errors='ignore'):
                line_data = line_data.split(txt_sep)  # txt 文件以txt_sep为分隔符
                corpus = line_data[data_col]  # csv 文件第 data_col 列为文本数据
                yield corpus

# 文件打开配置调试
if __name__ == '__main__':
    corpus_data = get_corpus(r'C:\Users\Chen\Desktop\bulletProjects\bulletNewWordsDiscovery\Data\BV1a54y1q7ZZ.csv', data_col='bulletContent', txt_sep='\n',
                             encoding='utf-8', clean=True, emojiCorpus='emojis.csv', file_name='BV1a54y1q7ZZ')
    print(corpus_data)
    for i, corpus_i in enumerate(corpus_data):
        print(i, corpus_i[:30])
        if i > 10000:
            break
