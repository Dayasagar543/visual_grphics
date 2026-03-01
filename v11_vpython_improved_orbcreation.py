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
chanel_r=1
chanel_g=0
chanel_b=1
delta_r=0.001
delta_b=-0.001
delta_g=0.001
while True:
    rate(90)
    ball_radius+=delta_radius
    Ball.radius=ball_radius
    chanel_r+=delta_r
    chanel_b+=delta_b
    chanel_g+=delta_g
    Ball.color=vector(chanel_r,chanel_g,chanel_b)
    if ball_radius>=1 or ball_radius<=0:
        delta_radius=delta_radius*(-1)
    if chanel_r>=1.5 or chanel_r<=0:
        delta_r=delta_r*(-1)
    if chanel_b>=1.5 or chanel_b<=0:
        chanel_b=chanel_b*(-1)
    if chanel_g>=1.5 or chanel_g<=0:
        chanel_g=chanel_g*(-1)
    
    pass