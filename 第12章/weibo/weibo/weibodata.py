# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif']=['SimHei'] #pyplot中文显示
def Main():
    #使用pandas读取数据文件，创建DataFrame对象，并删除其中所有缺失值；
    df = pd.read_excel('./weibo.xlsx', encoding='cp936')
    df = df.dropna()  # 读取数据，丢弃缺失值
    # 生成天点赞数折线图
    plt.figure()
    df.plot(x='datetime')
    plt.savefig('E:/Linda/python37/weibo/hot.jpg')
if __name__=="__main__":
    Main()
