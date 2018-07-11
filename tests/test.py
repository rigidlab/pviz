import pandas as pd
import copy
from bokeh.plotting import show
from pviz import space,time,display
from bokeh.layouts import column,layout,row,gridplot

def test_pviz():
    df=pd.read_csv("fmcl.csv",header=0)
    s = space(df).plot(x='x',y='y',radius=0.3).slider().hover(['ts','x'])
    s1=space(df).plot(x='y',y='x',radius=0.3)
    s2 = time(df).plot('t','y',color='red').hover('x')
    display([[s.p,s2.p]],name="test1.html")
    #show(layout(children=[row(s.wb),row([s.p,s2.p],sizing_mode="stretch_both")]))

def test_usecase():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3).slider().hover(['x','y'])
    display([[s.p]],name="test2.html")
    #show(row(column(s.wb,s.p),))