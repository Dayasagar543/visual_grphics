from vpython import *
import numpy as np
import math
#postion co ordinates
x_home=0  
y_home=0
z_home=0
# sphere radius
radius_sphere=1
# orb
orb= sphere(radius=radius_sphere,pos=vector(x_home,y_home,z_home),color=vector(radius_sphere,radius_sphere,radius_sphere))
delta_radius=0.01
shpere_radius=0
while True:
    rate(10)
    shpere_radius+=delta_radius
    orb.radius=shpere_radius
    if orb.radius>=1 or orb.radius<=0:
       delta_radius=delta_radius*(-1)  
    pass