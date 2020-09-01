# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:40:42 2020

@author: shivendra
"""


def partition(S):
        last = {}
        c = 0
        for i in S:
            last[i] = c
            c+=1 #creating last index for all characters
       
        j = 0 
        end = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c]) #updating last index of partition if changed 
            if i == j:
                ans.append(i - end + 1)
                end = i + 1
            
        return ans
    
    
s = 'ababcbacadefegdehijhklij'  
x= partition(s)
print(x)
