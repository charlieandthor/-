import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
mushroom=pd.read_csv('secondary_data_replace_miss.csv')
# lbs=mushroom['cap-color'].value_counts().index
# print(len(lbs))
def tizi_size(p_text,l_text):#定义调整字体大小的函数
    for t in p_text:
        t.set_size(6) #调整饼图内文字大小
    for t in l_text:
        t.set_size(12) #调整饼图对应的文字大小
#所有饼图画一起
# def draw(data,color=None):
#     lbs=data.value_counts().index
#     if color:
#         patches,l_text,p_text=plt.pie(data.value_counts(normalize=True),
#                 labels=lbs, colors=sns.color_palette(color,len(lbs)),
#                 autopct='%.2f%%', radius=1, startangle=120)  # 统计数据项的种类，并计算百分比
#         tizi_size(p_text,l_text)
# #matplotlib.rcParams['font.sans.serif']=['SimHei']
# plt.figure(num=1,figsize=(24,18)) #指定子图片大小12*9
# ax=plt.subplot(3,4,1) #画子图
# draw(data=mushroom['cap-shape'],color='Purples')
# ax.set_title('cap-shape')
# ax=plt.subplot(3,4,2) #画子图
# draw(data=mushroom['cap-surface'],color='Blues')
# ax.set_title('cap-surface')
# ax=plt.subplot(3,4,3) #画子图
# draw(data=mushroom['cap-color'],color='Reds')
# ax.set_title('cap-color')
# ax=plt.subplot(3,4,4) #画子图
# draw(data=mushroom['does-bruise-or-bleed'],color='Oranges')
# ax.set_title('does-bruise-or-bleed')
# ax=plt.subplot(3,4,5) #画子图
# draw(data=mushroom['gill-attachment'],color='Greens')
# ax.set_title('gill-attachment')
# ax=plt.subplot(3,4,6) #画子图
# draw(data=mushroom['gill-color'],color='Purples')
# ax.set_title('gill-color')
# ax=plt.subplot(3,4,7) #画子图
# draw(data=mushroom['stem-color'],color='Blues')
# ax.set_title('stem-color')
# ax=plt.subplot(3,4,8) #画子图
# draw(data=mushroom['has-ring'],color='Reds')
# ax.set_title('has-ring')
# ax=plt.subplot(3,4,9) #画子图
# draw(data=mushroom['ring-type'],color='Greens')
# ax.set_title('ring-type')
# ax=plt.subplot(3,4,10) #画子图
# draw(data=mushroom['habitat'],color='Oranges')
# ax.set_title('habitat')
# ax=plt.subplot(3,4,11) #画子图
# draw(data=mushroom['season'],color='Blues')
# ax.set_title('season')

#画单张饼图
plt.figure(figsize=(6,6))
lbs=mushroom['season'].value_counts().index
patches,l_text,p_text=plt.pie(mushroom['season'].value_counts(normalize=True),
                labels=lbs, colors=sns.color_palette('Greens',len(lbs)),
                autopct='%1.1f%%', radius=1.0, startangle=120,pctdistance=0.9,
                )  # 统计数据项的种类，并计算百分比
tizi_size(p_text,l_text)
plt.title('season')
#plt.savefig('piechart.png')
plt.show()