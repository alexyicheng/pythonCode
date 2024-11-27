# 22.11.2024

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as sfa

# read csv data
data = pd.read_csv('dpi_cpi.csv')
# print(data)

# print graphic
sns.lmplot(x = 'DPI', y = 'CPI', data = data, fit_reg = True)

# show
plt.show()

# create model
# ols -> y = a*x+b  = CPI = a*DPI + b
reg = sfa.ols('CPI~DPI',data = data)
fit = reg.fit()
# DPI increase 1 Dollar -> increase consumption 0.653478
# Intercept  what ever incraese or decrease -> has to consumption 1101.306338 minimum
print(fit.params)
