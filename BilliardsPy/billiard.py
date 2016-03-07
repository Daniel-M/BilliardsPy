#!/usr/bin/python

from Ball import Ball
import random
import math
import numpy as np

limits=np.array([10,7])
p= np.array([0.1,0.1])
v= np.array([1,0.3])

b1 = Ball(1,1,p,v)

dt=0.1
t=0

print "#t position velocity"
while t < 2500:
    b1.move(dt)
    b1.collide(limits)
    print str(t) + " " + str(b1.getPosition()) + " " + str(b1.getVelocity())
    t+=dt;
