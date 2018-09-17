from bokeh.plotting import figure, show, output_notebook
p = figure(plot_width=400, plot_height=400,
                   toolbar_sticky=False, toolbar_location="below",
                              active_scroll="wheel_zoom", active_drag="box_zoom", tools="reset,wheel_zoom,box_zoom,save")
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15)
show(p)
