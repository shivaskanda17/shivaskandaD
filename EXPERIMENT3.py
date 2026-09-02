# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:12:35 2026

@author: user
"""

s ="Hello python"
print("original string:",s)

print("length:",len(s))

print("uppercase:", s.upper())

print("lowercase:", s.lower())

print("character at index 6:",s[6])

print("position of python:", s.find("python"))
    
print("slice:",s[6:])

print("replace:", s.replace("python","world"))
print(s)

print("contains python:","python" in s)

print("concatenation:", s +" programming")

s2 ="hello python "
print("trim:",s2.strip())
