# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:56:37 2026

@author: user
"""

class Base:
    def show(self):
        print("statement from base class")
        
class Derived(Base):
     def show(self):
         super().show()
         print("statemnt from derived class")
         
         
ob=Derived()
ob.show()
ob.show()        

o/p
statement from base class
statemnt from derived class
statement from base class
statemnt from derived class
