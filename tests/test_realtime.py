import pandas as pd
from pviz import space,time,display
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.layouts import column,layout,row,widgetbox

df=pd.read_csv("fmcl.csv",header=0)
slice=[0,-1]
s=space(output_backend="webgl")
s.load(df).plot("x","y",slice=slice,radius=0.3)
#s.vector('x','y','theta',0.5,slice=slice)
s.vector('x','y','theta',0.5,realtime=True)
#s.plot("x","y",line=True,size=2,slice=slice)
#s.p.x_range.follow = "end"
#s.p.x_range.follow_interval = 100
#s.p.x_range.range_padding =0
s.plot("x","y",realtime=True,radius=0.3)
display([[s]],name="test_vector.html",realtime=True)
#apps={"/": Application(FunctionHandler(make_document))}
#server=Server(apps,port=5001)
#server.show("/")
#server.run_until_shutdown()
