# 30.11.2024

import matplotlib.pyplot as plt
import numpy as np

# # normalized horizontally stacked columns
# # Data and Labels
# label = ['dataset_1','dataset_2','dataset_3','dataset_4','dataset_5']
# sublabel = ['data_1','data_2','data_3','data_4']
# value = np.array([
#     [60,100,30,70],
#     [80,120,40,50],
#     [90,110,60,38],
#     [70,130,50,40],
#     [50,140,20,60]
# ])
# color = ['#1f77b4','red','darkgreen','orange']
#
# # create plot
# fig,ax = plt.subplots(figsize=(6,6))
# plt.subplots_adjust(left=0.15,right=0.83)
# ax.set_title('Normalized horizontal stack columns')
#
# # Normalization
# value_normalized = value/value.sum(axis=1,keepdims=True)
#
# # Normalized horizontal stack columns
# bottom = np.zeros(value_normalized.shape[0])
# for i in range(len(sublabel)):
#     ax.barh(label, value_normalized[:, i],left=bottom,color=color[i],label=sublabel[i])
#     bottom += value_normalized[:, i]
#
# # Axis and Name
# ax.set_xlabel('Proportional')
# ax.set_ylabel('data_sets')

# legends
# ax.legend(bbox_to_anchor=(1,1))
# plt.show()


# histogram
# fig,ax = plt.subplots(figsize = (6,6))
# ax.set_title('Histogram')
# label = ['data_1','data_2','data_3','data_4']
# value = [60,100,30,70]
# color = ['blue','yellow','red','green']
# ax.bar(label,value,label=label,color=color)
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.legend()
# plt.show()


# combined histogram

# label = ['dataset_1','dataset_2']
# sublabel = ['data_1','data_2','data_3']
# value = np.array([
#     [60,100,30,70],
#     [80,120,40,50]
# ])
# color = ['darkblue','darkred','darkgreen']
#
# fix,ax = plt.subplots(figsize=(6,6))
# ax.set_title('combined histogram')
# width = 0.3 # width of pillar
#
# x = np.arange(len(label)) # position for the main labels
# for i in range(len(sublabel)):
#     ax.bar(x + i * width, value[:,i],width=width,color=color[i],label=sublabel[i])
#
# ax.set_xlabel('x axes')
# ax.set_ylabel('y axes')
# # ax.set_xticks(x + width,label) # centers of group
# ax.set_xticks(x + width * (len(sublabel) - 1) / 2)  # Zentriert die Gruppen
# ax.legend()
# plt.show()

# box diagram

# np.random.seed(10)
# data = [np.random.normal(loc,10,100) for loc in [60,100,30,70]]
#
# fig, ax = plt.subplots(figsize=(6,6))
# ax.set_title('Box diagram')
# labels = ['data_1','data_2','data_3','data_4']
# colors = ['darkblue','darkred','gold','darkgreen']
#
# box = ax.boxplot(data,patch_artist=True,label=labels)
#
# for patch,color in zip(box['boxes'],colors):
#     patch.set_facecolor(color)
#
# ax.set_xlabel('x axes')
# ax.set_ylabel('y axes')
#
# # X-Ticks und set up Labels
# ax.set_xticks(range(1, len(labels) + 1))  # Positionen der Boxen
# ax.set_xticklabels(labels)  # Labels an diesen Positionen
#
# plt.show()

# stacked bar chart

# label = ['dataSet_1','dataSet_2','dataSet_3']
# sublabel = ['data_1','data_2','data_3','data_4']
# value = np.array([
#     [60,100,30,70],
#     [80,120,40,50],
#     [80,120,40,50]
# ])
# color = ['darkblue','darkred','gold','darkgreen']
# x = np.arange(len(label))
#
# fig, ax = plt.subplots(figsize=(6,6))
# ax.set_title('Stacked Box Chart')
#
# bottom_values = np.zeros(len(label))
# for i in range(len(sublabel)):
#     ax.bar(x, value[:, i], width=0.7, color=color[i],
#     label=sublabel[i], bottom=bottom_values    )
#     bottom_values += value[:, i]  # Aktualisiere die Basis für den nächsten Stapel
#
# ax.set_xlabel('x axes')
# ax.set_ylabel('y axes')
# ax.set_xticks(x)
# ax.set_xticklabels(label)
# ax.legend(bbox_to_anchor=(1,1))
# plt.show()

# # horizontal bar chart
# label = ['data_1','data_2','data_3','data_4']
# value = [60,100,30,70]
# color = ['darkblue','darkred','gold','darkgreen']
#
# fig,ax = plt.subplots(figsize=(6,6))
# ax.set_title('honrizontal bar chart')
# ax.barh(label,value,color=color)
#
# ax.set_xlabel('x axes')
# ax.set_ylabel('y axes')
#
# plt.show()

# waterfall diagram

# label = ['sum','data_1','data_2','data_3','data_4','data_5']
# value = np.array([2900,-1200,-300,-900,-300])
#
# fig,ax = plt.subplots(figsize=(6,6))
# ax.set_title('Waterfall diagram')
# color = ['darkblue','darkred','gold','darkgreen','yellow','lightcoral']

# calculate comulate summe
# comulative = np.cumsum(value)
# step = np.insert(comulative[:-1],0,0)
#
# # draw bar chart
# for i in range(len(value)):
#     ax.bar(label[i],value[i],bottom=step[i],color=color[i])
#     ax.text(label[i],step[i]+value[i]/2, str(abs(value[i])),
#             ha='center',va='center',color='white',fontsize=12)
# ax.set_xlabel('x axes')
# ax.set_ylabel('y axes')
#
# plt.show()

# postiv and negativ histogram
label = ['class_1','class_2','class_3','class_4','class_5']
value = np.array([20,-10,30,-25,15])
color = ['gold' if v>= 0 else 'darkblue' for v in value]

fig,ax = plt.subplots(figsize=(6,6))
ax.set_title('positv and negativ histogram')

ax.barh(label,value,color=color,edgecolor='black')

ax.set_xlabel('x axes')
ax.set_ylabel('y axes')

plt.show()