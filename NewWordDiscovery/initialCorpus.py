# _*_ coding: utf-8 _*_
"""
Time:     2021/12/5 0:13
Author:   ChenXin
Version:  V 0.1
File:     initialCorpus.py
Describe:  Github link: https://github.com/Chen-X666
"""
import logging
import os
import pandas as pd

logger = logging.getLogger('NLP')
#  当前文件路径 的上层路径， 'NLP' 所在目录   'C:\Users\Chen\Desktop\NewWordDiscovery'
cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

def getEmojiCorpus(file):
    # 输入文件名时，默认其存放路径为 .\Corpus'

    if not os.path.isfile(file):
        filePath = os.path.join(cwd, 'Corpus', file)
    return pd.read_csv(filePath,encoding='utf-8')['emojis'].to_list()

def getModernCorpus(file):
    # 输入文件名时，默认其存放路径为 .\Corpus'
    if not os.path.isfile(file):
        filePath = os.path.join(cwd, 'Corpus', file)
    return pd.read_csv(filePath,encoding='utf-8')['词语'].to_list()

def getNewWordCorpus(file):
    # 输入文件名时，默认其存放路径为 .\Corpus'
    if not os.path.isfile(file):
        filePath = os.path.join(cwd, 'Corpus', file)
    return pd.read_csv(filePath,encoding='utf-8')['newWord'].to_list()

def getRamdomForestModel(file):
    # 输入文件名时，默认其存放路径为 .\Corpus'
    if not os.path.isfile(file):
        filePath = os.path.join(cwd, 'Corpus', file)
    return filePath

if __name__ == '__main__':
    print()