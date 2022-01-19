# -*- coding: utf-8 -*-
"""
******* 文档说明 ******
读取多进程提取的新词，提取并转换成CSV保存在 result 文件夹下

Time:     2020/11/26 21:46
Author:   ChenXin
Version:  V 0.1
File:     bulletDensity.py
Describe:  Github link: https://github.com/Chen-X666
"""
import asyncio
import os
import pickle
import logging
import shutil
import time
from NewWordDiscovery.get_corpus import get_corpus
import pandas as pd
import re
from .edgeAdvanced import edgeAdavanced
logger = logging.getLogger('NLP')
from NewWordDiscovery.tool.initialingCorpus import *


def standard(csv_path,column):
    df = pd.read_csv(csv_path,encoding='GBK')
    if len(df[column].to_list())==0:print('0')
    else:
        Max = max(df[column].to_list())
        if Max!=0: df[column] = df[column]/Max
        else:print('0')
        df.to_csv(csv_path,encoding='GBK',index=False)

def deleteTemp():
    cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
    file = os.path.join(cwd, 'Temp')
    del_list = os.listdir(file)
    for f in del_list:
        file_path = os.path.join(file, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def get_new_word(args):
    modernCorpus = getModernCorpus(args.modernCorpus)
    newWordCorpus = getNewWordCorpus(args.newWordCorpus)
    # 读取文件夹下所有文件名称
    file_list = os.listdir(os.path.join(args.CWD, 'Temp'))
    # 提取新词发现对应的文件
    file_list = [file_i for file_i in file_list if 'CandidateWordResult_%s' % args.file_name in file_i]
    # 合并各个进程的搜索结果
    result_count = []
    for file_i in sorted(file_list, reverse=False):
        with open(os.path.join(args.CWD, 'Temp', file_i), 'rb') as f_read_tmp:
            # 读取 文本行数 及 各词组词频数
            result_count_i = pickle.load(f_read_tmp)
            # 合并 搜索结果
            result_count.extend(result_count_i)
        logger.info("CandidateWordResult File:  {}  WordNum: {}".format(file_i, len(result_count_i)))

    # 保存到 CSV 文件 中
    csv_path = os.path.join(args.CWD, 'CandidateWordResult',
                            'CandidateWordResult_%s.csv' % (args.file_name))


    with open(csv_path, 'w') as f_csv:
        # 打印标题
        print('Word,Num,Frequence,Mut,Freedom_L,Freedom_R,Den,Rep,Mark', file=f_csv)
        for j, new_word_i in enumerate(result_count):
            # 只提取不含空格的词组
            if ' ' not in new_word_i[0]:
                if new_word_i[0] in newWordCorpus:
                    new_word_i.append(1)
                elif new_word_i[0] in modernCorpus:
                    new_word_i.append(0)
                else:
                    new_word_i.append(-1)
                print_str = '%s,%d,%d,%.1f,%.3f,%.3f,%.3f,%.3f,%d' % (tuple(new_word_i))

                #查看是否还有包含词， 如“4G套餐” 中包含“4G”和“套餐”
                similar_word = [r_i for r_i in result_count[:j] if r_i[0] in new_word_i[0]]

                if len(similar_word) != 0 : pass
                else:print(print_str, file=f_csv)
                # for s_word_i in similar_word:
                #     print_str = '%s,%s,%d,%.1f,%.3f,%.3f' % (print_str, s_word_i[0], s_word_i[2], s_word_i[3],
                #                                              s_word_i[4], s_word_i[5])

                #print(print_str, file=f_csv)


    logger.info("CandidateWordResult path:  {}  ".format(csv_path))
    #standard(csv_path, column='Rep')
    #deleteTemp()#删除全部本地缓存

    return csv_path

if __name__ == '__main__':
    print()