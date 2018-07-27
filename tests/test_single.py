import pandas as pd
from pviz import space,time,display

def test_space():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3)
    display([[s]],name="test_space.html")

def test_time():
    df=pd.read_csv("fmcl.csv",header=0)
    s=time(df).plot("t","y",color='black')
    df=df.sort_values(by=['t'])
    display([[s]],name="test_time.html")

def test_multiple_plot():
    df=pd.read_csv("fmcl.csv",header=0)
    s1 = space(df).plot(x='x',y='y',radius=0.3).slider()
    s2 = time(df).plot('t','y',color='red')
    display([[s1],[s2]],name="test_multiple_plot.html")

def test_hover():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3).hover(['x','y'])
    display([[s]],name="test_hover.html")

def test_vector():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space(df).plot("x","y",radius=0.3).vector('x','y','theta',0.5)
    display([[s]],name="test_vector.html")

