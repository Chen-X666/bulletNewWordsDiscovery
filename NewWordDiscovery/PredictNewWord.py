# _*_ coding: utf-8 _*_
"""
Time:     2022/1/1 17:52
Author:   ChenXin
Version:  V 0.1
File:     RandomForest.py
Describe:  Github link: https://github.com/Chen-X666
"""
import logging
import os

import joblib

from NewWordDiscovery import initialCorpus

logger = logging.getLogger('NLP')
#  当前文件路径 的上层路径， 'NLP' 所在目录   'C:\Users\Chen\Desktop\NewWordDiscovery'
cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

def predictNewWord():
    joblib.load(initialCorpus.getRamdomForestModel('RandomForest.model'))

if __name__ == '__main__':
    predictNewWord()