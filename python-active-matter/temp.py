#!/usr/bin/python

from visual import *   # visual also imports numpy
from numpy.random import *
import sys
import ConfigParser
#from evdev import uinput, ecodes as e
from time import time

t0 = time()

if len(sys.argv) != 2:
    # print >> sys.stderr, "Usage: SPP.py config.ini"
    # sys.exit(1)
    parfile = "alignment.txt";
if len(sys.argv) == 2:
    parfile = sys.argv[1] # 'parameters.ini' # 
C = ConfigParser.ConfigParser()
C.optionxform = str
C.read(parfile)

for section in C.sections():
	for par in C.options(section):
		print >> sys.stderr, par+'='+C.get(section,par)
		exec par+'='+C.get(section,par)


##### boundary conditions #####

def enforce_boundary(p):  # enforce the boundary for particle p
	if periodic_x:
		p.pos.x -= Lx*rint(p.pos.x/Lx)
	elif abs(p.pos.x)>0.5*Lx:
		p.pos.x = copysign(0.5*Lx,p.pos.x)
	if periodic_y:
		p.pos.y -= Ly*rint(p.pos.y/Ly)
	elif abs(p.pos.y)>0.5*Ly:
		p.pos.y = copysign(0.5*Ly,p.pos.y)  # wall along y
	if wedge:	enforce_wedge(p)
	
u1  = vector(1,w_s)/sqrt(1+w_s**2)   # unit vector along the left wall
u2  = vector(1,-w_s)/sqrt(1+w_s**2)  # unit vector along the right wall
u1p = vector(-u1.y,u1.x)             # unit vector perpendicular to u1
u2p = vector(-u2.y,u2.x)             # unit vector perpendicular to u2
v_tip = vector(0,0.25*Lx*w_s)        # position of the upper tip of the wedge

def wedge_eqn(x):
	return ( 0.25*Lx - abs(x) ) * w_s

def enforce_wedge(p):
	side = ( p.pos.y>wedge_eqn(p.pos.x) )
	if ( side == p.side ) or ( abs(p.pos.x) < w_dx ) :
		# if the particle stayed on the same side of the wedge, 
		# or went through the opening, just update 'self.side'
		p.side = side
		p.S.color = (1,0,0) if side else (0,0,1)
	else:
		# otherwise, block it
		u = u1 if p.pos.x<0 else u2
		p.pos = v_tip + u * dot(p.pos-v_tip,u)


##### boundary drawing #####

w = 2e-3 * min(Lx,Ly)  # boundary width


# draw the rectangular box
lx = 0.5*Lx; ly=0.5*Ly
cylinder(pos=(-lx,-ly),axis=( 0, Ly),radius=w)
cylinder(pos=(-lx, ly),axis=( Lx, 0),radius=w)
cylinder(pos=( lx, ly),axis=( 0,-Ly),radius=w)
cylinder(pos=( lx,-ly),axis=(-Lx, 0),radius=w)

# draw the wedge if present
if wedge:
	w = 1e-3 * min(Lx,Ly)
	x  = 0.5*Lx
	y  = 0.25*Lx*w_s
	ux = x-w_dx
	cylinder(pos=(-x,-y),axis=( ux,w_s*ux),radius=w)
	cylinder(pos=( x,-y),axis=(-ux,w_s*ux),radius=w)


##### evaluation of forces and torques #####
	##### evaluation of forces and torques #####

def get_neighbors(particles):
	global Lx,Ly,R
	X,Y = array([p.pos for p in particles]).T[0:2]
	dX = X[:,None]-X[None,:]
	dY = Y[:,None]-Y[None,:]
	if periodic_x:	dX -= rint(dX/Lx)
	if periodic_y:	dY -= rint(dY/Ly)
	d = hypot(dX,dY)
	I,J = nonzero(d<R)
	i = nonzero(I!=J)
	I,J = I[i], J[i]
	return [J[nonzero(I==i)] for i in range(N)],I,J,dX,dY,d

