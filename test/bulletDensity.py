# _*_ coding: utf-8 _*_
"""
Time:     2021/11/26 21:46
Author:   ChenXin
Version:  V 0.1
File:     bulletDensity.py
Describe:  Github link: https://github.com/Chen-X666
"""
import csv
import re

import pandas as pd
import numpy as np


def findkeywordnum(sTxtStr,keyword):
  maxnum=0
  macthall = re.finditer(r'(?im)^.*?' + re.escape(keyword) +  '.*' , sTxtStr)
  if macthall:
     for everymatch in macthall:
         matchObj = re.findall('(?im)' + re.escape(keyword) ,everymatch.group())
         if matchObj:
            if len(matchObj) > maxnum:
               maxnum=len(matchObj)
  return maxnum

def candicateDen(videoLength,sTxtStr,keyword):
    videoLength = videoLength
    count = 0
    macthall = re.finditer(r'(?im)^.*?' + re.escape(keyword) + '.*', sTxtStr)
    if macthall:
        for everymatch in macthall:
            count += 1
    return count


# 搜索函数
def findkeywordnumc( sTxtStr , keyword):
  maxnum=0
  macthall = re.finditer(r'(?i)(' + re.escape(keyword) +  ')+' , sTxtStr)
  if macthall:
     for everymatch in macthall:
         #print(everymatch.group())
         macthLine = re.finditer(r'(?i)' + re.escape(keyword) , everymatch.group())
         if macthLine:
            countnum=0
            for mctline in macthLine:
               countnum+=1
            if countnum > maxnum:
              maxnum=countnum
  return maxnum


if __name__ == '__main__':
    # df = pd.read_csv('BV1j4411W7F7.csv',encoding='utf-8')
    # df = df.sort_values('dm_time', ascending=True)
    # dfText = df['dm_text']
    # candidate = pd.read_csv('标注集.csv',encoding='GBK')
    # #复用率
    # # 读取文件内容
    # sTxtStr = df['dm_text'].to_string(index=False)
    # denList = []
    # repList = []
    # cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9^\n]")  # 匹配不是中文、大小写、数字的其他字符
    # sTxtStr = cop.sub('', sTxtStr)
    # #复用率
    # for i in candidate['Word']:
    #     keyword = i  # 搜索关键词
    #     findnum = findkeywordnum(sTxtStr, keyword)
    #     repList.append(findnum)
    # Di1 = max(repList)
    # candidate['Rep'] = np.array(repList)/Di1
    # #词频密度
    # for i in candidate['Word']:
    #     keyword = i
    #     findnum = candicateDen(max(df['dm_time']),sTxtStr,keyword)
    #     denList.append(findnum)
    # Di2 = max(denList)
    # candidate['Den'] = np.array(denList)/Di2
    # print(candidate)
    # candidate.to_csv('training.csv',encoding='utf-8',index=False)
    # 读取文件内容
    hfile = open("2.txt", "r", encoding='utf-8');
    sTxtStr = hfile.read()
    print(sTxtStr)
    hfile.close()

    keyword = "给力"  # 搜索关键词
    #findnum = findkeywordnumc(sTxtStr, keyword)
    den = candicateDen(123,str(sTxtStr),keyword)
    print(den)



