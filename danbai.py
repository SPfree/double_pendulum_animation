# -*- coding: utf-8 -*-

from math import sin
import numpy as np
from scipy.integrate import odeint
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False
g = 9.8

def pendulum_equations(w, t, l):
    th, v = w
    dth = v
    dv  = - g/l * sin(th)
    return dth, dv

if __name__ == "__main__":
    import pylab as pl
    t = np.arange(0, 10, 0.01)
    track = odeint(pendulum_equations, (0.0, 0), t, args=(1.0,))
    pl.plot(t, track[:, 0])
    pl.title(u"单摆的角度变化, 初始角度=0.0弧度")
    pl.xlabel(u"时间(秒)")
    pl.ylabel(u"震度角度(弧度)")
    pl.show()