def get_torques(NL):
	global particles
	for i in range(N):
		if len(NL[i])==0:
			particles[i].torque = 0
		else:
			da = atan2(*array([p.dir for p in particles[NL[i]]]).mean(axis=0)[0:2][::-1]) - particles[i].ang
			da -= 2*pi*round(0.5*da/pi)
			particles[i].torque = da/tau

def get_forces(I,J,dX,dY,d):
	global particles
	forces = zeros((N,N,2))
	forces[I,J] = k*vstack((dX[I,J],dY[I,J])).T
	forces[I,J] *= 1 - R / vstack((d[I,J],d[I,J])).T
	forces = sum(forces,axis=0)
	for i in range(N):
		particles[i].force = vector(forces[i])

class Particle:
	# Properties of a particle:
	# pos = particle's position
	# dir = particle's orientation
	# ang = angle between dir and x axis
	# force, torque
	# side = which side of the wedge the particle is on
	# S,A = sphere and arrow for visualization
	
	def draw(self):
		global Ra, alignment
		self.S.pos  = self.pos
		self.A.pos  = self.pos
		self.A.axis = La*self.dir
		if alignment:
			self.S.color = color.hsv_to_rgb((0.5*self.ang/pi,0.8,0.9))
			self.A.color = color.hsv_to_rgb((0.5*self.ang/pi,0.8,0.9))
	
	def update(self):
		global sig, sig_r, dt, r
		self.pos += dt * v0 * self.dir + dt * self.force + sig * vector(randn(2))
		self.ang += dt * self.torque + sig_r * randn()
		enforce_boundary(self)
		self.dir = vector(cos(self.ang),sin(self.ang))


particles=empty((N,),dtype=type(Particle()))
for i in range(N):
	p = Particle()                                             # create a new particle
	p.pos = vector(Lx*(rand()-0.5),Ly*(rand()-0.5))                    # pick a random position in the box
	p.ang = 2*pi*rand()                                        # pick a random angle in [0,2*pi]
	p.dir = vector(cos(p.ang),sin(p.ang))
	p.side = (p.pos.y > wedge_eqn(p.pos.x))
	# create the graphical representation: a sphere + a cone to indicate orientation
	c = color.hsv_to_rgb((float(i)/N,0.8,0.9))
	p.S = sphere(pos=p.pos,radius=Rs,color=c,opacity=Os)
	p.A = cone(pos=p.pos,radius=Ra,axis=La*p.dir,color=c,opacity=Oa,visible=(v0>0))
	p.force = vector(0,0)
	p.torque = 0
	particles[i] = p
# density profile initialization
if output == 'density_profile':
#	bins = linspace(-0.5*Ly-dy,0.5*Ly+dy,int(Ly/dy))
	bins = linspace(-0.5*Ly,0.5*Ly,int(Ly/dy))
	Y = array([p.pos.y for p in particles])
	density_profile = histogram(Y,bins=bins)[0]


##### iteration of the equations of motion #####

n_steps = int(tsim/dt)
n_print = int(tprint/dt)
n_draw  = int(tdraw/dt)
f = open(output_file,'w')

for i in range(n_steps):
	t = i*dt
	if repulsion or alignment:	NL,I,J,dX,dY,d = get_neighbors(particles)
	if alignment:	get_torques(NL)
	if repulsion:	get_forces(I,J,dX,dY,d)
	for p in particles:	p.update()
	if i % n_draw == 0:
		for p in particles:	p.draw()
		if frame_rate:	rate(frame_rate)
	
	if output == 'density_profile':
		Y = array([p.pos.y for p in particles])
		density_profile += histogram(Y,bins=bins)[0]
	
	if i % n_print == 0:
		if output == 'above_wedge':
			s = '%g     %g' % ( t, len([p for p in particles if p.side])/float(N) )
		if output == 'orientation':
			v = array([p.dir for p in particles]).mean(axis=0)
			s = '%g     %g' % ( t, hypot(v[0],v[1]) )
		if output == 'density_profile':
			s = '  '.join(map(str, density_profile*dt/(t+dt)))
		print s
		

f.close()


print 'duration: %g' % (time()-t0)




