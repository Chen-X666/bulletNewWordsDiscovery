# _*_ coding: utf-8 _*_
"""
Time:     2021/11/8 23:14
Author:   ChenXin
Version:  V 0.1
File:     paraChose.py
Describe:  Github link: https://github.com/Chen-X666
"""
import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
if __name__ == '__main__':
    # Mark = []
    # trainingData = pd.read_csv('data/标注集.csv',encoding='GBK')['Word'].to_list()
    # df = pd.read_csv('data/oneVideo.csv',encoding='GBK')['词组'].to_list()
    # for i in df:
    #     if i in trainingData:
    #         Mark.append(1)
    #     else:
    #         Mark.append(0)
    # df = pd.read_csv('data/oneVideo.csv', encoding='GBK')
    #
    # df['Mark'] = Mark
    # df.to_csv('1.csv',encoding='GBK')
    # print('1')
    data = pd.read_csv('data/1.csv',encoding='GBK')
    #data = data[data['Mark'] >= 0]
    #data = data[data['TF-IDF'] <= 0.0006]
    #data = data[data['TF'] <= 0.00015]
    #data = data[data['IDF'] <= 0.00015]
    sns.set(font_scale = 3)
    flatui = ["#3498db","#e74c3c"]
    sns.set_color_codes()
    data = data.sample(frac=1).reset_index(drop=True).sort_values(by=['Mark'],na_position='first')
    data['候选词序号(NO.)'] = data.index
    print(data)
    #data = data[data['Mark'] > 0]
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    #sns.relplot(x='新词序号(NO.)', y='信息熵(Ent)', data=data,dashes=False,markers=True,estimator= None,hue= 'Mark',style='Mark',palette="ch:r=-.2,l=.75",alpha = 0.8).figure.set_size_inches(12,6)

    #sns.relplot(x='候选词序号(NO.)', y='N', data=data, dashes=False, markers=True, estimator=None,
    #           palette="ch:r=-.2,l=.75").figure.set_size_inches(7, 6)
    #sns.relplot(x='候选词序号(NO.)', y='互信息(Mut)', data=data, dashes=False, markers=True, estimator=None,hue='Mark',style='Mark',alpha = 0.8,
    #              palette="ch:r=-.2,l=.75",s=150).figure.set_size_inches(25, 18)
    sns.relplot(x='候选词序号(NO.)', y='最小左右信息熵{min(Ent_L, Ent_R)}', data=data, dashes=False, markers=True, estimator=None,hue='Mark',style='Mark',alpha = 0.8,
              palette="ch:r=-.2,l=.75",s=150).figure.set_size_inches(25, 18)

    # #sns.stripplot(x="Mark", y="Mut", data=data,jitter=True)
    plt.yticks([0,1,1.2,2,3,4,5,6])
    #plt.yticks([0, 2, 4, 6, 8, 10, 12])
    plt.show()

