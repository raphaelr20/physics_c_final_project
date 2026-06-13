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
scene_graph = graph(title="RLC Circuit Response | MNA solver", xtitle="Time (s)", ytitle="Amplitude", width=800, height=400)
current_plot = gcurve(graph=scene_graph, color=color.blue, label="Current", fast=False)
voltage_plot = gcurve(graph=scene_graph, color=color.red, label="Capacitor Voltage", fast=False)

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
        self.current = 0
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
        self.old_voltage = vol
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
selected_component = None
initial_voltage = 10
component_slider_value = 0.1


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
        if dragObject.kind=="wire" and dragObject.direction=="vert":
            shift = snap_obj_vert(obj_pos)
        if shift!=None or shift == vec(0,0,0):
            dragObject.move(shift)
            new_pos = dragObject.outline.pos
            if dragObject.kind=="wire" and dragObject.direction=="vert":
                dragObject.covered_line = vert[int((2-(new_pos.y+6)/6)*4+(new_pos.x+15)/10)]
            else:
                dragObject.covered_line = horiz[int((3-(new_pos.y+9)/6)*3+(new_pos.x+10)/10)]
            dragObject.covered_line.visible = False
            select_component(dragObject)
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
        objects.append(Inductor())

def new_capacitor(evt) :
    if started==False:
        objects.append(Capacitor(vol=initial_voltage))

def new_resistor(evt) :
    if started==False:
        objects.append(Resistor())

def new_horiz_wire(evt) :
    if started==False:
        objects.append(Wire(vec(-5,0,0),vec(10,0,0),"horiz"))

def new_vert_wire(evt) :
    if started==False:
        objects.append(Wire(vec(0,-3,0),vec(0,6,0),"vert"))

def component_value(obj):
    if obj.kind=="resistor":
        return obj.resistance
    if obj.kind=="inductor":
        return obj.inductance
    if obj.kind=="capacitor":
        return obj.capacitance
    return 0

def component_unit(obj):
    if obj.kind=="resistor":
        return "ohms"
    if obj.kind=="inductor":
        return "henrys"
    if obj.kind=="capacitor":
        return "farads"
    return ""

def select_component(obj):
    global selected_component, component_slider_value
    if obj.kind!="wire":
        selected_component = obj
        component_slider_value = component_value(obj)
        component_value_slider.value = component_slider_value
        selected_text.text = "selected " + obj.kind + ": " + str(round(component_value(obj),4)) + " " + component_unit(obj)
        component_value_text.text = " component value = " + str(round(component_value(obj),4)) + " " + component_unit(obj)

def set_component_value(s):
    global component_slider_value
    component_slider_value = s.value
    if selected_component == None:
        component_value_text.text = " component value = " + str(round(component_slider_value,4))
    else:
        component_value_text.text = " component value = " + str(round(component_slider_value,4)) + " " + component_unit(selected_component)

def apply_value(evt):
    global selected_component
    if selected_component == None:
        print("No resistor, capacitor, or inductor selected")
        return None
    val = component_slider_value
    if selected_component.kind=="resistor":
        selected_component.resistance = val
    elif selected_component.kind=="inductor":
        selected_component.inductance = val
    elif selected_component.kind=="capacitor":
        selected_component.capacitance = val
        selected_component.charge = selected_component.capacitance*selected_component.voltage
    selected_text.text = "selected " + selected_component.kind + ": " + str(round(component_value(selected_component),4)) + " " + component_unit(selected_component)
    component_value_text.text = " component value = " + str(round(component_value(selected_component),4)) + " " + component_unit(selected_component)

def set_initial_voltage(s):
    global initial_voltage
    initial_voltage = s.value
    voltage_text.text = " initial capacitor voltage = " + str(round(initial_voltage,2)) + " V"
    if started==False:
        for obj in objects:
            if obj.kind=="capacitor":
                obj.voltage = initial_voltage
                obj.old_voltage = initial_voltage
                obj.charge = obj.capacitance*obj.voltage

def run(evt) :
    global started, edges
    if started==True:
        return None
    reset_graph(evt)
    edges = build_edges()
    if edges == None:
        return None
    if build_node_map(edges)[1] == 0:
        print("No complete circuit to solve")
        return None
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
        if obj.covered_line != None:
            obj.covered_line.visible = False

def reset(evt) :
    global objects, edges, selected_component
    if started==True:
        stop(evt)
    for obj in objects:
        obj.destroy()
    objects = []
    edges = []
    selected_component = None
    selected_text.text = "selected component: none"
    component_value_text.text = " component value = 0.1"
    component_value_slider.value = 0.1
    reset_graph(evt)

def reset_graph(evt) :
    current_plot.data = []
    voltage_plot.data = []
    scene_graph.title = "RLC Circuit Response | MNA solver"


