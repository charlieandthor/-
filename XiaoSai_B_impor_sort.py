# 导入相关库和包
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.feature_selection import SelectFromModel

# 装载数据
# 只处理缺失值和异常值数据
# data=pd.read_csv('secondary_data_repMiss_repNum.csv')
#正态后但未去噪
# data=pd.read_csv('secondary_data_repMiss_repNum_norm.csv')
# #去噪后数据
# data=pd.read_csv('secondary_data_repMiss_repNum_denoising.csv')

#data=pd.read_csv('repVal_onehot.csv')
#data=pd.read_csv('repVal_norm_onehot.csv')
data=pd.read_csv('repVal_denoising_onehot.csv')

features = data.drop(columns=['class'])
target = data['class']
# 创建随机森林模型并计算特征重要度
randomforest = RandomForestClassifier(random_state=0, n_jobs=-1)
model = randomforest.fit(features, target)
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
names = [model.feature_names_in_[i] for i in indices]
#print(names)
#print(range(features.shape[1]), importances[indices])
# 画图
plt.figure(figsize=(12,12))
from matplotlib.font_manager import FontProperties
#设置支持中文字体
fp= FontProperties(fname="c:/windows/fonts/simsun.ttc", size=25)
plt.suptitle('特征重要性',fontproperties=fp)
plt.bar(range(features.shape[1]), importances[indices])
plt.xticks(range(features.shape[1]), names, rotation=90,fontsize=5)
#plt.savefig('impor_sort.png')
plt.show()
# 通过重要度的阈值筛选特征
# 定义重要度的阈值
selector = SelectFromModel(randomforest, threshold=0.3)
features_important = selector.fit_transform(features, target)
# 训练新的模型
#model = randomforest.fit(features_important, target)
