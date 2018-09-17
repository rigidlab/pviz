import pandas as pd
from pviz import space,time,tile_display
def test_space():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space().load(df).plot("x","y",radius=0.3)
    tile_display([[s]],name="test_space.html")
def test_time():
    df=pd.read_csv("fmcl.csv",header=0)
    s=time().load(df).plot("t","y",color='black')
    df=df.sort_values(by=['t'])
    tile_display([[s]],name="test_time.html")

def test_multiple_plot():
    df=pd.read_csv("fmcl.csv",header=0)
    s1 = space().load(df).plot(x='x',y='y',radius=0.3).slider()
    s2 = time().load(df).plot('t','y',color='red')
    tile_display([[s1],[s2]],name="test_multiple_plot.html")

def test_hover():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space().load(df).plot("x","y",radius=0.3).hover(['x','y'])
    tile_display([[s]],name="test_hover.html")

def test_vector():
    df=pd.read_csv("fmcl.csv",header=0)
    s=space().load(df).plot("x","y",radius=0.3).vector('x','y','theta',0.5)
    tile_display([[s]],name="test_vector.html")
