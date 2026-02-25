import random
from vpython import *
import numpy as np

# home_positions
x_home=0
y_home=0
z_home=0

#ball radius
ball_radius=1

Ball=sphere(color=color.white,pos=vector(x_home,y_home,z_home),radius=ball_radius)
delta_radius=0.001

while True:
    rate(50)
    ball_radius+=delta_radius
    Ball.radius=ball_radius
    if ball_radius>=1 or ball_radius<=0:
        delta_radius=delta_radius*(-1)
    pass