Web VPython 3.2

scene.camera.pos=vec(0,0,20)

# vertical lines of grid
v00 = curve(pos=[vec(-15,3.1,0),vec(-15,9,0)],color=color.red)
v01 = curve(pos=[vec(-5,9,0),vec(-5,3.1,0)],color=color.red)
v02 = curve(pos=[vec(5,9,0),vec(5,3.1,0)],color=color.red)
v03 = curve(pos=[vec(15,9,0),vec(15,3.1,0)],color=color.red)
v10 = curve(pos=[vec(-15,-2.9,0),vec(-15,2.9,0)],color=color.red)
v11 = curve(pos=[vec(-5,2.9,0),vec(-5,-2.9,0)],color=color.red)
v12 = curve(pos=[vec(5,2.9,0),vec(5,-2.9,0)],color=color.red)
v13 = curve(pos=[vec(15,-2.9,0),vec(15,2.9,0)],color=color.red)
v20 = curve(pos=[vec(-15,-9,0),vec(-15,-3.1,0)],color=color.red)
v21 = curve(pos=[vec(-5,-3.1,0),vec(-5,-9,0)],color=color.red)
v22 = curve(pos=[vec(5,-3.1,0),vec(5,-9,0)],color=color.red)
v23 = curve(pos=[vec(15,-3.1,0),vec(15,-9,0)],color=color.red)
vert = [v00,v01,v02,v03,v10,v11,v12,v13,v20,v21,v22,v23]

#horizontal lines of grid
c00 = curve(pos=[vec(-14.8,9,0),vec(-5.2,9,0)],color=color.red)
c01 = curve(pos=[vec(-4.8,9,0),vec(4.8,9,0)],color=color.red)
c02 = curve(pos=[vec(14.8,9,0),vec(5.2,9,0)],color=color.red)
c10 = curve(pos=[vec(-14.8,3,0),vec(-5.2,3,0)],color=color.red)
c11 = curve(pos=[vec(-4.8,3,0),vec(4.8,3,0)],color=color.red)
c12 = curve(pos=[vec(14.8,3,0),vec(5.2,3,0)],color=color.red)
c20 = curve(pos=[vec(-14.8,-3,0),vec(-5.2,-3,0)],color=color.red)
c21 = curve(pos=[vec(-4.8,-3,0),vec(4.8,-3,0)],color=color.red)
c22 = curve(pos=[vec(14.8,-3,0),vec(5.2,-3,0)],color=color.red)
c30 = curve(pos=[vec(-14.8,-9,0),vec(-5.2,-9,0)],color=color.red)
c31 = curve(pos=[vec(-4.8,-9,0),vec(4.8,-9,0)],color=color.red)
c32 = curve(pos=[vec(14.8,-9,0),vec(5.2,-9,0)],color=color.red)
horiz = [c00,c01,c02,c10,c11,c12,c20,c21,c22,c30,c31,c32]

class Component :
    def __init__(self) :
        self.parts = []
        self.covered_line = None
        self.kind = ""
    def move(self,shift):
        for obj in self.parts:
            obj.pos += shift
    def destroy(self) :
        for obj in self.parts:
            obj.visible = False
            
class Inductor(Component) :
    def __init__(self,ind=10) :
        Component.__init__(self)
        self.kind = "inductor"
        self.inductance = ind
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.hel = helix(pos=vec(-3,0,0),axis=vec(6,0,0),color=color.red,coils=15)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(2,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(3,0,0),axis=vec(2,0,0),radius=0.05)
        self.parts = [self.outline,self.hel,self.leftl,self.rightl]

