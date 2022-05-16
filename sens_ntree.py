import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, precision_score, accuracy_score,f1_score
import matplotlib.pyplot as plt
# dataset: 去噪后数据
data=pd.read_csv('repVal_denoising_onehot.csv')

X=data.drop(columns=['class'])
Y=data['class']

l_numTree = list(range(50, 251, 20))
A = []
P = []
R = []
f1 = []
X_train,X_val,y_train,y_val=train_test_split(X,Y,test_size=0.2)

for i in range(11):
    n_trees = l_numTree[i]
    clf = RandomForestClassifier(n_estimators=n_trees)
    clf.fit(X_train, y_train)
    pred=clf.predict(X_val)
    # Evaluate model
    A.append(accuracy_score(y_val, pred))
    P.append(precision_score(y_val, pred, average='micro'))
    R.append(recall_score(y_val, pred, average='micro'))
    f1.append(f1_score(y_val,pred))

plt.subplot(2, 2, 1)
plt.plot(l_numTree, A, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='accuracy score')
plt.legend(loc="upper right")
plt.xlabel('test size')
plt.ylabel('accuracy score')
plt.subplot(2, 2, 2)
plt.plot(l_numTree, P, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='precision score')
plt.legend(loc="upper right")
plt.xlabel('test size')
plt.ylabel('precision score')
plt.subplot(2, 2, 3)
plt.plot(l_numTree, R, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='recall score')
plt.legend(loc="upper right")
plt.xlabel('test size')
plt.ylabel('recall score')
plt.subplot(2, 2, 4)
plt.plot(l_numTree, f1, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='f1 score')
plt.legend(loc="upper right")
plt.xlabel('test size')
plt.ylabel('f1 score')
plt.tight_layout()
plt.show()
