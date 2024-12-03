# 30.10.2024

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# instantiated unit
line = Line()

# define x axis
line.add_xaxis(['Germany','US','China'])

# define y axis
line.add_yaxis('GDP',[30,20,10])

# set title
line.set_global_opts(
    title_opts=TitleOpts(title='Showing GDP of countries', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# create render.html -> open the render.html in browser to show the graph
line.render()
