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

# graph
scene_graph = graph(title="Series RLC Circuit Response", xtitle="Time (s)", ytitle="Amplitude", width=800, height=400)
current_plot = gcurve(graph=scene_graph, color=color.blue, label="Inductor Current (A)", fast=False)
voltage_plot = gcurve(graph=scene_graph, color=color.red, label="Capacitor Voltage (V)", fast=False)

# trash
box(pos=vec(16.2,-10.3,0),height=1.5,length=3.3,width=0.1)
text(pos=vec(14.55,-10.7,0),axis=vec(3,0,0),text="Trash",color=color.black,depth=0.05)


# classes
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
        if self.covered_line!=None:
            self.covered_line.visible = True
            
class Inductor(Component) :
    def __init__(self,ind=0.01) :
        Component.__init__(self)
        self.kind = "inductor"
        self.inductance = ind
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.hel = helix(pos=vec(-3,0,0),axis=vec(6,0,0),color=color.red,coils=15)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(2,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(3,0,0),axis=vec(2,0,0),radius=0.05)
        self.parts = [self.outline,self.hel,self.leftl,self.rightl]

class Capacitor(Component) :
    def __init__(self,cap=0.04,vol=10) :
        Component.__init__(self)
        self.kind = "capacitor"
        self.capacitance = cap
        self.voltage = vol
        self.charge = cap*vol
        self.outline = box(pos=vec(0,0,0),length=6,height=2,opacity=0)
        self.left_plate = box(pos=vec(-0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.right_plate = box(pos=vec(0.5,0,0),length=0.2,height=3,width=0.2,color=color.red)
        self.leftl = cylinder(pos=vec(-5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.rightl = cylinder(pos=vec(.5,0,0),axis=vec(4.5,0,0),radius=0.05)
        self.parts = [self.outline,self.left_plate,self.right_plate,self.leftl,self.rightl]
            
class Resistor(Component) :
    def __init__(self,res=0.1) :
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


# globals
dragObject = None
lastPos = None
started = False
objects = []
edges = []
loops = []


# mouse-related functions
def drag(evt) :
    global dragObject, lastPos
    if started==False:
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
        if shift!=None or shift == vec(0,0,0):
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
    

# button-related functions
def new_inductor(evt) :
    if started==False:
        ind = Inductor()
        objects.append(ind)
    
def new_capacitor(evt) :
    if started==False:
        cap = Capacitor()
        objects.append(cap)
    
def new_resistor(evt) :
    if started==False:
        res = Resistor()
        objects.append(res)
    
def new_horiz_wire(evt) :
    if started==False:
        wire = Wire(vec(-5,0,0),vec(10,0,0),"horiz")
        objects.append(wire)
    
def new_vert_wire(evt) :
    if started==False:
        wire = Wire(vec(0,-3,0),vec(0,6,0),"vert")
        objects.append(wire)
    
def run(evt) :
    global started, loops, edges
    if started==True:
        return None
    reset_graph(evt)
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
        edge = [node1, node2, obj]
        node1.edges.append(edge)
        node2.edges.append(edge)
        edges.append(edge)
    loops = []
    loops = find_loops(nodes,edges)
    for i in range(len(loops)):
        for edge in loops[i]:
            if len(edge) < 4:
                edge.append([])
            edge[3].append(i)
    if len(loops)==0 :
        print("Must have at least one loop to run")
        return None
    print("loops found:")
    print(len(loops))
    for i in range(len(loops)):
        print("loop",i+1)
        for edge in loops[i]:
            print(edge[2].kind)
    for edge in edges:
        if len(edge) > 3 and len(edge[3]) > 1:
            print("shared component:", edge[2].kind)
    started = True
    for line in horiz :
        line.visible = False
    for line in vert :
        line.visible = False
        
def stop(evt) :
    global started
    started = False
    for line in horiz :
        line.visible = True
    for line in vert :
        line.visible = True
    for obj in objects :
        obj.covered_line.visible = False
        
def reset(evt) :
    global objects
    if started==True :
        stop(evt)
    for obj in objects:
        obj.destroy()
    objects = []
    loops = []
    edges = []
    reset_graph(evt)
    
def reset_graph(evt) :
    current_plot.data = []
    current_plot.delete()
    voltage_plot.data = []
    voltage_plot.delete()
    
    
# basic circuits
def simple_rlc(evt) :
    global dragObject
    reset(evt)
    new_resistor(evt)
    dragObject = objects[0]
    shift = vec(0,3,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[1]
    shift = vec(0,-3,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    new_capacitor(evt)
    dragObject = objects[2]
    shift = vec(-10,3,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    new_inductor(evt)
    dragObject = objects[3]
    shift = vec(-10,-3,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[4]
    shift = vec(-15,0,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[5]
    shift = vec(5,0,0)-dragObject.outline.pos
    dragObject.move(shift)
    drop(evt)
    
def simple_rc(evt):
    global dragObject
    reset(evt)
    new_resistor(evt)
    dragObject = objects[0]
    dragObject.move(vec(0,3,0) - dragObject.outline.pos)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[1]
    dragObject.move(vec(0,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_capacitor(evt)
    dragObject = objects[2]
    dragObject.move(vec(-10,3,0) - dragObject.outline.pos)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[3]
    dragObject.move(vec(-10,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[4]
    dragObject.move(vec(-15,0,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[5]
    dragObject.move(vec(5,0,0) - dragObject.outline.pos)
    drop(evt)
    
def simple_rl(evt):
    global dragObject
    reset(evt)
    new_resistor(evt)
    dragObject = objects[0]
    dragObject.move(vec(0,3,0) - dragObject.outline.pos)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[1]
    dragObject.move(vec(0,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_inductor(evt)
    dragObject = objects[2]
    dragObject.move(vec(-10,3,0) - dragObject.outline.pos)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[3]
    dragObject.move(vec(-10,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[4]
    dragObject.move(vec(-15,0,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[5]
    dragObject.move(vec(5,0,0) - dragObject.outline.pos)
    drop(evt)
    
def double_resistor_rlc(evt):
    global dragObject
    reset(evt)
    new_resistor(evt)
    dragObject = objects[0]
    dragObject.move(vec(-10,3,0) - dragObject.outline.pos)
    drop(evt)
    new_resistor(evt)
    dragObject = objects[1]
    dragObject.move(vec(0,3,0) - dragObject.outline.pos)
    drop(evt)
    new_capacitor(evt)
    dragObject = objects[2]
    dragObject.move(vec(-10,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_inductor(evt)
    dragObject = objects[3]
    dragObject.move(vec(0,-3,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[4]
    dragObject.move(vec(-15,0,0) - dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[5]
    dragObject.move(vec(5,0,0) - dragObject.outline.pos)
    drop(evt)
        

# dfs to find loops
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
    
    
# simulation functions
def simulate(loops, edges) :
    num_loops = len(loops)
    I = []
    for i in range(num_loops):
        I.append(0)
    for obj in objects:
        if obj.kind == "capacitor":
            obj.charge = obj.capacitance * obj.voltage
    t = 0
    t_max = 5
    dt = 0.0001
    
    while t < t_max and started==True:
        rate(10000)
        A = []
        B = []
        for i in range(num_loops):
            row = []
            for k in range(num_loops) :
                row.append(0)
            rhs = 0
            for edge in loops[i]:
                obj = edge[2]
                if obj.kind=="wire":
                    continue
                loops_using = edge[3]
                for k in loops_using:
                    if k==i:
                        sign = 1
                    else:
                        sign = -1
                    if obj.kind=="resistor":
                        row[k] += (obj.resistance*sign)
                    elif obj.kind=="inductor":
                        row[k] += (obj.inductance/dt*sign)
                    elif obj.kind=="capacitor":
                        row[k] += (dt/obj.capacitance*sign)
                old_current = edge_current(edge,i,I)
                if obj.kind == "inductor":
                    rhs = rhs + (obj.inductance / dt) * old_current
                elif obj.kind == "capacitor":
                    rhs = rhs - (obj.charge / obj.capacitance)
            A.append(row)
            B.append(rhs)
        newI = solve_matrix(A,B)
        if newI==None:
            return None
        I = newI
        for edge in edges:
            obj = edge[2]
            if obj.kind == "capacitor":
                loop_index = edge[3][0]
                cap_current = edge_current(edge, loop_index, I)
                obj.charge = obj.charge + cap_current * dt
        current_plot.plot(t, I[0])
        for obj in objects:
            if obj.kind == "capacitor":
                voltage_plot.plot(t, obj.charge / obj.capacitance)
                break
        t = t + dt
            
def edge_current(edge, loop_index, I):
    loops_using = edge[3]
    if len(loops_using) == 1:
        return I[loop_index]
    other = loops_using[0]
    if other == loop_index:
        other = loops_using[1]
    return I[loop_index] - I[other]

def solve_matrix(A, b):
    n = len(b)
    for i in range(n):
        max_row = i
        for r in range(i+1, n):
            if abs(A[r][i]) > abs(A[max_row][i]):
                max_row = r
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        pivot = A[i][i]

        if abs(pivot) < 0.0000000001:
            print("Matrix cannot be solved")
            return None

        for c in range(i, n):
            A[i][c] = A[i][c] / pivot
        b[i] = b[i] / pivot

        for r in range(n):
            if r != i:
                factor = A[r][i]
                for c in range(i, n):
                    A[r][c] = A[r][c] - factor * A[i][c]
                b[r] = b[r] - factor * b[i]
    return b
    
    

# mouse binds
scene.bind('mousedown',drag)
scene.bind('mouseup',drop)


# buttons
scene.append_to_caption('\n')
run_button = button(bind=run,text='run simulation')
scene.append_to_caption('    ')
stop_button = button(bind=stop,text='stop simulation')
scene.append_to_caption('    ')
reset_button = button(bind=reset,text='reset')
scene.append_to_caption('\n')
scene.append_to_caption('\n')
simple_loop_button = button(bind=simple_rlc,text="create basic RLC circuit")
scene.append_to_caption('   ')
simple_rc_button = button(bind=simple_rc, text="create basic RC circuit")
scene.append_to_caption('   ')
simple_rl_button = button(bind=simple_rl, text="create basic RL circuit")
scene.append_to_caption('   ')
double_res_button = button(bind=double_resistor_rlc, text="create double resistor RLC")
scene.append_to_caption('\n')
scene.append_to_caption('\n')
new_ind_button = button(bind=new_inductor,text='new inductor')
scene.append_to_caption('    ')
new_cap_button = button(bind=new_capacitor,text='new capacitor')
scene.append_to_caption('    ')
new_res_button = button(bind=new_resistor,text='new resistor')
scene.append_to_caption('    ')
new_horiz_wire_button = button(bind=new_horiz_wire,text='new horizontal wire')
scene.append_to_caption('    ')
new_vert_wire_button = button(bind=new_vert_wire,text='new vertical wire')



# constant loop
while True:
    rate(60)
    if started==True:
        simulate(loops, edges)
        print("Simulation finished.")
        stop(None)
    else:
        if dragObject != None:
            newPos = scene.mouse.project(normal=vec(0,0,1))
            shift = newPos-lastPos
            dragObject.move(shift)
            lastPos = newPos
        
