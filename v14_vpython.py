from vpython import *
import numpy as np

null_value=0
x_home=0
y_home=0
z_home=0

x_active=1
y_active=1
z_active=1

cylinder_length=0.2

radius_clock=float(input("please enter the radius of the clock"))
clock_disc=cylinder(radius=radius_clock,color=vector(x_home,125,110),pos=vector(x_home,y_home,z_home),axis=vector(x_home,y_home,-z_active),length=cylinder_length)
major_tics_length=radius_clock/10
major_tics_width=2*np.pi*radius_clock/100
major_tics_height=radius_clock/20
minor_tics_length=radius_clock/100
minor_tics_width=major_tics_width/100
minor_tics_height=radius_clock/100

while True:
    for radians in np.linspace(null_value,2*np.pi,13):
        major_Tics=box(color=color.red,pos=vector(radius_clock*np.cos(radians),radius_clock*np.sin(radians),z_home),axis=vector(radius_clock*np.cos(radians),radius_clock*np.sin(radians),z_active),length=major_tics_length,width=major_tics_width,height=major_tics_height)
   
    for radians in np.linspace(null_value,2*np.pi,67):
        minor_Tics=box(color=color.blue,pos=vector(radius_clock*np.cos(radians),radius_clock*np.sin(radians),z_home),axis=vector(radius_clock*np.cos(radians),radius_clock*np.sin(radians),z_active),length=minor_tics_length,width=minor_tics_width,height=minor_tics_height)
    pass                                   