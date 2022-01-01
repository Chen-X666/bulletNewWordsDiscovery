# -*- coding: utf-8 -*-
"""
******* 文档说明 ******
# 当前项目: NewWordDiscovery
# 创建时间: 2020/10/5 16:50
# 开发作者: Chen
# 创建平台: PyCharm Community Edition    python 3.8
# 版    本: V1.0
"""
import asyncio
import os
import time

import pandas as pd


if __name__ == '__main__':
    # #####################################  弹幕获取  返回提取的新词存储表格 **.csv 路径
    time.sleep(2)
    bvids = pd.read_csv('Data/100预测.csv')['videoBvno'].tolist()

    for bvid in bvids:
    #     #bvid = 'BV1qt411j7fV'
        from NewWordDiscovery import new_word_discover  # 新词发现程序
        new_word_discover(bvid+'.csv', f_data_col='bulletContent', f_time_col='videoLength', f_encoding='utf-8', f_txt_sep='\n',
                          batch_len=10000000,
                          n_gram=5, p_min=10, co_min=5.2, h_min=-1, top_n=10000000,emojiCorpus='emojis.csv')
        time.sleep(2)


    """
    file:       待切词的文件 【绝对路径或文件名，若为文件名则默认存储路径为 .\\NLP\\Data】
    f_data_col: 提取数据的列序号 默认为None 【整数 从 0 开始】
    f_txt_sep:  txt 文件的切分字符  默认为None 【 csv 文件忽然此参数】
    f_encoding: 默认为utf8  utf8 | gbk
    n_gram:     提取的新词长度  默认为5。 即超过5个字符的新词不再处理
    batch_len:  批次计算的文本字符串长度 。【 字符串长度减少可降低占用内存，默认100000个字符就进入统计计算】
    top_n:      保存 top_n 个词组 参数设置越大，结果准确度越高，内存也增加, 在硬件配置允许的条件下应尽量调高 【默认 1000000】
    p_min:      词出现的最小概率 （p_min = 3 整数则为频数， p_min = 0.0001 浮点数则为概率）【默认 0.0001】
    co_min:     最小凝固度，只有超过最小凝固度才继续判断自由度并进入下一步搜索  【dytpe: int, default 100】
    h_min:      最大自由度，若小于最大自由度，则认为词组不完整，为大词组中的一小部分  【dytpe: int, default 1.2】
    level_s:    界面显示日志级别.  ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']  默认 INFO
    level_f:    日志文件记录级别.  ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']  默认 INFO
    log_path:   日志存储路径，默认为 None，默认存储到 .\\NLP\\log\\NLP_[当前时间].log
    process_no: 多进程处理的进程数，int 类型，默认为None 即 CPU 核数
    """