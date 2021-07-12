# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
def Main():
    # 读取baidu.csv文件的title和reply列
    csv_data = pd.read_csv("../baidu.csv", usecols=['title', 'reply'])
    df = DataFrame(csv_data )
    #设置柱状图
    df.plot(kind='bar')
    #设置标题
    plt.title('reply')
    plt.show()
if __name__=="__main__":
    Main()
