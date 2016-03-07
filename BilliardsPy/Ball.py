#!/usr/bin/python
import random

class Ball:
    'Main class to define billiard balls objects'

    def __init__(self,mass,radious,position,velocity):
        self.Mass=mass
        self.Radious=radious
        self.Position=position
        self.Velocity=velocity

    def __str__(self):
        return "Ball mass: %f" % (self.Mass)

    def getMass(self):
        return self.Mass

    def getPosition(self):
        return self.Position
    
    def getVelocity(self):
        return self.Velocity

    def move(self,delta):
        random.seed()
        variation =  random.uniform(-0.1*delta,0.1*delta)
        self.Position = self.Position + delta*self.Velocity + variation

    def reverseVelocity(self,component):
        random.seed()
        variation = random.uniform(-0.01*self.Velocity[component],0.01*self.Velocity[component])
        self.Velocity[component] = -1.0*self.Velocity[component] + variation

    def collide(self,limits):
        if( 0 >= self.Position[0]+self.Radious):
            self.reverseVelocity(0)
        elif(self.Position[0]+self.Radious >= limits[0]):
            self.reverseVelocity(0)
        elif( 0 > self.Position[1]+self.Radious):
            self.reverseVelocity(1)
        elif(self.Position[1]+self.Radious >= limits[1]):
            self.reverseVelocity(1)

    def checkState(self,bBoundary):
        result = bBoundary.evaluate(self.Position)
        return result 
    
    #def checkBoundary(self,funcionFrontera,*argumentos):
        #return funcionFrontera(*argumentos)
