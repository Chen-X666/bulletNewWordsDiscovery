# _*_ coding: utf-8 _*_
"""
Time:     2022/1/1 17:52
Author:   ChenXin
Version:  V 0.1
File:     PredictNewWord.py
Describe:  Github link: https://github.com/Chen-X666
"""
import logging
import os
import time

import joblib
import pandas as pd
from NewWordDiscovery.tool import initialingCorpus

logger = logging.getLogger('NLP')
#  当前文件路径 的上层路径， 'NLP' 所在目录   'C:\Users\Chen\Desktop\NewWordDiscovery'
cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

class Arguments:
    #  当前文件路径 的上层路径
    CWD = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

    # 调用当前文件时的系统日期时间
    Call_Time = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 初始化时间， 导入此文件时间，实例化时不变

    def __init__(self):
        self.start_time = time.time()  # 实例化时间

    # 打印当前存储类中的所有参数 取值
    def __repr__(self):
        arg_values = '\n'.join(['     {}: {}'.format(x, self.__getattribute__(x)) for x in dir(self) if x[0] != '_'])
        return 'Arguments Values:  \n{}'.format(arg_values)

#输出新词
def toNewWordCsv(newWords,file_name):
    csv_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')), 'NewWordResult',
                            'NewWordResult_%s.csv' % (file_name))
    with open(csv_path, 'a',encoding='utf-8') as f_csv:
        for i in newWords:
            print(i, file=f_csv)
    logger.info("NewWordResult path:  {}  ".format(csv_path))

def predictNewWord(args):
    randomForest = joblib.load(initialingCorpus.getRamdomForestModel('RandomForest.model'))
    # 模型预测
    # 预测集数据预处理
    csv_path = os.path.join(args.CWD, 'CandidateWordResult',
                            'CandidateWordResult_%s.csv' % (args.file_name))
    predict_data = pd.read_csv(csv_path,encoding='gbk')
    if not predict_data.empty:
        del predict_data['Word']
        del predict_data['Frequence']
        #del predict_data['edgeAdavanced']
        #predict_data = predict_data[predict_data['Mark'] >= 0]
        predict_data = predict_data.iloc[:, :-1]
        print(predict_data)
        print("输入特征数据：{}".format(predict_data.T))
        print("模型预测结果：{}".format(randomForest.predict(predict_data)))
        predictData = randomForest.predict(predict_data)
        outputData = pd.read_csv(csv_path, encoding='gbk')
        #trainingData = trainingData[trainingData['Mark'] >= 0]
        outputData['Mark_Pre'] = predictData.tolist()
        outputData = outputData[outputData['Mark_Pre'] < 1]
        newWords = outputData['Word'].tolist()
        toNewWordCsv(newWords=newWords,file_name=args.file_name)

if __name__ == '__main__':
    args = Arguments()
    args.file_name = 'BV1Gb411P7wK.csv'
    randomForest = predictNewWord(args)
