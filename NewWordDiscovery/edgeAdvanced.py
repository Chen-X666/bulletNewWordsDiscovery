# _*_ coding: utf-8 _*_
"""
Time:     2021/12/27 22:13
Author:   ChenXin
Version:  V 0.1
File:     edgeAdvanced.py
Describe:  Github link: https://github.com/Chen-X666
"""
import re

def edgeAdavanced(keyword,corpus):
    #hfile = open("testData.txt", "r", encoding='utf-8');
    #sReadfile = hfile.read();
    #hfile.close()
    #keyword = "给力"
    count_left = 0;
    count_right = 0;
    count_mid = 0;
    count_all = 0;

    macth_left = re.finditer(r'(?im)(?<!\S)' + keyword + '\S+', corpus)
    if macth_left:
        for everymatch in macth_left:
            count_left += 1;
            # print(count_left , ' ',everymatch.group())

    macth_right = re.finditer(r'(?im)\S+' + keyword + '(?!\S)', corpus)
    if macth_right:
        for everymatch in macth_right:
            count_right += 1;
            # print(count_right , ' ',everymatch.group())

    macth_mid = re.finditer(r'(?im)(?<!\S)' + keyword + '(?!\S)', corpus)
    if macth_mid:
        for everymatch in macth_mid:
            count_mid += 1;
            # print(count_mid , ' ',everymatch.group())

    macth_all = re.finditer(r'(?im)' + keyword, corpus)
    if macth_all:
        for everymatch in macth_all:
            count_all += 1;
            # print(count_all , ' ',everymatch.group())

    # 打印结果
    # print(keyword)
    # print('的左边界initial: ', str(count_left) + '/' + str(count_all))
    # print('的右边界end: ', str(count_right) + '/' + str(count_all))
    # print('的独立indep: ', str(count_mid) + '/' + str(count_all))
    return (count_left+count_right+count_mid)/count_all

if __name__ == '__main__':
    hfile = open("testData.txt", "r", encoding='utf-8');
    sReadfile = hfile.read();
    hfile.close()
    keyword = "给力"
    edgeAdavanced(keyword,sReadfile)
