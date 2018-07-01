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

class space():
    """
    Figure class that plot state variables against one another
    """
    def __init__(self,source,w=500,h=500,**kwargs):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset"]
        self.p = figure(plot_width=w,plot_height=h,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools,**kwargs)
        #self.p.xgrid.grid_line_color=None
        #self.p.ygrid.grid_line_color=None
        self.source=source

    def add_circle(self,x,y,**kwargs):
        self.p.circle(x=x, y=y,fill_color=None,**kwargs)

    def add_vector(self):    
        self.p.add_layout(Arrow(end=NormalHead(size=5), line_color="red",
            x_start='x',y_start='y',x_end='x+0.8',
            y_end='y+0.6',
            source=self.source))

    def add_line(self,**kwargs):
        self.p.line(source=self.source,**kwargs)

    def add_rectangle(self,x,y,w=1,h=1):
        self.p.rect(x,y,w,h)

    def plot(self,name="pviz.html",pshow=False):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

class state():
    """
    Figure class that plot state variables vs time
    """
    def __init__(self,source,w=500,h=500,**kwargs):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset"]
        self.p = figure(plot_width=w,plot_height=h,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools,**kwargs)
        #self.p.xgrid.grid_line_color=None
        #self.p.ygrid.grid_line_color=None
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
        self.source=source

    def add_vector(self): 
        self.p.add_layout(Arrow(end=NormalHead(size=5), line_color="red",
            x_start='x',y_start='y',x_end='x+0.8',y_end='y+0.6',
            source=self.source))

    def add_line(self,t,state,color=None):
        self.p.line(x=t,y=state,source=self.source,legend=dict(value=state),
            line_color=color)

    def add_circle(self,t,state,color=None):
        self.p.circle(x=t,y=state,source=self.source,legend=dict(value=state),
            line_color=color,fill_color=color,)

    def add_rectangle(self,x,y,w=1,h=1):
        self.p.rect(x,y,w,h)

    def plot(self,name="pviz.html",pshow=False):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

def test():
    df=pd.read_csv("fmcl.csv",header=0)
    df['t']=pd.to_datetime(df['t'],unit='s')
    print (df.head())
    p = space(df)
    #p.add_circle(2,2,radius=0.5)
    #p.add_rectangle(1,1)
    p.add_line(x='x',y='y')
    #p.plot()
     
    ymin,ymax = (df.loc[:, ['x', 'y']].min().min(),
        df.loc[:, ['x', 'y']].max().max())
    delta=ymax-ymin
    p2 = state(df,y_range=(ymin-delta/2,ymax+delta/2))
    p2.add_circle('t','y',color='red')
    p2.add_circle('t','x',color='green')
    show(column(p.get_figure(),p2.get_figure()))
    #show(p2.get_figure())

if __name__=="__main__":
    print "Running"
