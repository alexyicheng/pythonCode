import numpy as np
import pandas as pd

sample_mean = 45
std = 15
n = 30

se = std/np.sqrt(n)

min_ = sample_mean-1.96*se
max_ = sample_mean+1.96*se
print(min_,max_)
