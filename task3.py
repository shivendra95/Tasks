# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:43:12 2020

@author: shivendra
"""


s = 'barfoothefoobarman'
words = ['foo','bar']

res = [] 
dc = dict()

size = len(words[0]) 
count_word = len(words) 
size_words = size * count_word 

# creating dictionary to keep count of every word present  
for i in range(count_word): 
        if words[i] in dc: 
            dc[words[i]] += 1
        else: 
            dc[words[i]] = 1
            
for i in range(0, len(s) - size_words + 1, 1): 
        temp_dc = dc.copy() 
        j = i 
        count = count_word 
  
     
        while j < i + size_words: 
                
            word = s[j:j + size] # word extracted 
  
            if (word not in dc or 
                temp_dc[word] == 0): 
                break
           
            else: 
                temp_dc[word] -= 1 # decreasing the counter for words
                count -= 1
            j += size_words
 
        if count == 0: 
            res.append(i)    
            
print(res)            