from vpython import *
import numpy as np
#home axis values
home_x=0
home_y=0
home_z=0

#activing values
x_axis_active=1
y_axis_active=1
z_axis_active=1

#thermometer1--------------> details and settings
cylinder_length=7
cylinder_inner_radius=0.75
cylinder_outer_radius=1
sphere_outer_radius=1.5
sphere_inner_radius=1.25

themo1Cylinder_outer=cylinder(length=cylinder_length,radius=cylinder_outer_radius,pos=vector(home_x+4,home_y,home_z),color=color.white,axis=vector(home_x,y_axis_active,home_z),opacity=0.1)
themo1Cylinder_inner=cylinder(length=cylinder_length,radius=cylinder_inner_radius,pos=vector(home_x+4,home_y,home_z),color=color.red,axis=vector(home_x,y_axis_active,home_z))
themo1shpere_inner=sphere(radius=sphere_inner_radius,color=color.red,pos=vector(home_x+4,home_y,home_z))
themo1shpere_outer=sphere(radius=sphere_outer_radius,color=color.white,pos=vector(home_x+4,home_y,home_z),opacity=0.2)

                                   

# thermometer2------------------> details and settings
pressure2Cylinder_outer=cylinder(length=cylinder_length,radius=cylinder_outer_radius,pos=vector(home_x-4,home_y,home_z),color=color.white,axis=vector(home_x,y_axis_active,home_z),opacity=0.1)
pressure2Cylinder_inner=cylinder(length=cylinder_length,radius=cylinder_inner_radius,pos=vector(home_x-4,home_y,home_z),color=color.red,axis=vector(home_x,y_axis_active,home_z))
pressure2shpere_inner=sphere(radius=sphere_inner_radius,color=color.red,pos=vector(home_x-4,home_y,home_z))
pressure2shpere_outer=sphere(radius=sphere_outer_radius,color=color.white,pos=vector(home_x-4,home_y,home_z),opacity=0.2)

for tick in np.linspace(1,7,10):
    height_disc=0.05
    radius_disc=0.75
    disc_temp=cylinder(radius=radius_disc,length=height_disc,pos=vector(home_x-4,tick,home_z),color=color.cyan,axis=vector(home_x,y_axis_active,home_z))
    disc_pressure=cylinder(radius=radius_disc,length=height_disc,pos=vector(home_x+4,tick,home_z),color=color.cyan,axis=vector(home_x,y_axis_active,home_z))

while True:
    
    for temperature in np.linspace(1,7,50):
        rate(80)
        themo1Cylinder_inner.length=temperature
    for temperature in np.linspace(7,1,50):
        rate(80)
        themo1Cylinder_inner.length=temperature
    for pressure in np.linspace(1,7,100):
        rate(40)
        pressure2Cylinder_inner.length=pressure
    for pressure in np.linspace(7,1,100):
        rate(40)
        pressure2Cylinder_inner.length=pressure
        
        
        #can also use the increment by adding the small increment for each one and and use the conditinos to stop just as ball
        # in the  the wall 
    pass