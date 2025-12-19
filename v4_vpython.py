from vpython import *
from time import *
from math import *
#dimensions
no_dimension=0
sphere_rad=0.5
wall_thickness=0.25
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

# movement positions x
xpos=0
x_move=0.1

while True:
    rate(10)
    # xpos
    xpos+=x_move
    # marble behaviour
    right_marble_edge=xpos+sphere_rad
    left_marble_edge=xpos-sphere_rad

    # walls 
    right_wall_edge=x_wall_dimension/2-wall_thickness/2
    left_wall_edge=-x_wall_dimension/2+wall_thickness/2  
    
     
    
    
    # print(right_marble_edge,right_wall_edge,left_marble_edge,left_wall_edge)
    if right_marble_edge >= right_wall_edge  or left_marble_edge <= left_wall_edge:
        x_move=x_move*(-1)
    ball.pos=vector(xpos,no_dimension,no_dimension)   
    pass