# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:13:25 2026

@author: user
"""
import re

data = input("Enter Email or Mobile Number: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[0-9]{10}$'

if re.fullmatch(email_pattern, data):
    print("Valid email ID")

elif re.fullmatch(mobile_pattern, data):
    print("Valid mobile number")

else:
    print("Invalid Email or Mobile Number")900875