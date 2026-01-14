from vpython import *
# import time
import random

no_value=0

# ball
radius_ball=0.75
ball=sphere(pos=vector(no_value,no_value,no_value),radius=radius_ball,color=color.red)

#box
wall_thickness=0.5
x_direction=20
y_direction=10
z_direction=10

leftwall=box(pos=vector(-x_direction/2,no_value,no_value),color=color.blue,size=vector(wall_thickness,y_direction,z_direction))
rightwall=box(pos=vector(x_direction/2,no_value,no_value),color=color.blue,size=vector(wall_thickness,y_direction,z_direction))
wall_ceiling=box(pos=vector(no_value,y_direction/2,no_value),color=color.blue,size=vector(x_direction,wall_thickness,z_direction))
wall_floor=box(pos=vector(no_value,-y_direction/2,no_value),color=color.blue,size=vector(x_direction,wall_thickness,z_direction))
backwall=box(pos=vector(no_value,no_value,-z_direction/2),color=color.blue,size=vector(x_direction,y_direction,wall_thickness))

#inital positions
xpos=0
ypos=0
zpos=0


#change in the directions
x_move=0.1
y_move=0.1
z_move=0.1

while True:
  
    # updating the xposition,yposition,zposition
    rate(10)
    xpos=xpos+x_move
    ypos=ypos+y_move
    zpos=zpos+z_move
    
    #borders for x direction
    right_marble_edge=xpos+radius_ball
    left_marble_edge=xpos-radius_ball
    right_wall_edge=x_direction/2-wall_thickness/2
    left_wall_edge=-x_direction/2+wall_thickness/2
    
    
    #borders for y direction
    top_marble_edge=ypos+radius_ball
    bottom_marble_edge=ypos-radius_ball
    top_wall_edge=y_direction/2-wall_thickness/2
    bottom_wall_edge=-y_direction/2+wall_thickness/2
    
    
    #borders for z direction
    back_marble_edge=zpos+radius_ball
    front_marble_edge=zpos-radius_ball
    back_wall_edge=-z_direction/2+wall_thickness/2
    front_wall_edge=z_direction/2-wall_thickness/2
    
    # x_direction
    if right_marble_edge >= right_wall_edge or left_marble_edge <= left_wall_edge:
        x_move=x_move*(-1)
    # y_direction
    if top_marble_edge >= top_wall_edge or bottom_marble_edge <= bottom_wall_edge:
        y_move=y_move*(-1)
    # z_direction
    if back_marble_edge >= back_wall_edge or front_marble_edge <= front_wall_edge:
        z_move=z_move*(-1)
        
    ball.pos = vector(xpos, ypos, zpos)
    pass
