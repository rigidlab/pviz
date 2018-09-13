import pandas as pd
from pviz import space,time,display

def test_realtime():
    df=pd.read_csv("fmcl.csv",header=0)
    slice=[0,-1]
    s=space().load(df).plot("x","y",slice=slice,radius=0.3)
    #s.vector('x','y','theta',0.5,slice=slice)
    s.vector('x','y','theta',0.5,realtime=True)
    #s.plot("x","y",line=True,size=2,slice=slice)
    #s.p.x_range.follow = "end"
    #s.p.x_range.follow_interval = 100
    #s.p.x_range.range_padding =0
    s.plot("x","y",realtime=True,radius=0.3)
    display([[s]],name="test_vector.html",realtime=True)

test_realtime()
