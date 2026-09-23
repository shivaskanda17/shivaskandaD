# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:29:16 2026

@author: user
"""

t = (10,20,30,20,40)
print("Tuple:",t)
print("First element:",t[0])
print("last element:",t[-1])

print ("Length:",len(t))


print("count of 20:",t.count(20))

print("Index of 30:",t.index(30))

print("Maximum:",max(t))
print("Minimum:",min(t))
print("Sum:",sum(t))
print("is 40 present?",40 in t)

l = list(t)
print("Tuple coverted to list:",l)

t2 = tuple(l)
print ("List converted to tuple:", t2)

O/P
Tuple: (10, 20, 30, 20, 40)
First element: 10
last element: 40
Length: 5
count of 20: 2
Index of 30: 2
Maximum: 40
Minimum: 10
Sum: 120
is 40 present? True
Tuple coverted to list: [10, 20, 30, 20, 40]
List converted to tuple: (10, 20, 30, 20, 40)

