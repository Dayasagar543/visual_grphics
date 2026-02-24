import numpy as np
from vpython import *
from time import sleep
import time as tm

#home positions
x_home=0
y_home=0
z_home=0

#active positions
max_RED_position=255
max_GREEN_position=255
max_BLUE_position=255

#colors of the loop
ball_color=0


ball_radius=6
Ball=sphere(color=vector(ball_color,ball_color,ball_color),pos=vector(x_home,y_home,z_home),radius=ball_radius)
#colors to change
delta_color=0
steps=500
while True:
    for delta_color in np.linspace(0,255,steps):
        Ball.color=vector(delta_color,y_home,z_home)
    for delta_color in np.linspace(0,255,steps):
        Ball.color=vector(x_home,delta_color,z_home)
    for delta_color in np.linspace(0,255,steps):
        Ball.color=vector(x_home,y_home,delta_color)
   
    pass