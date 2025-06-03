# 07.05.2025

from scipy import stats
import numpy as np

# a = np.array([0.497,0.506,0.518,0.524,0.498,0.511,0.520,0.515,0.512])
#
# sample_mean=a.mean()
# std=0.015
# n=len(a)
# se = std/np.sqrt(n)
# min_=sample_mean-1.96*se
# max_=sample_mean+1.96*se
# print(f'interval:[{min_:.3f},{max_:.3f}]')

u = u0 = 0.5
a = np.array([0.497,0.506,0.518,0.524,0.498,0.511,0.520,0.515,0.512])
std = 0.015
sample_mean = a.mean()
n=len(a)
mean = 0.5
se = std/np.sqrt(n)
Z=(sample_mean-mean)/se
# print(Z)
P=2*stats.norm.sf(abs(Z))
print(P)

P2 = stats.norm.sf(abs(Z))
print(P2)

P3 = stats.norm.cdf(Z)
print(P3)