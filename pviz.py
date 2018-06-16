from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.layouts import column,layout,row

class space():
    """
    Figure class that plot state variables against one another
    """
    def __init__(self,width,height):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset,crosshair",hover]
        self.p = figure(plot_width=width,plot_height=height,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools)
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None

    def add_circle(self,x,y,radius=1,**kwargs):
        self.p.circle(x=x, y=y, radius=radius,fill_color=None,**kwargs)

    def add_rectangle(self,x,y,w=1,h=1):
        self.p.rect(x,y,w,h)

    def plot(self,name=None):
        if name:
            output_file(name)
        show(self.p)

    def get_figure(self):
        return self.p

class state():
    """
    Figure class that plot state variables vs time
    """
    def __init__(self,width,height):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset,crosshair",hover]
        self.p = figure(plot_width=width,plot_height=height,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools)
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None

    def add_circle(self,x,y,radius=1,**kwargs):
        self.p.circle(x=x, y=y, radius=radius,fill_color=None,**kwargs)
 
    def plot(self,name=None):
        if name:
            output_file(name)
        show(self.p)

    def get_figure(self):
        return self.p

if __name__=="__main__":
    p = space(500,500)
    p.add_circle(2,2,radius=0.1)
    p.add_rectangle(1,1)
    p.plot()

