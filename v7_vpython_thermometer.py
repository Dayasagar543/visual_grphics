from vpython import *
import numpy as np
#null
home_x=0
home_y=0
hom_z=0
#active
home_x_active=1
home_y_active=1
home_z_active=1
#opacity
opacity_value=0.3

#thermometer

#bulbs
glassbulb_radius=1.5
glassbulb=sphere(radius=glassbulb_radius,pos=vector(home_x,home_y,home_x),color=color.white,opacity=opacity_value)

inner_liquid_sphere_radius=1.25
inner_liquid_sphere=sphere(radius=inner_liquid_sphere_radius,pos=vector(home_x,home_y,hom_z),color=color.red)

#cylinder
cylinder_outer_radius=0.75
cylinder_height=6
glasscylinder_outer=cylinder(radius=cylinder_outer_radius,length=cylinder_height,color=color.white,opacity=opacity_value,axis=vector(home_x,home_y_active,hom_z),pos=vector(home_x,home_y+0.2,hom_z))


cylinder_inner_radius=0.5
cylinder_height=6
temperaturecylinder_inner=cylinder(radius=cylinder_inner_radius,length=cylinder_height,color=color.red,opacity=opacity_value,axis=vector(home_x,home_y_active,hom_z),pos=vector(home_x,home_y,hom_z))


for tick in np.linspace(1,6,10):
    length_tick=0.02
    radius_tick=0.75
    disc=cylinder(color=color.cyan,length=length_tick,radius=radius_tick,pos=vector(home_x,tick,hom_z),axis=vector(home_x,home_y_active+1,hom_z))

while True:
    for temperature in np.linspace(1,6,1000):
        rate(100)
        temperaturecylinder_inner.length=temperature
        
    for temperature in np.linspace(6,1,1000):
        rate(100)
        temperaturecylinder_inner.length=temperature
        
        
    pass