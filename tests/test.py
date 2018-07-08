import pandas as pd
import copy
from bokeh.plotting import show
from pviz import space,time,display
from bokeh.layouts import column,layout,row

def test_pviz():
    df=pd.read_csv("fmcl.csv",header=0)
    df['t']=pd.to_datetime(df['t'],unit='s')
    s = space(df).plot(x='x',y='y',radius=0.3).slider()
    s1=space(df).plot(x='y',y='x',radius=0.3)
    s2 = time(df).plot('t','y',color='red').plot('t','x',color='green')
    display([[s.p,s2.p],[s.wb]])

def test_usecase():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3).slider()
    display([[s.p],[s.wb]],name="space.html")