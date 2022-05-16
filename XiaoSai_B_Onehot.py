#对17个名义变量进行one-hot编码
import pandas as pd
#data=pd.read_csv('secondary_data_repVal.csv')
#data=pd.read_csv('secondary_data_repVal_norm.csv')
data=pd.read_csv('secondary_data_repVal_denoising.csv')
print(data.head())
#class中，p有毒--1，e无毒--0
data['class']=data['class'].replace(['p','e'],[1,0])

a=pd.get_dummies(data['cap-shape'],prefix="cap-shape")
b=pd.get_dummies(data['cap-surface'],prefix="cap-surface")
c=pd.get_dummies(data['cap-color'],prefix="cap-color")
d=pd.get_dummies(data['gill-attachment'],prefix="gill-attachment")
e=pd.get_dummies(data['gill-color'],prefix="gill-color")
f=pd.get_dummies(data['stem-color'],prefix="stem-color")
g=pd.get_dummies(data['has-ring'],prefix="has-ring")
h=pd.get_dummies(data['ring-type'],prefix="ring-type")
i=pd.get_dummies(data['habitat'],prefix="habitat")
j=pd.get_dummies(data['season'],prefix="season")

frames=[data['class'],data['cap-diameter'],
        a,b,c,d,e,data['stem-height'],data['stem-width'],f,g,h,i,j]
ohc=pd.concat(frames,axis=1)
print(ohc)
#ohc.to_csv('repVal_onehot.csv')
#ohc.to_csv('repVal_norm_onehot.csv')
#ohc.to_csv('repVal_denoising_onehot.csv')
