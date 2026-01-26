import numpy as np
from vpython import *
from time import sleep

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
delta_color=0.1

while True:
    
    # ball_color+=delta_color
    # if Ball.color==vector(max_RED_position,y_home,z_home):
    #     ball_color=0
    # else:
    #     rate(5)
    #     Ball.color=vector(ball_color,y_home,z_home)
    
    # if Ball.color==vector(x_home,max_GREEN_position,z_home):
    #     ball_color=0
    # else:
    #     rate(5)
    #     Ball.color=vector(x_home,ball_color,z_home)
    # if Ball.color==vector(x_home,y_home,max_BLUE_position):
    #     ball_color=0
    # else:
    #     rate(5)
    #     Ball.color=vector(x_home,y_home,ball_color)
    
    
    
    #linear color change
    # if Ball.color==vector(max_RED_position,y_home,z_home):
    #     ball_color=0
    # else:
    #     rate(5)
    #     Ball.color=vector(ball_color,y_home,z_home)
    
    #     if Ball.color==vector(x_home,max_GREEN_position,z_home):
    #         ball_color=0
    #     else:
    #         rate(5)
    #         Ball.color=vector(x_home,ball_color,z_home)
    #         if Ball.color==vector(x_home,y_home,max_BLUE_position):
    #             ball_color=0
    #         else:
    #             rate(5)
    #             Ball.color=vector(x_home,y_home,ball_color)
    #             if Ball.color==vector(max_RED_position,max_GREEN_position,z_home):
    #                 ball_color=0
    #             else:
    #                 rate(5)
    #                 Ball.color=vector(ball_color,ball_color,z_home)
    #                 if Ball.color==vector(x_home,max_GREEN_position,max_BLUE_position):
    #                     ball_color=0
    #                 else:
    #                     rate(5)
    #                     Ball.color=vector(x_home,ball_color,ball_color)
    #                     if Ball.color==vector(max_RED_position,y_home,max_BLUE_position):
    #                         ball_color=0
    #                     else:
    #                         rate(5)
    #                         Ball.color=vector(ball_color,y_home,ball_color)
    
    # continue color change
    for red_color in range(0,255,1):
        rate(10)
        Ball.color=vector(red_color,y_home,z_home)
        for green_color in range(0,255,1):
            rate(10)
            Ball.color=vector(red_color,green_color,z_home)
            for blue_color in range(0,255,1):
                rate(10)
                Ball.color=vector(red_color,green_color,blue_color)
    
    if Ball.color==vector(x_home,y_home,z_home) or Ball.color==vector(max_RED_position,max_GREEN_position,max_BLUE_position):
        Ball.color=vector(ball_color*-1,ball_color*-1,ball_color*-1)      
    pass