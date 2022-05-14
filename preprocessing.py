from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

data = pd.read_csv('secondary_data.csv', encoding='utf-8', index_col=0)
imputer = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
data['cap-surface'] = imputer.fit_transform(data['cap-surface'].values.reshape(-1,1))[:,0]
data['gill-attachment'] = imputer.fit_transform(data['gill-attachment'].values.reshape(-1,1))[:,0]
data['ring-type'] = imputer.fit_transform(data['ring-type'].values.reshape(-1,1))[:,0]
data.to_csv("secondary_data_replace_miss.csv")
