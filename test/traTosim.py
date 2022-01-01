# _*_ coding: utf-8 _*_
"""
Time:     2021/7/20 10:46
Author:   ChenXin
Version:  V 0.1
File:     getBulletByBvno.py
Describe:  Github link: https://github.com/Chen-X666
"""
import os
import os.path  # 文件夹遍历函数
from langconv import *
import re
import pandas as pd

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

def getData(path):
	file = open(path,encoding='utf-8')
	line = file.read().splitlines()
	file.close()
	return line

def getAllTxt(filesPath,resultPath):
    # coding=utf-8
    # 获取目标文件夹的路径
    filedir = filesPath
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(filedir)
    # 打开当前目录下的result.txt文件，如果没有则创建
    f = open(resultPath, 'w',encoding='utf-8')
    # 先遍历文件名
    for filename in filenames:
        filepath = filedir + '/' + filename
        # 遍历单个文件，读取行数
        for line in open(filepath,encoding='utf-8'):
            f.writelines(line)
        f.write('\n')
    # 关闭文件
    f.close()

if __name__=="__main__":
    f = open(file='../../Data/allData/guichuAll.txt', encoding='utf-8')
    data = f.readlines()
    f.close()
    with open("../../Data/allData/guichuAllToSimpleLanguage.txt", "w", encoding='utf-8') as f1:
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^\n]")
        for line in data:
            line = Traditional2Simplified(line.lower())
            line = cop.sub('', line)
            if line != '\n':
                f1.write(line)
    f1.close()
    print('finished')




