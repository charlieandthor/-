import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
mushroom_p=pd.read_csv('secondary_data_repVal_p.csv')
mushroom_e=pd.read_csv('secondary_data_repVal_e.csv')

def tizi_size(p_text,l_text):#定义调整字体大小的函数
    for t in p_text:
        t.set_size(6) #调整饼图内文字大小
    for t in l_text:
        t.set_size(9) #调整饼图对应的文字大小
plt.figure(num=1,figsize=(24,18))
ax=plt.subplot(1,2,1)
lbs=mushroom_p['ring-type'].value_counts().index
patches,l_text,p_text=plt.pie(mushroom_p['ring-type'].value_counts(normalize=True),
                labels=lbs, colors=sns.color_palette('Oranges',len(lbs)),
                autopct='%1.1f%%', radius=1.0, startangle=120,pctdistance=0.9,
                explode=(0,0,0,0,0.1,0.2,0.3)
                )  # 统计数据项的种类，并计算百分比
tizi_size(p_text,l_text)
ax.set_title('poisonous')
ax=plt.subplot(1,2,2)
lbs=mushroom_e['ring-type'].value_counts().index
patches,l_text,p_text=plt.pie(mushroom_e['ring-type'].value_counts(normalize=True),
                labels=lbs, colors=sns.color_palette('Oranges',len(lbs)),
                autopct='%1.1f%%', radius=1.0, startangle=120,pctdistance=0.9,
                explode=(0,0,0,0,0.1,0.2,0.3)
                )  # 统计数据项的种类，并计算百分比
tizi_size(p_text,l_text)
ax.set_title('edibile')
plt.suptitle('ring-type')
#plt.savefig('piechart.png')
plt.show()

mushroom=[mushroom_p['cap-diameter'],mushroom_e['cap-diameter']]
#print(mushroom)
# mushroom=pd.read_csv('secondary_data_replace_miss.csv')
# box_1, box_2, box_3 = mushroom['cap-diameter'], mushroom['stem-height'], mushroom['stem-width']
# plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('cap-diameter', fontsize=20)  # 标题，并设定字号大小
labels = 'poisonous', 'edibile' # 图例
plt.boxplot(mushroom, labels=labels)  # grid=False：代表不显示背景中的网格线
#mushroom.boxplot()#画箱型图的另一种方法，参数较少，而且只接受dataframe，不常用
plt.show()  # 显示图像
