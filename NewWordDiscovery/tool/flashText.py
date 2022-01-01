# _*_ coding: utf-8 _*_
"""
Time:     2021/12/31 13:10
Author:   ChenXin
Version:  V 0.1
File:     flashText.py
Describe:  Github link: https://github.com/Chen-X666
"""
from flashtext import KeywordProcessor

def build_actree(wordlist):
    '''
        AC自动机进行关键词匹配
        构造AC trie
    '''
    actree = KeywordProcessor()
    for index, word in enumerate(wordlist):
        actree.add_keyword(word)     # 向trie树中添加单词
    #self.actree = actree
    return actree

def ac_detect(actree,text,span_info = True):
    '''
        AC自动机进行关键词匹配
        文本匹配
    '''
    region_wds = []
    for w1 in actree.extract_keywords(text,span_info = span_info):
        if len(w1) > 0:
            region_wds.append(w1[0])
    return region_wds

if __name__ == '__main__':
    wordlist = ['健康','减肥']
    text = '今天你减肥了吗，今天你健康了吗，减肥 = 健康！'
    actree = build_actree(wordlist)
    print(ac_detect(actree,text))