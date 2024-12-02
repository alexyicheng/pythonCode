import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Erstellen der Subplots (4x4 Grid für 16 Beispiele)
fig, axes = plt.subplots(4, 4, figsize=(20, 20))
axes = axes.ravel()  # 2D-Array der Achsen in eine Liste umwandeln

# Example 1: Add x- and y- axis
x = np.arange(0, 10)
axes[0].plot(x, x*x)
axes[0].set_title('Square of x^2')
axes[0].set_xlabel('X-axis')
axes[0].set_ylabel('Y-axis')

# Example 2: Add text
x = np.arange(-10, 11, 1)
y = x * x
axes[1].plot(x, y)
axes[1].set_title('Square of x^2')
axes[1].text(-2.5, 30, 'function y = x^2')

# Example 3: Add explanation (annotate)
axes[2].plot(x, y)
axes[2].set_title('Square of x^2')
axes[2].annotate('start', xy=(0, 0), xytext=(-4, 50),
                 arrowprops={'headwidth': 10, 'facecolor': 'black'})

# Example 4: Add legend
axes[3].plot(x, x, label='y=x')
axes[3].plot(x, x*2, label='y=2x')
axes[3].plot(x, x*3, label='y=3x')
axes[3].plot(x, x*4, label='y=4x')
axes[3].legend()
axes[3].set_title('Legend Example')

# Example 5: Change color
x = np.arange(1, 5)
axes[4].plot(x, color='g')
axes[4].plot(x+1, color='0.5')
axes[4].plot(x+2, color='gold')
axes[4].plot(x+3, color=(0.1, 0.2, 0.3))
axes[4].set_title('Color Example')

# Example 6: Marker
axes[5].plot(x, marker='o')
axes[5].plot(x+1, marker='>')
axes[5].plot(x+2, marker='s')
axes[5].set_title('Marker Example')

# Example 7: Mathematical formula
axes[6].set_title('Mathematical Formula')
axes[6].set_xlim([1, 8])
axes[6].set_ylim([1, 5])
axes[6].text(2, 4, r'$ \alpha \beta \pi \lambda \omega $', size=15)
axes[6].text(4, 4, r'$ \sin(0)=\cos(\frac{\pi}{2}) $', size=15)
axes[6].text(2, 2, r'$ lim_{x \rightarrow y} \frac{1}{x^3} $', size=15)
axes[6].text(4, 2, r'$ \sqrt{4}{x}=\sqrt{y} $', size=15)

# Example 8: Add grid
x = ['data_1', 'data_2', 'data_3', 'data_4']
y = [15, 30, 45, 10]
axes[7].grid(color='g', linewidth='1', linestyle='-.')
axes[7].plot(x, y)
axes[7].set_title('Grid Example')

# Example 9: Change axis locator-params
x = np.arange(0, 30, 1)
axes[8].plot(x, x)
axes[8].set_title('x-, y-axis Locator')
axes[8].locator_params('x', nbins=20)
axes[8].locator_params('y', nbins=20)

# Example 10: Axis limits
axes[9].plot(x, x*x)
axes[9].set_xlim([0, 40])
axes[9].set_ylim([0, 1000])
axes[9].set_title('Axis Limits')

# Example 11: Autoformat date
x = pd.date_range('2024/12/01', periods=30)
y = np.arange(0, 30, 1)
axes[10].plot(x, y)
axes[10].set_title('Autoformat Date')
fig.autofmt_xdate()

# Example 12: Add twinx
x = np.arange(1, 20)
y1 = x*x
y2 = np.log(x)
axes[11].plot(x, y1, label="y=x^2")
ax2 = axes[11].twinx()
ax2.plot(x, y2, 'r', label="y=log(x)")
axes[11].set_title('Twinx Example')

# Example 13: Fill/fill_between
x = np.linspace(0, 5*np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2*x)
axes[12].plot(x, y1)
axes[12].plot(x, y2)
axes[12].fill(x, y1, 'g', alpha=0.5)
axes[12].fill(x, y2, 'r', alpha=0.5)
axes[12].set_title('Fill/Fill-Between')

# Example 14: matplotlib.patches
xy1 = np.array([0.2, 0.2])
xy2 = np.array([0.2, 0.8])
xy3 = np.array([0.8, 0.2])
xy4 = np.array([0.8, 0.8])

axes[13].add_patch(mpatches.Circle(xy1, 0.15))
axes[13].add_patch(mpatches.Rectangle(xy2 - np.array([0.1, 0.05]), 0.2, 0.1, color='r'))
axes[13].add_patch(mpatches.RegularPolygon(xy3, numVertices=6, radius=0.1, color='g'))
axes[13].add_patch(mpatches.Ellipse(xy4, 0.4, 0.2, color='c'))
axes[13].axis('equal')
axes[13].set_title('Patches Example')

# Example 15: plt.style.use
axes[14].plot(x, x*x)
axes[14].set_title('Style Example')

# Entferne den 16. Plot, falls nicht benötigt
axes[-1].axis('off')

# Layout anpassen
plt.tight_layout()
plt.show()
