import vpython as vp
import time as tm

sphere= vp.sphere(color=vp.color.purple,radius=10,pos=vp.vector(0,0,0))
# top=vp.box(color=vp.color.cyan,length=100,width=100,height=3,pos=vp.vector(0,50,0))
# left=vp.box(color=vp.color.cyan,length=3,width=100,height=100,pos=vp.vector(-50,0,0))
# right=vp.box(color=vp.color.cyan,length=3,width=100,height=100,pos=vp.vector(50,0,0))
# bottom=vp.box(color=vp.color.cyan,length=100,width=100,height=3,pos=vp.vector(0,-50,0))
# backwall=vp.box(color=vp.color.cyan,length=100,width=3,height=100,pos=vp.vector(0,0,-50))
backwall=vp.box(color=vp.color.cyan,size=vp.vector(100,100,3),pos=vp.vector(0,0,-50))
bottom=vp.box(color=vp.color.cyan,size=vp.vector(100,3,100),pos=vp.vector(0,-50,0))
right=vp.box(color=vp.color.cyan,size=vp.vector(3,100,100),pos=vp.vector(50,0,0))
left=vp.box(color=vp.color.cyan,size=vp.vector(3,100,100),pos=vp.vector(-50,0,0))
top=vp.box(color=vp.color.cyan,size=vp.vector(100,3,100),pos=vp.vector(0,50,0))
deltax=.1
xpos=0

while True:
    vp.rate(40)
    xpos=xpos+deltax
    if xpos>45 or xpos<-45:
        deltax=deltax*(-1)
    sphere.pos=vp.vector(xpos,0,0)
    pass
