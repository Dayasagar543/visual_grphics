import numpy as np
from vpython import *
import datetime as dt

x_home=0
y_home=0
z_home=0

radius_ball=1
# print(tm.localtime())
# print(dt.date.today())

Ball=sphere(color=color.white,pos=vector(x_home,y_home,z_home),radius=radius_ball)
delta_variance=0.01
ball_Radius=0
while True:
    rate(50)
    ball_Radius+=delta_variance
    Ball.radius=ball_Radius
    if ball_Radius>=1 or ball_Radius<=0:
        delta_variance=-delta_variance
    pass
