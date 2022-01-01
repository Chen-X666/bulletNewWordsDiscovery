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

import joblib
import pandas as pd
from NewWordDiscovery import initialCorpus

logger = logging.getLogger('NLP')
#  当前文件路径 的上层路径， 'NLP' 所在目录   'C:\Users\Chen\Desktop\NewWordDiscovery'
cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

def predictNewWord():
    randomForest = joblib.load(initialCorpus.getRamdomForestModel('RandomForest.model'))
    # 模型预测
    # 预测集数据预处理
    predict_data = pd.read_csv('预测集.csv',encoding='GBK')
    del predict_data['Word']
    del predict_data['Frequence']
    #predict_data = predict_data[predict_data['Mark'] >= 0]
    predict_data = predict_data.iloc[:, :-1]
    print("输入特征数据：{}".format(predict_data.T))
    print("模型预测结果：{}".format(randomForest.predict(predict_data)))
    predictData = randomForest.predict(predict_data)
    trainingData = pd.read_csv('预测集.csv', encoding='GBK')
    #trainingData = trainingData[trainingData['Mark'] >= 0]
    trainingData['Mark_Pre'] = predictData.tolist()
    trainingData.to_csv('预测集结果.csv',encoding='GBK')

if __name__ == '__main__':
    randomForest = predictNewWord()
