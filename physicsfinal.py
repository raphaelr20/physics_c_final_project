from vpython import *
#Web VPython 3.2

scene.camera.pos=vec(0,0,20)

# vertical lines of grid
curve(pos=[vec(-15,-9,0),vec(-15,-3.1,0)],color=color.red)
curve(pos=[vec(-15,-2.9,0),vec(-15,2.9,0)],color=color.red)
curve(pos=[vec(-15,3.1,0),vec(-15,9,0)],color=color.red)
curve(pos=[vec(15,9,0),vec(15,3.1,0)],color=color.red)
curve(pos=[vec(15,-2.9,0),vec(15,2.9,0)],color=color.red)
curve(pos=[vec(15,-3.1,0),vec(15,-9,0)],color=color.red)
curve(pos=[vec(-5,9,0),vec(-5,3.1,0)],color=color.red)
curve(pos=[vec(-5,2.9,0),vec(-5,-2.9,0)],color=color.red)
curve(pos=[vec(-5,-3.1,0),vec(-5,-9,0)],color=color.red)
curve(pos=[vec(5,9,0),vec(5,3.1,0)],color=color.red)
curve(pos=[vec(5,2.9,0),vec(5,-2.9,0)],color=color.red)
curve(pos=[vec(5,-3.1,0),vec(5,-9,0)],color=color.red)

#horizontal lines of grid
curve(pos=[vec(-14.8,9,0),vec(-5.2,9,0)],color=color.red)
curve(pos=[vec(-4.8,9,0),vec(4.8,9,0)],color=color.red)
curve(pos=[vec(14.8,9,0),vec(5.2,9,0)],color=color.red)
curve(pos=[vec(-14.8,3,0),vec(-5.2,3,0)],color=color.red)
curve(pos=[vec(-4.8,3,0),vec(4.8,3,0)],color=color.red)
curve(pos=[vec(14.8,3,0),vec(5.2,3,0)],color=color.red)
curve(pos=[vec(-14.8,-3,0),vec(-5.2,-3,0)],color=color.red)
curve(pos=[vec(-4.8,-3,0),vec(4.8,-3,0)],color=color.red)
curve(pos=[vec(14.8,-3,0),vec(5.2,-3,0)],color=color.red)
curve(pos=[vec(-14.8,-9,0),vec(-5.2,-9,0)],color=color.red)
curve(pos=[vec(-4.8,-9,0),vec(4.8,-9,0)],color=color.red)
curve(pos=[vec(14.8,-9,0),vec(5.2,-9,0)],color=color.red)

dragObject = None
lastPos = None

outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
hel = helix(pos=vec(-2,0,0),axis=vec(4,0,0),color=color.red,coils=10)
leftl = cylinder(pos=vec(-3,0,0),axis=vec(1,0,0),radius=0.05)
rightl = cylinder(pos=vec(2,0,0),axis=vec(1,0,0),radius=0.05)
inductor = [outline,hel,leftl,rightl]

def move_obj(obj_arr, shift) :
    for obj in obj_arr:
        obj.pos += shift
    
def drag(evt) :
    global dragObject, lastPos
    if scene.mouse.pick == outline:
        dragObject = inductor
        lastPos = evt.pos
    
        
def drop(evt) :
    global dragObject
    dragObject = None
        
scene.bind('mousedown',drag)
scene.bind('mouseup',drop)

while True:
    rate(60)
    if dragObject != None:
        newPos = scene.mouse.project(normal=vec(0,0,1))
        shift = newPos-lastPos
        move_obj(dragObject,shift)
        lastPos = newPos

