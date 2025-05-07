# 28.04.2025
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.family'] = 'Simhei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13

all_ = np.random.lognormal(size=10000)

def plot_dist(all_):
    sample_num = [1,5,10,30]
    print(all_.std()/np.sqrt(sample_num))
    fig,ax = plt.subplots(2,2)
    fig.set_size_inches(15,8)
    ax = ax.ravel()
    for index,num in enumerate(sample_num):
        mean_arr = np.zeros(1000)
        for i in range(len(mean_arr)):
            mean_arr[i]=np.random.choice(all_,size=num).mean()
        sns.histplot(mean_arr,ax=ax[index],kde=True,color='green',alpha=0.6)
        ax[index].set_title(f'样本容量: {num}，样本均值的均值:{mean_arr.mean():.2f},样本均值得标准差: {mean_arr.std():.2f}')
plt.show()

# plot_dist(all_)
# plt.show()

# iris = load_iris()
# data = np.concatenate([iris.data,iris.target.reshape(-1,1)],axis = 1)
# data = pd.DataFrame(data,columns=['sepal_length','sepal_width','petal_length','petal_width','type'])
# print(data.head(5))

# print(data.shape)
# (150, 5) - 150 rows 5 columns

# print(data['petal_length'].mean())


# scale = 50
# x=np.random.normal(0,scale,size=100000)
# for times in range(1,4):
#     y=x[(x>-times*scale)&(x<times*scale)]
#     print(f'{times}倍标准差')
#     print(f'{len(y)*100/len(x)}%')


mean=np.random.randint(-100000,100000)
std = 30
all2_ = np.random.normal(loc=mean,scale=std,size=10000)
sample = np.random.choice(all2_,size = 50)
sample_mean=sample.mean()
print('样本均值: ',sample_mean)
se=std/np.sqrt(50)
min_ = sample_mean-1.96*se
max_ = sample_mean+1.96*se
print(min_,max_)
plt.figure(figsize=(12,6))
plt.plot(mean,0,marker='*',color='orange',ms=15,label='总体均值')
plt.plot(sample_mean,0,marker='o',color='red',label='样本均值')
plt.hlines(0,xmin=min_,xmax=max_,color='g',label='置信区间')