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

#helix(pos=vec(-5,0,0),axis=vec(10,0,0),color=color.red,coils=20)
