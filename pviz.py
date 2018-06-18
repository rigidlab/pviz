from bokeh.plotting import figure, output_file, show, save
from bokeh.models import HoverTool, CustomJS, ColumnDataSource,Slider
from bokeh.models import Arrow, NormalHead
from bokeh.layouts import column,layout,row

class space():
    """
    Figure class that plot state variables against one another
    """
    def __init__(self,source,w=500,h=500,**kwargs):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset"]
        self.p = figure(plot_width=w,plot_height=h,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools,**kwargs)
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None
        self.source=source

    def add_circle(self,x,y,**kwargs):
        self.p.circle(x=x, y=y,fill_color=None,**kwargs)
        
    def add_vector(self):    
        self.p.add_layout(Arrow(end=NormalHead(size=5), line_color="red",
                                x_start='x',y_start='y',x_end='x+0.8',y_end='y+0.6',
                                source=self.source))
    
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
    def __init__(self,w=500,h=500,**kwargs):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset,crosshair",hover]
        self.p = figure(plot_width=w,plot_height=h,**kwargs,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools)
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None

    def plot(self,name="pviz.html",pshow=False):
        output_file(name)
        save(self.p)
        if pshow:
            show(self.p)

    def get_figure(self):
        return self.p

if __name__=="__main__":
    p = space(x_range=(-5,5),y_range=(-5,5))
    p.add_circle(2,2,radius=0.5)
    p.add_rectangle(1,1)
    p.plot()
