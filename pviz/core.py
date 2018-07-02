# Import essential numerical libaries
import math
import numpy as np
import pandas as pd

# Import essential bokeh plotting tools
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import HoverTool, CustomJS, ColumnDataSource,Slider
from bokeh.models import Arrow, NormalHead
from bokeh.layouts import column,layout,row
from bokeh.models.formatters import DatetimeTickFormatter
class base():
    """
    Base figure class
    """
    def __init__(self,source,**kwargs):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset"]
        self.p = figure(logo=None,tools=tools,**kwargs)
        #self.p.xgrid.grid_line_color=None
        #self.p.ygrid.grid_line_color=None
        self.source=source
    
    def save(self,name="space.html",pshow=True):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

class space(base):
    """
    Figure class that plot state variables against one another
    """
    def __init__(self,source,**kwargs):
        super().__init__(source,**kwargs)
        self.p.aspect_scale=1
        self.p.match_aspect=True
        self.p.sizing_mode="scale_height"

    def plot(self,x,y,line=False,**kwargs):
        self.p.circle(x, y,fill_color=None,source=self.source,**kwargs)
        if line:
            self.p.line(x,y,source=self.source,**kwargs)
        return self

    def add_vector(self):    
        self.p.add_layout(Arrow(end=NormalHead(size=5), line_color="red",
            x_start='x',y_start='y',x_end='x+0.8',
            y_end='y+0.6',
            source=self.source))
        return self

    def add_line(self,**kwargs):
        self.p.line(source=self.source,**kwargs)

class time(base):
    """
    Figure class that plot state variables vs time
    """
    def __init__(self,source,**kwargs):
        super().__init__(source,**kwargs)
        self.p.sizing_mode="stretch_both"
        self.p.xaxis.formatter=DatetimeTickFormatter(
            minsec=["%m/%d/%Y %H:%M:%S"],
            minutes=["%m/%d/%Y %H:%M:%S"],
            hourmin=["%m/%d/%Y %H:%M:%S"],
            seconds=["%m/%d/%Y %H:%M:%S"],
            hours=["%m/%d/%Y %H:%M:%S"],
            days=["%m/%d/%Y %H:%M:%S"],
            months=["%m/%d/%Y %H:%M:%S"],
            years=["%m/%d/%Y %H:%M:%S"],
        ) 
        self.p.xaxis.major_label_orientation = math.pi/4

    def add_line(self,t,state,color=None):
        self.p.line(x=t,y=state,source=self.source,legend=dict(value=state),
            line_color=color)

    def plot(self,t,state,color=None):
        self.p.circle(x=t,y=state,source=self.source,legend=dict(value=state),
            line_color=color,fill_color=color)
        self.p.line(x=t,y=state,source=self.source,legend=dict(value=state),
            line_color=color)
        return self

    def save(self,name="time.html",pshow=True):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

def display(pList,name="pviz.html"):
    output_file(name)
    show(layout([p.get_figure() for p in pList],sizing_mode="stretch_both"))