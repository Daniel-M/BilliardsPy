#!/usr/bin/python

from Ball import Ball
from Boundary import Boundary

import random
import math
import numpy as np

def ellipseBound(parameters,coordinates):
    value = (coordinates[0]*coordinates[0])/(parameters[0]*parameters[0])+(coordinates[1]*coordinates[1])/(parameters[1]*parameters[1])
    if (value < 1):
        return True 
    else:
        return False



limits=np.array([10,7])
p= np.array([0.1,0.1])
v= np.array([1,0.3])


params = np.array([2,1])

b1 = Ball(1,1,p,v)
boundary = Boundary("Ellipse",ellipseBound,params)

dt=0.1
t=0

print ("#t position velocity")
while t < 2500:
    b1.move(dt)
    #b1.collide(limits)
    b1.checkState(boundary)
    print (str(t) + " " + str(b1.getPosition()) + " " + str(b1.getVelocity()) + " " + str(b1.checkState(boundary)))
    t+=dt;
