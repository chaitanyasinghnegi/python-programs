"""
This file is a simple program that 
pseudo-randomizes integers between two given intervals, 
using the linear congruential algorithm with variable seeds 
using time, date, os files etc.
"""

import os
import time

class GenerateRandom:
    def __init__(self,a=48271,c=0,m=2**31-1,seed=None):
        self.a=a
        self.c=c
        self.m=m
        
        if seed is None:
            self.x0=int(os.getpid()+time.time())
        else:
            self.x0=seed
        
        self.x1 = (self.a * self.x0 + self.c) % self.m
        
    def random_gen(self,rangeGiven=None):
        self.x1 = (self.a * self.x1 + self.c) % self.m
        
        if rangeGiven is None:
            return self.x1
        else:
            return int(( self.x1 / (self.m-1 )) * (rangeGiven[1] - rangeGiven[0]) + rangeGiven[0])
        
genRandom = GenerateRandom()

start = int(input("Enter start of range : "))
end = int(input("Enter end of range : "))

num = int(input("Enter how many numbers you want : "))

for i in range(num):
    print(genRandom.random_gen([start,end]))
    