# basic circuits
def simple_rlc(evt) :
    global dragObject
    reset(evt)
    new_resistor(evt)
    dragObject = objects[0]
    dragObject.move(vec(0,3,0)-dragObject.outline.pos)
    drop(evt)
    new_horiz_wire(evt)
    dragObject = objects[1]
    dragObject.move(vec(0,-3,0)-dragObject.outline.pos)
    drop(evt)
    new_capacitor(evt)
    dragObject = objects[2]
    dragObject.move(vec(-10,3,0)-dragObject.outline.pos)
    drop(evt)
    new_inductor(evt)
    dragObject = objects[3]
    dragObject.move(vec(-10,-3,0)-dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[4]
    dragObject.move(vec(-15,0,0)-dragObject.outline.pos)
    drop(evt)
    new_vert_wire(evt)
    dragObject = objects[5]
    dragObject.move(vec(5,0,0)-dragObject.outline.pos)
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


# graph building
def build_edges():
    nodes = []
    for j in range(4):
        row = []
        for i in range(4):
            row.append(Node(i,j))
        nodes.append(row)
    new_edges = []
    for obj in objects:
        if obj.covered_line == None:
            print("All objects must be on the circuit or removed in the trash")
            return None
        if obj.kind=="wire" and obj.direction=="vert":
            col = int((obj.outline.pos.x+15)/10)
            row = int(2-(obj.outline.pos.y+6)/6)
            node1 = nodes[row][col]
            node2 = nodes[row+1][col]
        else:
            col = int((obj.outline.pos.x+10)/10)
            row = int(3-(obj.outline.pos.y+9)/6)
            node1 = nodes[row][col]
            node2 = nodes[row][col+1]
        edge = [node1,node2,obj]
        node1.edges.append(edge)
        node2.edges.append(edge)
        new_edges.append(edge)
    return new_edges


# MNA functions
def node_id(node):
    return node.y*4+node.x

def find_parent(parent,x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_parent(parent,a,b):
    pa = find_parent(parent,a)
    pb = find_parent(parent,b)
    if pa != pb:
        parent[pb] = pa

def wire_groups(edges):
    parent = []
    for i in range(16):
        parent.append(i)
    for edge in edges:
        if edge[2].kind=="wire":
            union_parent(parent,node_id(edge[0]),node_id(edge[1]))
    groups = []
    for i in range(16):
        groups.append(find_parent(parent,i))
    return groups

def build_node_map(edges):
    groups = wire_groups(edges)
    active = []
    for i in range(16):
        active.append(False)
    for edge in edges:
        active[node_id(edge[0])] = True
        active[node_id(edge[1])] = True
    ground_group = None
    for i in range(16):
        if active[i] == True:
            ground_group = groups[i]
            break
    node_map = []
    for i in range(16):
        node_map.append(0)
    if ground_group == None:
        return node_map,0
    next_number = 1
    for i in range(16):
        if active[i] == False:
            node_map[i] = 0
        elif groups[i] == ground_group:
            node_map[i] = 0
        else:
            already_found = False
            for j in range(i):
                if active[j] == True and groups[j] == groups[i]:
                    node_map[i] = node_map[j]
                    already_found = True
            if already_found == False:
                node_map[i] = next_number
                next_number = next_number+1
    return node_map,next_number-1

def add_A(A,r,c,value):
    if r != 0 and c != 0:
        A[r-1][c-1] = A[r-1][c-1]+value

def add_z(z,r,value):
    if r != 0:
        z[r-1] = z[r-1]+value

def stamp_resistor(A,z,n1,n2,R):
    g = 1/R
    add_A(A,n1,n1,g)
    add_A(A,n2,n2,g)
    add_A(A,n1,n2,-g)
    add_A(A,n2,n1,-g)

def stamp_capacitor(A,z,n1,n2,C,old_v,dt):
    g = C/dt
    add_A(A,n1,n1,g)
    add_A(A,n2,n2,g)
    add_A(A,n1,n2,-g)
    add_A(A,n2,n1,-g)
    add_z(z,n1,g*old_v)
    add_z(z,n2,-g*old_v)

def stamp_inductor(A,z,n1,n2,L,old_i,spot,dt):
    if n1 != 0:
        A[n1-1][spot] = A[n1-1][spot]+1
        A[spot][n1-1] = A[spot][n1-1]+1
    if n2 != 0:
        A[n2-1][spot] = A[n2-1][spot]-1
        A[spot][n2-1] = A[spot][n2-1]-1
    A[spot][spot] = A[spot][spot]-L/dt
    z[spot] = z[spot]-(L/dt)*old_i

def voltage(ans,n):
    if n == 0:
        return 0
    return ans[n-1]

def solve_matrix(A,z):
    n = len(z)
    for i in range(n):
        best = i
        for r in range(i+1,n):
            if abs(A[r][i]) > abs(A[best][i]):
                best = r
        A[i],A[best] = A[best],A[i]
        z[i],z[best] = z[best],z[i]
        pivot = A[i][i]
        if abs(pivot) < 0.000000000001:
            return None
        for c in range(i,n):
            A[i][c] = A[i][c]/pivot
        z[i] = z[i]/pivot
        for r in range(n):
            if r != i:
                factor = A[r][i]
                for c in range(i,n):
                    A[r][c] = A[r][c]-factor*A[i][c]
                z[r] = z[r]-factor*z[i]
    return z

def component_current(edge,dt):
    obj = edge[2]
    v = obj.v1-obj.v2
    if obj.kind=="wire":
        return 0
    if obj.kind=="resistor":
        return v/obj.resistance
    if obj.kind=="capacitor":
        return obj.capacitance*(v-obj.old_voltage)/dt
    if obj.kind=="inductor":
        return obj.current
    return 0

def simulate(edges):
    t = 0
    t_max = 3
    dt = 0.0005
    map_data = build_node_map(edges)
    node_map = map_data[0]
    node_count = map_data[1]
    inductors = []
    for edge in edges:
        obj = edge[2]
        obj.v1 = 0
        obj.v2 = 0
        obj.last_current = 0
        if obj.kind=="capacitor":
            obj.old_voltage = obj.voltage
            obj.charge = obj.capacitance*obj.voltage
        if obj.kind=="inductor":
            obj.current = 0
            inductors.append(obj)
    while t < t_max and started==True:
        rate(2000)
        size = node_count+len(inductors)
        A = []
        z = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            A.append(row)
            z.append(0)
        for i in range(node_count):
            A[i][i] = A[i][i]+0.000000000001
        ind_num = 0
        for edge in edges:
            obj = edge[2]
            n1 = node_map[node_id(edge[0])]
            n2 = node_map[node_id(edge[1])]
            if obj.kind=="resistor":
                stamp_resistor(A,z,n1,n2,obj.resistance)
            elif obj.kind=="capacitor":
                stamp_capacitor(A,z,n1,n2,obj.capacitance,obj.old_voltage,dt)
            elif obj.kind=="inductor":
                spot = node_count+ind_num
                obj.ind_spot = ind_num
                stamp_inductor(A,z,n1,n2,obj.inductance,obj.current,spot,dt)
                ind_num = ind_num+1
        ans = solve_matrix(A,z)
        if ans == None:
            print("Matrix could not be solved")
            return None
        for edge in edges:
            obj = edge[2]
            n1 = node_map[node_id(edge[0])]
            n2 = node_map[node_id(edge[1])]
            obj.v1 = voltage(ans,n1)
            obj.v2 = voltage(ans,n2)
            if obj.kind=="inductor":
                obj.current = ans[node_count+obj.ind_spot]
        for edge in edges:
            edge[2].last_current = component_current(edge,dt)
        cap_v = 0
        plotted_voltage = False
        for edge in edges:
            obj = edge[2]
            if obj.kind=="capacitor":
                new_v = obj.v1-obj.v2
                obj.old_voltage = new_v
                obj.charge = obj.capacitance*new_v
                if plotted_voltage == False:
                    cap_v = new_v
                    plotted_voltage = True
        main_i = 0
        plotted_current = False
        for edge in edges:
            obj = edge[2]
            if obj.kind=="inductor" and plotted_current == False:
                main_i = obj.last_current
                plotted_current = True
        if plotted_current == False:
            for edge in edges:
                obj = edge[2]
                if obj.kind!="wire" and plotted_current == False:
                    main_i = obj.last_current
                    plotted_current = True
        current_plot.plot(t,main_i)
        voltage_plot.plot(t,cap_v)
        t = t+dt


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
scene.append_to_caption('\n\n')
scene.append_to_caption('initial capacitor voltage: ')
voltage_slider = slider(bind=set_initial_voltage, min=0, max=30, value=10, length=220)
voltage_text = wtext(text=' initial capacitor voltage = 10 V')
scene.append_to_caption('\n')
scene.append_to_caption('component value: ')
component_value_slider = slider(bind=set_component_value, min=0.001, max=10, value=0.1, length=220)
component_value_text = wtext(text=' component value = 0.1')
scene.append_to_caption(' ')
value_button = button(bind=apply_value,text='apply value to selected component')
scene.append_to_caption(' ')
selected_text = wtext(text='selected component: none')
scene.append_to_caption('\n\n')
simple_loop_button = button(bind=simple_rlc,text="create basic RLC circuit")
scene.append_to_caption('   ')
simple_rc_button = button(bind=simple_rc, text="create basic RC circuit")
scene.append_to_caption('   ')
simple_rl_button = button(bind=simple_rl, text="create basic RL circuit")
scene.append_to_caption('   ')
double_res_button = button(bind=double_resistor_rlc, text="create double resistor RLC")
scene.append_to_caption('\n\n')
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
        simulate(edges)
        print("Simulation finished.")
        stop(None)
    else:
        if dragObject != None:
            newPos = scene.mouse.project(normal=vec(0,0,1))
            shift = newPos-lastPos
            dragObject.move(shift)
            lastPos = newPos
