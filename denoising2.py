import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt

data = pd.read_csv("secondary_data_repMissValNor_numOnly.csv", encoding='utf-8')
# 针对第二列数值（共三列）
data = data.values[:, 1]
index = list(range(1, 61070))
# Create wavelet object and define parameters
w = pywt.Wavelet('db8')  # 选用Daubechies8小波
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
print("maximum level is " + str(maxlev))
threshold = 0.06  # Threshold for filtering

# Decompose into wavelet components, to the level selected:
coeffs = pywt.wavedec(data, 'db8', level=maxlev)  # 将信号进行小波分解

plt.figure()
for i in range(1, len(coeffs)):
    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波

datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构

otpt_data = pd.DataFrame(datarec)
otpt_data.to_csv("pywtOtpt2.csv")

mintime = 0
maxtime = mintime + len(data) + 1

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel('mushroom number')
plt.ylabel('stem-height (cm)')
plt.title("Raw Data")
plt.subplot(2, 1, 2)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime-1])
plt.xlabel('mushroom number')
plt.ylabel('stem-height (cm)')
plt.title("De-noised signal using wavelet techniques")

plt.tight_layout()
plt.show()
