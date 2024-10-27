# 26.10.2024

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



data = pd.read_excel(r'C:\Users\AY\Desktop\pythonCode\exceldata\301101_forecast.xlsx')


date = data['时间'].dt.strftime('%Y-%W')
actual_values = data.groupby(date)['真实值'].sum()
predict_values = data.groupby(date)['预测值'].sum()


# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# use matplotlib.pyplot
# ax.barh(predict_values.index,predict_values.iloc[::-1], color='cyan', label='predicted_values', align='center')
# ax.barh(actual_values.index,-actual_values.iloc[::-1], color='purple', label='actual_values', align='center')
#
# # Label customization
# ax.set_xlabel('value')
# ax.set_title('comparing actual again predicted values', fontsize=15, color='red')
# ax.set_xticks(np.arange(-300, 301, 50))
# ax.set_xticklabels([abs(x) for x in np.arange(-300, 301, 50)])  # To show positive labels
#
# # Adding a legend
# ax.legend(loc='lower right')
#
# # Display the plot
# plt.tight_layout()
# plt.show()

sns.barplot(
    x=predict_values.iloc[::-1],
    y=predict_values.index[::-1],
    color='cyan',
    label='Predicted Values',
    ax=ax,
    orient='h'
)
sns.barplot(
    x=-actual_values.iloc[::-1],
    y=actual_values.index[::-1],
    color='purple',
    label='Actual Values',
    ax=ax,
    orient='h'
)

# Label customization
ax.set_xlabel('Value')
ax.set_title('Comparing Actual Against Predicted Values', fontsize=15, color='red')
ax.set_xticks(np.arange(-300, 301, 50))
ax.set_xticklabels([abs(x) for x in np.arange(-300, 301, 50)])  # To show positive labels

# Adding a legend
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()