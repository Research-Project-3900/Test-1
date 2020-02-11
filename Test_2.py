from vpython import *
from math import *


#Defining a charged 0article
p1 = sphere(pos = vector(0, 5, 0), radius = 0.5, color = color.red,
            vel = vector(5, 0, 0), mass = 1, charge = 1,
            make_trail = True, trail_color = color.yellow, retain = 150)

#wall = box(pos = vector(0, 0, 0,), size = vector(10, 10, 0.2), color = color.blue)

#Defining Fields
e_field = vector(0, 0, 0)
b_field = vector(0, 0, 1)

mField = arrow(pos = vector(0, 0, 0), axis = b_field, length = 1, color = color.yellow)
#Defining a force function
def force(particle):
    return particle.charge * (e_field + cross(particle.vel, b_field))

#Adding a track

#updating positions and velocities
accel = force(p1)/p1.mass # Newtons 2nd Law
dt = 0.001 #Time Interval
while True: #p1.pos.x > -0.01:
    rate(1000) #Per Second

    p1.pos = p1.pos + p1.vel*dt
    p1.vel = p1.vel + accel*dt
    #Newton's 2nd Law again
    accel = force(p1)/p1.mass
    
print("Acceleration: ", accel)
print("Force: ",force(p1))