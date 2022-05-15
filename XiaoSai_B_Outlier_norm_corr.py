import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib
from scipy.stats import boxcox
mushroom=pd.read_csv('secondary_data_repVal_norm.csv')
# mushroom['stem-height']=mushroom['stem-height'].replace([0],mushroom['stem-height'].mean())
# mushroom['stem-width']=mushroom['stem-width'].replace([0],mushroom['stem-width'].mean())
# mushroom.to_csv('secondary_data_repVal.csv')

#class中，p有毒--1，e无毒--0
mushroom['class']=mushroom['class'].replace(['p','e'],[1,0])

#print(mushroom)
# 画偏态分布转正态分布转化前后图
# x=mushroom['stem-width']
# plt.subplot(1,2,1)
# plt.hist(x,bins=40)
# y, lambda0 = boxcox(x, lmbda=None, alpha=None)
# plt.subplot(1,2,2)
# plt.hist(y,bins=40)
# plt.suptitle("stem-width")
# plt.show()

# 替换数据
# mushroom['cap-diameter'], lambda0 = boxcox(mushroom['cap-diameter'], lmbda=None, alpha=None)
# mushroom['stem-height'], lambda0 = boxcox(mushroom['stem-height'], lmbda=None, alpha=None)
# mushroom['stem-width'], lambda0 = boxcox(mushroom['stem-width'], lmbda=None, alpha=None)
# print(mushroom)
# mushroom.to_csv('secondary_data_repVal_norm.csv')

# 点二列相关(point-biserial correlation)
mushroom = mushroom.sample(frac=0.1, axis=0)
print(mushroom['class'].value_counts())
cor_val=stats.pointbiserialr(mushroom['class'],mushroom['cap-diameter'])
print("class and cap-diameter:\n",cor_val)
cor_val=stats.pointbiserialr(mushroom['class'],mushroom['stem-height'])
print("class and stem-height:\n",cor_val)
cor_val=stats.pointbiserialr(mushroom['class'],mushroom['stem-width'])
print("class and stem-width:\n",cor_val)
