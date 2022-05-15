import pandas as pd
from  scipy.stats import chi2_contingency

#cap-shape
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['cap-shape'])
kf = chi2_contingency(dfv)
print('cap-shape p-value = ', kf[1])
#cap-surface
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['cap-surface'])
kf = chi2_contingency(dfv)
print('cap-surface p-value = ', kf[1])
#cap-color
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['cap-color'])
kf = chi2_contingency(dfv)
print('cap-color p-value = ', kf[1])
#does-bruise-or-bleed
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['does-bruise-or-bleed'])
kf = chi2_contingency(dfv)
print('does-bruise-or-bleed p-value = ', kf[1])
#gill-attachment
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['gill-attachment'])
kf = chi2_contingency(dfv)
print('gill-attachment p-value = ', kf[1])
#gill-color
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['gill-color'])
kf = chi2_contingency(dfv)
print('gill-color p-value = ', kf[1])
#stem-color
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['stem-color'])
kf = chi2_contingency(dfv)
print('stem-color p-value = ', kf[1])
#has-ring
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['has-ring'])
kf = chi2_contingency(dfv)
print('has-ring p-value = ', kf[1])
#ring-type
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['ring-type'])
kf = chi2_contingency(dfv)
print('ring-type p-value = ', kf[1])
#habitat
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['habitat'])
kf = chi2_contingency(dfv)
print('habitat p-value = ', kf[1])
#season
data = pd.read_csv('secondary_data_replace_miss.csv')
data = data.sample(frac=0.1, axis=0)
dfv = pd.crosstab(data['class'], data['season'])
kf = chi2_contingency(dfv)
print('season p-value = ', kf[1])

