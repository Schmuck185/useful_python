import pandas as pd
import matplotlib.pyplot as plt

def plot_avp(df,aggby, actcol, predcol,xlab = '', ylab = '', title = ''):
    col = aggby
    vals_act = df.groupby([col])[actcol].mean()
    vals_pred = df.groupby([col])[predcol].mean()

    plt.scatter(x = vals_act.index, y = vals_act.values)
    plt.plot(vals_pred.index, vals_pred.values, c = 'r', linestyle = '-.')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()
