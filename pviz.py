from bokeh.plotting import figure, output_file, show

class pfig():
    def __init__(self,width,height):
        self.p = figure(plot_width=width,plot_height=height,logo=None,match_aspect=True)
   
    def plot_circle(self,x,y,size=20):
        self.p.circle(x=x, y=y, size=size)

    def plot_rectangle(self,x,y,w=1,h=1):
        self.p.rect(x,y,w,h)

    def plot(self):
        show(self.p)

if __name__=="__main__":
    p = pfig(500,500)
    p.plot_circle(2,2)
    p.plot_rectangle(1,1)
    p.plot()