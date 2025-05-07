# 07.05.2025

import numpy as np
a = np.array([0.497,0.506,0.518,0.524,0.498,0.511,0.520,0.515,0.512])

sample_mean=a.mean()
std=0.015
n=len(a)
se = std/np.sqrt(n)
min_=sample_mean-1.96*se
max_=sample_mean+1.96*se
print(f'interval:[{min_:.3f},{max_:.3f}]')