import pandas as pd
from bokeh.plotting import show
from pviz import space,time,display
from bokeh.layouts import column,layout,row

def test_pviz():
    df=pd.read_csv("fmcl.csv",header=0)
    df['t']=pd.to_datetime(df['t'],unit='s')
    print (df.head())
    p = space(df)
    #p.add_circle(2,2,radius=0.5)
    #p.add_rectangle(1,1)
    p.plot(x='x',y='y')
    #p.plot()
    ymin,ymax = (df.loc[:, ['x', 'y']].min().min(),
        df.loc[:, ['x', 'y']].max().max())
    delta=ymax-ymin
    p2 = time(df,y_range=(ymin-delta/2,ymax+delta/2))
    p2.plot('t','y',color='red')
    p2.plot('t','x',color='green')
    display([p,p2])

def test_usecase():
    df = pd.DataFrame(data={"t":[0,1,2],"x":[5,6,7],"y":[8,9,10]})
    s=space(df).plot("t","y",radius=0.3)
    display([s],name="space.html")