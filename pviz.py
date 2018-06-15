from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

class pfig():
    def __init__(self,width,height):
        hover=HoverTool(tooltips=[("x,y","$x,$y")])
        tools=["pan,box_zoom,wheel_zoom,save,reset,crosshair",hover]
        self.p = figure(plot_width=width,plot_height=height,logo=None,
                aspect_scale=1,match_aspect=True,tools=tools)
        self.p.xgrid.grid_line_color=None
        self.p.ygrid.grid_line_color=None

    def plot_circle(self,x,y,radius=1):
        self.p.circle(x=x, y=y, radius=radius)

    def plot_rectangle(self,x,y,w=1,h=1):
        self.p.rect(x,y,w,h)

    def plot(self):
        show(self.p)

if __name__=="__main__":
    p = pfig(500,500)
    p.plot_circle(2,2,radius=0.1)
    p.plot_rectangle(1,1)
    p.plot()
