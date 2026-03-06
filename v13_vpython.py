from vpython import *
import numpy as np

#home_coordintates
x_home=0
y_home=0
z_home=0

axis_x=1
axis_y=1
axis_z=1

arrow_length=2
arrow_thickness=0.01

PointerX=arrow(length=arrow_length,shaftwidth=arrow_thickness,axis=vector(axis_x,y_home,z_home),color=color.red)
PointerY=arrow(length=arrow_length,shaftwidth=arrow_thickness,axis=vector(x_home,axis_y,z_home),color=color.green)
PointerZ=arrow(length=arrow_length,shaftwidth=arrow_thickness,axis=vector(x_home,y_home,axis_z),color=color.blue)
ball=sphere(radius=arrow_length/100,color=color.cyan,make_trail=True,trail_color=color.orange)

moving_arrow=arrow(length=arrow_length,shaftwidth=arrow_thickness,axis=vector(axis_x,axis_y,axis_z),color=color.yellow)

while True:
    
    for angle in np.linspace(0,2*np.pi,1000):
        rate(50)
        moving_arrow.axis=vector(arrow_length*np.sin(angle),arrow_length*np.cos(angle),z_home)
        ball.pos=vector(arrow_length*np.sin(angle),arrow_length*np.cos(angle),z_home)

    for angle in np.linspace(0,2*np.pi,1000):
        rate(50)
        moving_arrow.axis=vector(arrow_length*np.sin(angle),y_home,arrow_length*np.cos(angle))
        ball.pos=vector(arrow_length*np.sin(angle),y_home,arrow_length*np.cos(angle))
        
    for angle in np.linspace(0,2*np.pi,1000):
        rate(50)
        moving_arrow.axis=vector(x_home,arrow_length*np.cos(angle),arrow_length*np.sin(angle))
        ball.pos=vector(x_home,arrow_length*np.cos(angle),arrow_length*np.sin(angle))



    pass