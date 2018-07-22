import pandas as pd
import copy
from bokeh.plotting import show
from pviz import space,time,display
from bokeh.layouts import column,layout,row,gridplot

def test_multiple_plot():
    df=pd.read_csv("fmcl.csv",header=0)
    s1 = space(df).plot(x='x',y='y',radius=0.3).slider().hover(['ts','x'])
    s2 = time(df).plot('t','y',color='red').hover('x')
    display([[s1],[s2]],name="test1.html")

def test_space():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3).slider().hover(['x','y'])
    display([[s]],name="test2.html")
    #show(row(column(s.wb,s.p),))
