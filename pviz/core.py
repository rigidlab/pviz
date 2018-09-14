# Import essential numerical libaries
import math
import random
import time as timer
import numpy as np
import pandas as pd

# Import essential bokeh plotting tools
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import HoverTool, CustomJS, ColumnDataSource,Slider
from bokeh.models import Arrow, NormalHead,Range1d
from bokeh.layouts import column,layout,row,widgetbox
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.models import CustomJS, Slider
from bokeh.io import curdoc
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

class base():
    """
    Base figure class
    """
    def __init__(self,**kwargs):
        tools=["pan,box_zoom,wheel_zoom,xwheel_zoom,ywheel_zoom,save,reset"]
        self.p = figure(logo=None,tools=tools,**kwargs)

    def load(self,source,t='t'):
        if t:
            source[t]=pd.to_datetime(source[t],unit='s')
            source['ts']=source[t].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        self.df=source
        self.source=ColumnDataSource(source)
        #self.source=source
        return self

    def save(self,name="pviz.html",pshow=True):
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
    def __init__(self,xnum_ticks=None,ynum_ticks=None,**kwargs):
        super().__init__(**kwargs)
        self.p.aspect_scale=1
        self.p.match_aspect=True
        self.p.sizing_mode="scale_width"
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None
        if xnum_ticks and ynum_ticks:
            self.p.xgrid[0].ticker.desired_num_ticks=xnum_ticks
            self.p.xgrid[0].ticker.num_minor_ticks=5
            self.p.ygrid[0].ticker.desired_num_ticks=ynum_ticks
            self.p.ygrid[0].ticker.num_minot_ticks=5
        self.current_state=ColumnDataSource(pd.DataFrame({}))
        self.current_index=0
        self.length=0

    def plot(self,x,y,realtime=False,line=False,update_interval=200,slice=None,**kwargs):
        if realtime:
            self.current_x = x
            self.current_y = y
            self.current_theta = 'theta' 
            source = self.current_state
            #curdoc().add_periodic_callback(self.update,update_interval)

        if slice:
            source = ColumnDataSource(self.df.iloc[slice,:])

        self.p.circle(x, y,fill_color=None,source=source,**kwargs)
        self.p.xaxis.axis_label = x
        self.p.yaxis.axis_label = y
        if line:
            self.p.line(x,y,source=source)
        return self

    def vector(self,x,y,theta,length,realtime=False,update_interval=200,size=3,color='black',slice=None):
        source = self.source
        if realtime:
            self.current_x = x
            self.current_y = y
            self.current_theta = theta
            self.length=length
            source = self.current_state
            #curdoc().add_periodic_callback(self.update,update_interval)
        if slice:
            source = ColumnDataSource(self.df.iloc[slice,:])
        if not realtime:
            source.data['x_end'] = source.data[x] + length*np.cos(source.data[theta])
            source.data['y_end'] = source.data[y] + length*np.sin(source.data[theta])
        self.p.add_layout(Arrow(end=NormalHead(size=size), line_color=color,
                x_start=x,y_start=y,x_end='x_end',y_end='y_end',
                source=source))
        self.p.circle(x=x,y=y,color=color,size=size,source=source)
        self.p.circle(x='x_end',y='y_end',color=color,size=0,source=source)
        return self

    def update(self):
        if self.current_index == len(self.df.index):
            self.current_index = 0
        x = self.df[self.current_x][self.current_index]
        y = self.df[self.current_y][self.current_index]
        theta = self.df[self.current_theta][self.current_index]
        x_end = x + self.length*math.cos(theta)
        y_end = y + self.length*math.sin(theta)
        self.current_state.data['index']=[self.current_index]
        self.current_state.data[self.current_x]=[x]
        self.current_state.data[self.current_y]=[y]
        self.current_state.data[self.current_theta]=[theta]
        self.current_state.data['x_end']=[x_end]
        self.current_state.data['y_end']=[y_end]
        print(self.current_state.data)
        self.current_index +=1

    def hover(self,hList):
        hov=HoverTool(tooltips=[(h,"@{}".format(h)) for h in hList])
        self.p.add_tools(hov)
        return self

    def slider(self):
        callback = CustomJS(args=dict(source=self.source), code="""
            var data = source.data;
            var i = index.value;
            var x = data['x'];
            var y = data['y'];
            x = data['x'][i];
            y = data['y'][i];
            source.change.emit();
        """)
        self.i_slider = Slider(start=self.source.data["index"][0], end=self.source.data["index"][-1],
                    value=0, step=1,
                    title="index",callback=callback)
        self.wb = widgetbox(self.i_slider,height=100,width=400)
        return self

    def save(self,name="space.html",pshow=True):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def grid(self,color="gray",alpha=0.3):
        self.p.xgrid.grid_line_color=color
        self.p.ygrid.grid_line_color=color
        self.p.xgrid.grid_line_alpha=alpha
        self.p.ygrid.grid_line_alpha=alpha
        return self

    def make_document(self,doc):
        doc.add_periodic_callback(self.update,200)
        doc.title="Bokeh App"
        layoutr = layout([self.p])
        doc.add_root(layoutr)

    def serve(self,port=5001):
        apps={"/": Application(FunctionHandler(self.make_document))}
        server=Server(apps,port=port)
        server.start()
        server.run_until_shutdown()
        #server.stop()
        return self

class time(base):
    """
    Figure class that plot state variables vs time
    """
    def __init__(self,source,**kwargs):
        super().__init__(source,**kwargs)
        #self.p.sizing_mode="stretch_both"
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
        self.p.xaxis.axis_label = t
        self.p.yaxis.axis_label = state
        return self

    def hover(self,hList):
        hov=HoverTool(tooltips=[(h,"@{}".format(h)) for h in hList])
        self.p.add_tools(hov)
        return self

    def save(self,name="time.html",pshow=True):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

def display(pList,name="pviz.html",realtime=False,**kwargs):
    #show(layout(children=[row([s for s in r ]) for r in pList],
    #   sizing_mode="stretch_both"))
    layoutr=(layout([[s.p for s in r] for r in pList],
        sizing_mode="stretch_both"))

    if not realtime:
        output_file(name)
        show(layoutr)
    else:
        curdoc().add_root(layoutr)

