from vpython import *
import numpy as np

null_value=0
active_Value=1

piston=cylinder(axis=vector(null_value,active_Value,null_value),length=6,color=color.yellow,radius=2,opacity=0.2,pos=vector(null_value,-3,null_value))
ball=sphere(radius=3,color=color.blue,pos=vector(6,null_value,null_value))
while True:
    
    for increase in np.linspace(0.1,6,1000):
        rate(50)
        piston.length=increase
        ball.radius=increase/2
        piston.opacity=increase
        ball.opacity=increase
    for decrease in np.linspace(6,0.1,1000):
        rate(50)
        piston.length=decrease
        ball.radius=decrease/2
        piston.opacity=decrease
        ball.opacity=decrease
    pass