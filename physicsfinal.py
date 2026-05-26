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
    def delete_obj(self) :
        for obj in self.parts:
            obj.visible = False

class Capacitor :
    def __init__(self,cap=10) :
        self.capacitance = cap
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.left_plate = box(pos=vec(-0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.right_plate = box(pos=vec(0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(.5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.parts = [self.outline,self.left_plate,self.right_plate,self.leftl,self.rightl]
    def move(self,shift):
        for obj in self.parts:
            obj.pos += shift
    def delete_obj(self) :
        for obj in self.parts:
            obj.visible = False
            
class Resistor :
    def __init__(self,res=10) :
        self.resistance = res
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.r1 = cylinder(pos=vec(-3,0,0),axis=vec(.5,1,0),radius=0.05,color=color.orange)
        self.r2 = cylinder(pos=vec(-2.5,1,0),axis=vec(1,-2,0),radius=0.05,color=color.orange)
        self.r3 = cylinder(pos=vec(-1.5,-1,0),axis=vec(1,2,0),radius=0.05,color=color.orange)
        self.r4 = cylinder(pos=vec(-0.5,1,0),axis=vec(1,-2,0),radius=0.05,color=color.orange)
        self.r5 = cylinder(pos=vec(0.5,-1,0),axis=vec(1,2,0),radius=0.05,color=color.orange)
        self.r6 = cylinder(pos=vec(1.5,1,0),axis=vec(1,-2,0),radius=0.05,color=color.orange)
        self.r7 = cylinder(pos=vec(2.5,-1,0),axis=vec(.5,1,0),radius=0.05,color=color.orange)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(2,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(3,0,0),axis=vec(2,0,0),radius=0.05)
        self.parts = [self.outline,self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r7,self.leftl,self.rightl]
    def move(self,shift):
        for obj in self.parts:
            obj.pos += shift
    def destroy(self) :
        for obj in self.parts:
            obj.visible = False


dragObject = None
lastPos = None

objects = []

    
def drag(evt) :
    global dragObject, lastPos
    for obj in objects :
        if scene.mouse.pick == obj.outline:
            dragObject = obj
            lastPos = scene.mouse.project(normal=vec(0,0,1))
        
def drop(evt) :
    global dragObject
    if dragObject!=None:
        obj_pos = dragObject.outline.pos
        shift = snap_obj(obj_pos)
        if shift!=None:
            dragObject.move(shift)
        elif obj_pos.x > 14.55 and obj_pos.x < 17.85 and obj_pos.y > -11.05 and obj_pos.y < -9.55:
            dragObject.destroy()
            objects.remove(dragObject)
        dragObject = None
    
def snap_obj(obj_pos) :
    for i in range(3) :
        for j in range(4) :
            if obj_pos.x < i*10-8 and obj_pos.x > i*10-12 and obj_pos.y < j*6-7 and obj_pos.y > j*6-11 :
                return vec(i*10-10,j*6-9,0)-obj_pos
    return None
    
def new_inductor(evt) :
    ind = Inductor()
    objects.append(ind)
    
def new_capacitor(evt) :
    cap = Capacitor()
    objects.append(cap)
    
def new_resistor(evt) :
    res = Resistor()
    objects.append(res)
        
scene.bind('mousedown',drag)
scene.bind('mouseup',drop)

new_ind_button = button(bind=new_inductor,text='new inductor')
new_cap_button = button(bind=new_capacitor,text='new capacitor')
new_res_button = button(bind=new_resistor,text='new resistor')

box(pos=vec(16.2,-10.3,0),height=1.5,length=3.3,width=0.1)
text(pos=vec(14.55,-10.7,0),axis=vec(3,0,0),text="Trash",color=color.black,depth=0.05)

while True:
    rate(60)
    if dragObject != None:
        newPos = scene.mouse.project(normal=vec(0,0,1))
        shift = newPos-lastPos
        dragObject.move(shift)
        lastPos = newPos