class Capacitor(Component) :
    def __init__(self,cap=10) :
        Component.__init__(self)
        self.kind = "capacitor"
        self.capacitance = cap
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.left_plate = box(pos=vec(-0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.right_plate = box(pos=vec(0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(.5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.parts = [self.outline,self.left_plate,self.right_plate,self.leftl,self.rightl]
            
class Resistor(Component) :
    def __init__(self,res=10) :
        Component.__init__(self)
        self.kind = "resistor"
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
        
class Wire(Component) :
    def __init__(self,posit,ax,dir) :
        Component.__init__(self)
        self.kind = "wire"
        self.direction = dir
        self.outline = box(pos=posit+ax/2,length=ax.x if ax.x != 0 else 0.3,height=ax.y if ax.y != 0 else 0.3,opacity = 0)
        self.line = cylinder(pos=posit,axis=ax,radius=0.05)
        self.parts = [self.outline,self.line]
        
class Node() :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.edges = []


dragObject = None
lastPos = None

objects = []

    
def drag(evt) :
    global dragObject, lastPos
    for obj in objects :
        if scene.mouse.pick == obj.outline:
            dragObject = obj
            if dragObject.covered_line != None:
                dragObject.covered_line.visible = True
                dragObject.covered_line = None
            lastPos = scene.mouse.project(normal=vec(0,0,1))
        
def drop(evt) :
    global dragObject
    if dragObject!=None:
        obj_pos = dragObject.outline.pos
        shift = snap_obj(obj_pos)
        if dragObject.kind=="wire" :
            if dragObject.direction=="vert":
                shift = snap_obj_vert(obj_pos)
        if shift!=None:
            dragObject.move(shift)
            new_pos = dragObject.outline.pos;
            if dragObject.kind=="wire" :
                if dragObject.direction=="vert":
                    dragObject.covered_line = vert[(2-(new_pos.y+6)/6)*4+(new_pos.x+15)/10]
                    dragObject.covered_line.visible = False
                else :
                    dragObject.covered_line = horiz[(3-(new_pos.y+9)/6)*3+(new_pos.x+10)/10]
                    dragObject.covered_line.visible = False
            else :
                dragObject.covered_line = horiz[(3-(new_pos.y+9)/6)*3+(new_pos.x+10)/10]
                dragObject.covered_line.visible = False
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
def snap_obj_vert(obj_pos) :
    for i in range(4) :
        for j in range(3) :
            if obj_pos.x < i*10-13 and obj_pos.x > i*10-17 and obj_pos.y < j*6-4 and obj_pos.y > j*6-8 :
                return vec(i*10-15,j*6-6,0)-obj_pos
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
    
def new_horiz_wire(evt) :
    wire = Wire(vec(-5,0,0),vec(10,0,0),"horiz")
    objects.append(wire)
    
def new_vert_wire(evt) :
    wire = Wire(vec(0,-3,0),vec(0,6,0),"vert")
    objects.append(wire)
    
def run(evt) :
    nodes = []
    for j in range(4):
        row = []
        for i in range(4):
            row.append(Node(i,j))
        nodes.append(row)
    edges = []
    for obj in objects:
        if obj.covered_line == None:
            print("All objects must be on the circuit or removed in the trash")
            return None
        if obj.kind == "wire" and obj.direction == "vert":
            col = int((obj.outline.pos.x + 15)/10)
            row = int(2-(obj.outline.pos.y + 6)/6)
            node1 = nodes[row][col]
            node2 = nodes[row+1][col]
        else:
            col = int((obj.outline.pos.x + 10)/10)
            row = int(3-(obj.outline.pos.y + 9)/6)
            node1 = nodes[row][col]
            node2 = nodes[row][col+1]
        edge = (node1,node2,obj)
        node1.edges.append(edge)
        node2.edges.append(edge)
        edges.append(edge)
    loops = find_loops(nodes,edges)
    print("loops found:")
    print(len(loops))
    for i in range(len(loops)):
        print("loop",i+1)
        for edge in loops[i]:
            print(edge[2].kind)
        
def other_node(edge,node):
    if edge[0] == node:
        return edge[1]
    else:
        return edge[0]

def build_tree(node,visited,tree_edges,extra_edges):
    visited.append(node)
    for edge in node.edges:
        next_node = other_node(edge, node)
        if next_node not in visited:
            tree_edges.append(edge)
            build_tree(next_node,visited,tree_edges,extra_edges)
        elif edge not in tree_edges and edge not in extra_edges:
            extra_edges.append(edge)

def find_path(current,target,tree_edges,visited,path):
    if current == target:
        return True
    visited.append(current)
    for edge in tree_edges:
        if edge[0] == current:
            next_node = edge[1]
        elif edge[1] == current:
            next_node = edge[0]
        else:
            continue
        if next_node not in visited:
            path.append(edge)
            if find_path(next_node,target,tree_edges,visited,path):
                return True
            path.pop()
    return False

def find_path_wrapper(start,end,tree_edges):
    visited = []
    path = []
    if find_path(start,end,tree_edges,visited,path):
        return path
    return None

def find_loops(nodes,edges):
    visited = []
    tree_edges = []
    extra_edges = []
    start = None
    for row in nodes:
        for node in row:
            if len(node.edges) > 0:
                start = node
                break
        if start != None:
            break
    if start == None:
        return []
    build_tree(start,visited,tree_edges,extra_edges)
    loops = []
    for edge in extra_edges:
        path = find_path_wrapper(edge[0],edge[1],tree_edges)
        if path != None:
            loop = path[:]
            loop.append(edge)
            loops.append(loop)
    return loops
    
        
        
scene.bind('mousedown',drag)
scene.bind('mouseup',drop)

new_ind_button = button(bind=new_inductor,text='new inductor')
new_cap_button = button(bind=new_capacitor,text='new capacitor')
new_res_button = button(bind=new_resistor,text='new resistor')
new_horiz_wire_button = button(bind=new_horiz_wire,text='new horizontal wire')
new_vert_wire_button = button(bind=new_vert_wire,text='new vertical wire')
run_button = button(bind=run,text='run simulation')

box(pos=vec(16.2,-10.3,0),height=1.5,length=3.3,width=0.1)
text(pos=vec(14.55,-10.7,0),axis=vec(3,0,0),text="Trash",color=color.black,depth=0.05)

while True:
    rate(60)
    if dragObject != None:
        newPos = scene.mouse.project(normal=vec(0,0,1))
        shift = newPos-lastPos
        dragObject.move(shift)
        lastPos = newPos
        
