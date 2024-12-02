# 01.12.2024

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# example 1 add x- and y- axis
# x = np.arange(0,10)
# plt.title('Square of x Power to 2')
# plt.plot(x,x*x)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# example 2 add text
# x=np.arange(-10,11,1)
# y=x*x
# plt.plot(x,y)
# plt.title('Square of x power to 2')
# plt.text(-2.5,30,'function y = x^2')
# plt.show()

# example 3 add explanation
# x=np.arange(-10,11,1)
# y=x*x
# plt.plot(x,y)
# plt.title('Square of x power to 2')
# plt.annotate('start', xy=(0, 0), xytext=(-4, 50),
#              arrowprops={'headwidth': 10, 'facecolor': 'black'})
# plt.show()

# example 4 add legend
# plt.plot(x,x)
# plt.plot(x,x*2)
# plt.plot(x,x*3)
# plt.plot(x,x*4)
# plt.legend(['blue','light','weigt','baby'])
# plt.show()

# example 5 change color
# x = np.arange(1,5)
# plt.plot(x,color='g')
# plt.plot(x+1,color='0.5')
# plt.plot(x+2,color='gold')
# plt.plot(x+3,color=(0.1,0.2,0.3))
# plt.show()

# example 6 marker
# x = np.arange(1,5)
# plt.plot(x,marker='o')
# plt.plot(x+1,marker='>')
# plt.plot(x+2,marker='s')
# plt.show()

# example 7 add mathematical formula
# plt.title('mathematical formula')
# plt.xlim([1,8])
# plt.ylim([1,5])
# plt.text(2,4,r'$ \alpha \beta \pi \lambda \omega $',size=25)
# plt.text(4,4,r'$ \sin(0)=\cos(\frac{\pi}{2}) $',size=25)
# plt.text(2,2,r'$ lim_{x \rightarrow y} \frac{1}{x^3} $',size=25)
# plt.text(4,2,r'$ \sqrt{4}{x}=\sqrt{y} $',size=25)
# plt.show()

# example 8 add grid
# x = 'data_1','data_2','data_3','data_4'
# y = [15,30,45,10]
# plt.grid(color='g',linewidth='1',linestyle='-.')
# plt.plot(x,y)
# plt.show()

# example 9 change axis locator-params
# x = np.arange(0,30,1)
# plt.plot(x,x)
# plt.title('x-,y-axis 2 steps pro unit')
# plt.locator_params('x',nbins=20)
# plt.locator_params('y',nbins=20)
# plt.show()

# example 10 axis->xlim/ylim
# x = np.arange(0,30,1)
# plt.plot(x,x*x)
# plt.xlim(xmin=0,xmax=40)
# plt.ylim(ymin=0,ymax=1000)
# plt.show()

# example 11 autofmt_xdate
# x=pd.date_range('2024/12/01',periods=30)
# y=np.arange(0,30,1)
# plt.plot(x,y)
# plt.gcf().autofmt_xdate()
# plt.show()

# example 12 add twinx
# x = np.arange(1,20)
# y1=x*x
# y2=np.log(x)
# plt.plot(x,y1)
# plt.twinx()
# plt.plot(x,y2,'r')
# plt.show()

# example 14 fill/fill_between
# x=np.linspace(0,5*np.pi,1000)
# y1=np.sin(x)
# y2=np.sin(2*x)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.fill(x,y1,'g')
# plt.fill(x,y2,'r')
#
# plt.title('Fill/Fill-Between')
# plt.show()

# example 15 matloitlib.patche
xy1=np.array([0.2,0.2])
xy2=np.array([0.2,0.8])
xy3=np.array([0.8,0.2])
xy4=np.array([0.8,0.8])

fig,ax = plt.subplots()

circle = mpatches.Circle(xy1,0.15)
ax.add_patch(circle)

rect = mpatches.Rectangle(xy2 - np.array([0.1, 0.05]), 0.2, 0.1, color='r')
ax.add_patch(rect)

# Add a regular polygon (e.g., triangle)
polygon = mpatches.RegularPolygon(xy3, numVertices=6, radius=0.1, color='g')
ax.add_patch(polygon)

ellipse = mpatches.Ellipse(xy4,0.4,0.2,color='c')
ax.add_patch(ellipse)

ax.axis('equal')
plt.show()

# example 16 plt.style.use
# print(plt.style.use('seaborn-whitegrid'))
# print(plt.style.available)