from vpython import *
from time import *
from math import *
#dimensions
no_dimension=0
sphere_rad=0.5
wall_thickness=0.5
x_wall_dimension=10
y_wall_dimension=10
z_wall_dimension=10

#creation_of_models

ball=sphere(radius=sphere_rad,pos=vector(no_dimension,no_dimension,no_dimension),color=color.blue)
ceiling_wall=box(size=vector(x_wall_dimension,wall_thickness,z_wall_dimension),pos=vector(no_dimension,y_wall_dimension/2,no_dimension),color=color.magenta)
floor_wall=box(size=vector(x_wall_dimension,wall_thickness,z_wall_dimension),pos=vector(no_dimension,-y_wall_dimension/2,no_dimension),color=color.magenta)
right_wall=box(size=vector(wall_thickness,y_wall_dimension,z_wall_dimension),pos=vector(x_wall_dimension/2,no_dimension,no_dimension),color=color.magenta)
left_wall=box(size=vector(wall_thickness,y_wall_dimension,z_wall_dimension),pos=vector(-x_wall_dimension/2,no_dimension,no_dimension),color=color.magenta)
back_wall=box(size=vector(x_wall_dimension,y_wall_dimension,wall_thickness),pos=vector(no_dimension,no_dimension,-z_wall_dimension/2),color=color.magenta)

xpos=0
x_move=0.1
ypos=0
y_move=0.1
zpos=0
z_move=0.1
time_sleep=5
while True:
    rate(10)
    xpos+=x_move
    if xpos > x_wall_dimension/2 or xpos < -x_wall_dimension/2:
        x_move=x_move*(-1)
    ball.pos=vector(xpos,no_dimension,no_dimension)   
    # sleep(time_sleep)
    
    # rate(10)
    # ypos+=ypos
    # if ypos > y_wall_dimension/2 or ypos < -y_wall_dimension/2:
    #     y_move=y_move*(-1)
    # ball.pos=vector(no_dimension,ypos,no_dimension)
    # sleep(time_sleep)  
     
    # rate(10)
    # zpos+=zpos
    # if zpos > z_wall_dimension/2 or zpos < -z_wall_dimension/2:
    #     z_move=z_move*(-1)
    # ball.pos=vector(no_dimension,no_dimension,zpos) 
    # sleep(time_sleep)
      
    pass