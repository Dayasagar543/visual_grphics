from vpython import *
import numpy as np
import random
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
rchan=0
gchan=0
bchan=0
deltR=.001
deltG=.002
deltB=.003
while True:
    rate(100)
    rchan+=deltR+int(random.random())
    gchan+=deltG+int(random.random())
    bchan+=deltB+int(random.random())
    shpere_radius+=delta_radius
    orb.radius=shpere_radius
    orb.color=vector(rchan,gchan,bchan)
    if orb.radius>=1 or orb.radius<=0:
       delta_radius=delta_radius*(-1)  
    if rchan >=1 or rchan<=0:
       deltR=deltR*(-1)
   
    if gchan >=1 or gchan<=0:
       deltG=deltG*(-1)
   
    if bchan >=1 or bchan<=0:
       deltB=deltB*(-1)
   
    pass