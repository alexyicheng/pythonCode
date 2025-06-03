
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(16,8))
plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False

z = np.linspace(-10,10,200)
y = 1/(1+np.exp(-z))
plt.plot(z,y,label='Sigmoid Function',linewidth=2)

plt.axvline(x=0,ls='--',c='black')
plt.axhline(y=1,ls=':',c='black')
plt.axhline(y=0,ls=':',c='black')
plt.axhline(y=0.5,ls=':',c='black')
plt.xlabel('z')
plt.ylabel('sigmoid(z)')
plt.title('Sigmoid function')
plt.show()