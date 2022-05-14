使用的软件：Python,KNIME[（官网下载地址）](https://www.knime.com/)
Python中需要安装的第三方库: pandas, matplotlib, numpy, seaborn, 
**由于数据文件输入输出问题，建议将数据文件与代码文件放置在同一路径下**

1.	数据预处理
将原数据文件中所有分号改为逗号，规范CSV文件格式
secondary_data.csv

2.	缺失值处理：将缺失值超过40%的删除；再使用“最频繁”策略替代剩余变量的缺失值
代码：preprocessing.py
填补后的文件：secondary_data_replace_miss.csv

3.	小波变换去噪：
secondary_data_replace_miss_numOnly.csv
[denoising1.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising1.py)
[denoising2.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising2.py)
[denoising3.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising2.py)
输出的数据文件：secondary_data_replaceMiss_denoising.csv

4.	分析蘑菇各指标的基本特征:
KNIME绘制直方图：XiaoSai_B_histogram.zip （将该压缩包解压后放入KNIME工作目录即可）
箱线图：XiaoSai_B_boxplot.py
百分比饼图：XiaoSai_B_piechart.py

