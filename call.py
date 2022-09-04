# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:42:05 2022

@author: 唐琪登
"""

class Student:
    
    def __init__(self, name):
         self.name = name
        
    def __call__(self, age):
        print(self.forward())
    
    def forward(self):
        return self.name + "Mr"
        
xiaoming = Student('xiaoming')
xiaoming(10)
