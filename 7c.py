# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:37:27 2026

@author: user
"""

class Mtd:
    def Fun(self,a,b):
        print("this is with two arguments program")
        print(a + b)
        
ovr = Mtd()
ovr.Fun(3,9)
ovr.Fun(3.9, 5.9)
ovr.Fun("hi","bye")
ovr.Fun("welcome","python")
ovr.Fun(366,9234)
ovr.Fun(3433.9, 5344.9)

o/p
this is with two arguments program
12
this is with two arguments program
9.8
this is with two arguments program
hibye
this is with two arguments program
welcomepython
this is with two arguments program
9600
this is with two arguments program
8778.8
