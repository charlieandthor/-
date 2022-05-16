import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from PlotRandomForestTrees import plot_RF_trees
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import recall_score, precision_score, accuracy_score,f1_score

# dataset
# 只处理缺失值和异常值数据
# data=pd.read_csv('repVal_onehot.csv')
#正态后但未去噪
# data=pd.read_csv('repVal_norm_onehot.csv')
#去噪后数据
data=pd.read_csv('repVal_denoising_onehot.csv')

X=data.drop(columns=['class'])
Y=data['class']
X_train,X_val,y_train,y_val=train_test_split(X,Y,test_size=0.2)

n_trees = 100
clf = RandomForestClassifier(n_estimators=n_trees)
clf.fit(X_train, y_train)
pred=clf.predict(X_val)
# Evaluate model
print("Accuracy: ", accuracy_score(y_val, pred))
print("Precision: ", precision_score(y_val, pred, average='micro'))
print("Recall: ", recall_score(y_val, pred, average='micro'))
print("f1 score: ",f1_score(y_val,pred))
