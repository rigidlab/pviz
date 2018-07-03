import pandas as pd
from bokeh.plotting import show
from pviz import space,time,display
from bokeh.layouts import column,layout,row

def test_pviz():
    df=pd.read_csv("fmcl.csv",header=0)
    df['t']=pd.to_datetime(df['t'],unit='s')
    p = space(df).plot(x='x',y='y',radius=0.3)
    p2 = time(df).plot('t','y',color='red').plot('t','x',color='green')
    display([p,p2])

def test_usecase():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3)
    display([s],name="space.html")