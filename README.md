使用的软件：Python, [KNIME](https://www.knime.com/)    
Python中需要安装的第三方库: pandas, matplotlib, numpy, seaborn, scipy, scikit-learn, PyWavelets  

**由于数据文件输入输出问题，建议将数据文件与代码文件放置在同一路径下**

1.	数据预处理  
将原数据文件中所有分号改为逗号，规范CSV文件格式  
[secondary_data.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data.csv)    

2.	缺失值处理：将缺失值超过40%的删除；再使用“最频繁”策略替代剩余变量的缺失值  
代码：[preprocessing.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/preprocessing.py)    
填补后的文件：[secondary_data_replace_miss.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data_replace_miss.csv)    

3.	异常值处理： stem-height, stem-width两列中所有0值用该列的平均值替代
4.	小波变换去噪：  
[secondary_data_repMissValNor_numOnly.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data_repMissValNor_numOnly.csv)    
[denoising1.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising1.py)    
[denoising2.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising2.py)    
[denoising3.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/denoising3.py)    
输出的数据文件：[secondary_data_repVal_denoising.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data_repVal_denoising.csv)  

5.	分析蘑菇各指标的基本特征:  
KNIME绘制直方图：[XiaoSai_B_histogram.zip](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_histogram.zip) （将该压缩包解压后放入KNIME工作目录即可）  
箱线图：[XiaoSai_B_boxplot.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_boxplot.py)    
百分比饼图：[XiaoSai_B_piechart.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_piechart.py)    

6.	分析有毒无毒与各指标的相关性：  
分类&分类：卡方检验 [chi-square.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/chi-square.py)    
分类&数值：对三个数值型变量正态转化，点二列相关（point-biserial correlation）  
[XiaoSai_B_Outlier_norm_corr.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_Outlier_norm_corr.py)  

7.	构建蘑菇有毒无毒的分类与识别模型  
独热编码：[XiaoSai_B_Onehot.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_Onehot.py)    
随机森林：  
[repVal_onehot.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/repVal_onehot.csv)  
[repVal_norm_onehot.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/repVal_norm_onehot.csv)  
[repVal_denoising_onehot.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/repVal_denoising_onehot.csv)  
[XiaoSai_B_RF.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_RF.py)  

8.	对相关因素的重要性进行排序：  
[XiaoSai_B_impor_sort.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_impor_sort.py)  
9.	模型灵敏度和可靠性分析  
[sens_tstsz.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/sens_tstsz.py)  
[sens_ntree.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/sens_ntree.py) 

1.	针对有毒蘑菇进一步进行分类，并分析对应类别下蘑菇的特征：   
箱线图&饼图：  
[secondary_data_repVal_p.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data_repVal_p.csv)  
[secondary_data_repVal_e.csv](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/secondary_data_repVal_e.csv)  
[XiaoSai_B_T5.py](https://github.com/charlieandthor/16th-mathematical-modeling-contest/blob/main/XiaoSai_B_T5.py)
 

