# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:15:19 2020

@author: shivendra
"""


class Rect: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  

def check(lcord1, lcord2, rcord1, rcord2): 
      
   # if one rectangle left of the other
    if(lcord1.x >= rcord2.x or lcord2.x <= rcord1.x): 
        return False
  
    # if one rectangle top of the other
    if(lcord1.y >= rcord2.y or lcord2.y <= rcord1.y): 
        return False
  
    return True
  

if __name__ == "__main__": 
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    lcord1 = Rect(rec1[0],rec1[1])
    lcord2 = Rect(rec1[2],rec1[3])
    rcord1 = Rect(rec2[0],rec2[1])
    rcord2 = Rect(rec2[2],rec2[3])
  
    if(check(lcord1, lcord2, rcord1, rcord2)): 
        print("True") 
    else: 
        print("False") 