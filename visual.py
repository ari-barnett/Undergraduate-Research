#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:38:40 2021
@author: ajbarnett
institution: St. Petersburg College (Spring 2021)
"""

import numpy as np
import random 
from matplotlib import pyplot, colors


print('Conways Game of Life')

'''
Conways Game of Life Rules:

1. If a cell is inactivated and has 3 neighbors - the cell will then become activated
2. If a cell is activated and has 2 or 3 neighbors - the cell will remain activated
3. If a cell is inactive or activated and has more than 3 or less than 2 neighbors - the cell will become or remain inactive
''' 

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
colormap = colors.ListedColormap(["white","black"])

'''
For the find neighbors method, for the numpy array that is given (x) the idx values are grabbed and a sequence of 
"movements" are performed performed in order to create a list of 0's and 1's in order to return the sum. This is performed for
each index value on the user-designated board. 
'''
def find_neighbors(matrix, r, c):
    def get(r, c):
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
            return matrix[r][c]
        else:
            return 0
    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]   
    return sum(neighbors_list)
'''===================================================================================================================='''

'''
The update matrix method pulls the previously found neighbor information and runs each index through the set of rules for 
the game of life. Since the idx call is not indivdual integers - I implemented a basic count for the desired index values. The 
updated values of each index are then placed in a new array called "new". 
'''

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
'''===================================================================================================================='''

'''
Generation of inital game board x and establishment of updated game board new. 
'''
for row in range(r):  
    grid.append([])
    for column in range(c):        
        grid[row].append(random.randint(0,1))
        x = np.array(grid)
        x_ori = np.array(grid)
find_neighbors(x,m,n)
new = np.copy(x)

'''===================================================================================================================='''

'''
Display of the inital game board.
'''

print('ORIGINAL BOARD:')
print('')
print(x)
pyplot.figure(figsize=(10,10))
pyplot.imshow(new, cmap = colormap, interpolation='nearest')
pyplot.title("Original Board")
pyplot.axis('off')
pyplot.grid()

pyplot.show()
print('')

'''===================================================================================================================='''

'''
Display of each subsequent updated generation board - dependent on the number of cycles specified.
'''
   
print('')  
print('NEW BOARDS:')
print('')
while (iteration < desire_turns):
    
    print('Update', iteration + 1)
    print(update(x))
    update(x)
    pyplot.figure(figsize=(8,8))
    pyplot.imshow(new, cmap = colormap, interpolation='nearest')
    pyplot.title(iteration + 1)
    pyplot.axis('off')

    pyplot.show()
    print('')
    
    x = np.copy(new)
    iteration = iteration + 1
