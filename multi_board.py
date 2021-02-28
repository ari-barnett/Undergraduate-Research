#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:38:40 2021
@author: ajbarnett
Neighbors method - work on integrating into more tomorrow 
"""

import numpy as np
import random 


print('Conways Game of Life')
print('')
r = int(input("Indicate number of rows/columns: "))
desire_turns = int(input("Number of cycles: "))
print('')

grid = []
c = r
n = 0
m = 0
length = r*c
iteration = 0


def find_neighbors(matrix, r, c):
    def get(r, c):
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
            return matrix[r][c]
        else:
            return 0
    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]
    return sum(map(bool, neighbors_list))

#print('INDEX w/ # OF NEIGHBORS')
def update(matrix):
    x = np.array(grid)
    n = 0
    m = 0
    for idx, i in np.ndenumerate(matrix):
        #print((m,n), find_neighbors(x,m,n))
        
        if i == 0 and find_neighbors(matrix,m,n) == 3:
            new[m,n] = 1
        elif i == 1 and find_neighbors(matrix,m,n) in (2,3):
            new[m,n] = 1
        elif i == 1 and find_neighbors(matrix,m,n) >= 4 or find_neighbors(x,m,n) < 2:
            new[m,n] = 0
        else:
            new[m,n] = 0
        
        n = n + 1 
        if (n % c) == 0:
            m = m + 1
            n = n - c
        
    return (new)

for row in range(r):  
    grid.append([])
    for column in range(c):        
        grid[row].append(random.randint(0,1))
        x = np.array(grid)
        
find_neighbors(x,m,n)
new = np.copy(x)

print('ORIGINAL BOARD')
print(x)
print('')


      
print('')  
print('NEW BOARDS')
while (iteration < desire_turns):
    print(iteration + 1)
    print(update(x))
    print('')
    x = np.copy(new)
    iteration = iteration + 1

