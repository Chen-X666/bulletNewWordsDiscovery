# _*_ coding: utf-8 _*_
"""
Time:     2021/10/27 0:20
Author:   ChenXin
Version:  V 0.1
File:     resultStatistic.py
Describe:  Github link: https://github.com/Chen-X666
"""
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def resultLine(data):
    sns.set()
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    sns.relplot(x="训练集数量(trainingNum)", linewidth=2,y="精准度(precision)", data=data, kind="line",dashes=False, markers=True,estimator= None).figure.set_size_inches(12,6)
    plt.yticks(np.arange(0.5,0.95,0.05))
    plt.xticks(np.arange(100,3100,100))
    plt.show()
if __name__ == '__main__':
    df = pd.read_csv('data/modelResult.csv',encoding='utf-8')
    print(df)
    # print(df['trainingNum'])
    # print(df['precision'])
    resultLine(df)
