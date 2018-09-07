import pandas as pd
from pviz import space,time,display

def test_vector():
    df=pd.read_csv("fmcl.csv",header=0)
    slice=[0,100]
    s=space(df).plot("x","y",slice=slice,radius=0.3)
    s.vector('x','y','theta',0.5,slice=slice)
    #s.plot("x","y",line=True,size=2)
    display([[s]],name="test_vector.html")

  
