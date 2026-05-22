from vpython import *
Web VPython 3.2

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


class Inductor :
    def __init__(self,ind=10) :
        self.inductance = ind
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.hel = helix(pos=vec(-3,0,0),axis=vec(6,0,0),color=color.red,coils=15)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(2,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(3,0,0),axis=vec(2,0,0),radius=0.05)
        self.parts = [self.outline,self.hel,self.leftl,self.rightl]
    def move(self,shift):
        for obj in self.parts:
            obj.pos += shift


dragObject = None
lastPos = None

objects = []

def move_obj(obj_arr, shift) :
    for obj in obj_arr:
        obj.pos += shift
    
def drag(evt) :
    global dragObject, lastPos
    for obj in objects :
        if scene.mouse.pick == obj.outline:
            dragObject = obj
            lastPos = evt.pos
    
        
def drop(evt) :
    global dragObject
    if dragObject!=None:
        shift = snap_obj(dragObject.outline.pos)
        if shift!=None:
            dragObject.move(shift)
        dragObject = None
    
def snap_obj(obj_pos) :
    for i in range(3) :
        for j in range(3) :
            if obj_pos.x < i*10-8 and obj_pos.x > i*10-12 and obj_pos.y < j*6-7 and obj_pos.y > j*6-11 :
                return vec(i*10-10,j*6-9,0)-obj_pos
    return None
    
def new_inductor(evt) :
    ind = Inductor()
    objects.append(ind)
        
scene.bind('mousedown',drag)
scene.bind('mouseup',drop)

new_ind_button = button(bind=new_inductor,text='new inductor')

while True:
    rate(60)
    if dragObject != None:
        newPos = scene.mouse.project(normal=vec(0,0,1))
        shift = newPos-lastPos
        dragObject.move(shift)
        lastPos = newPos
        
