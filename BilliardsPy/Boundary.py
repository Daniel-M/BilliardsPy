#!/usr/bin/python

class Boundary:
    'Main class to define billiard table boundary objects'

    def __init__(self,name,function,parameters):
        self.Name=name
        self.Function=function
        self.Parameters=parameters

    def __str__(self):
        return self.Name

    def getFunction(self):
        return self.function
    
    def getParameters(self):
        return self.Parameters

    def evaluate(self,*arguments):
        return self.Function(self.Parameters,*arguments)
