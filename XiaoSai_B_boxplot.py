import pandas as pd
import matplotlib.pyplot as plt
#画数值型数据的箱线图，找出异常值
mushroom=pd.read_csv('secondary_data_replace_miss.csv')
# box_1, box_2, box_3 = mushroom['cap-diameter'], mushroom['stem-height'], mushroom['stem-width']
# plt.figure(figsize=(10, 5))  # 设置画布的尺寸
# plt.title('Boxplot', fontsize=20)  # 标题，并设定字号大小
# labels = 'cap-diameter', 'stem-height', 'stem-width' # 图例
# plt.boxplot([box_1, box_2, box_3], labels=labels)  # grid=False：代表不显示背景中的网格线
mushroom.boxplot(column=['cap-diameter','stem-height','stem-width'])#画箱型图的另一种方法，参数较少，而且只接受dataframe，不常用
plt.show()  # 显示图像
