#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:34:04 2021

@author: ajbarnett
"""
import matplotlib.pyplot as plt
import random 

def group(x,y,z):
    group_point = [(x[i], y[i], z[i]) for i in range(0, len(x))]
    return group_point

iteration = 0
collusions = 0
non_collusions = 0

while(iteration < 100):
    
    iteration = iteration + 1 
    available_particles = 1000 #total number of particles available - number of potential collusions is // 2. 
    figure = plt.figure()
    model = figure.add_subplot(111, projection='3d')
    
    model.grid(b = True, color ='black', 
        linestyle ='-', linewidth = 0.5, 
        alpha = 0.5)
    
    #Representing Na ions within aq solution
    x = [random.gauss(0, 1000) for i in range(available_particles)]
    y = [random.gauss(0, 1000) for i in range(available_particles)]
    z = [random.gauss(0, 1000) for i in range(available_particles)]
    
    #Representing Cl ions within aq solution
    x2 = [random.gauss(0, 1000) for i in range(available_particles)]
    y2 = [random.gauss(0, 1000) for i in range(available_particles)]
    z2 = [random.gauss(0, 1000) for i in range(available_particles)]
    
    
    model.scatter(x, y, z, c= 'green', marker='o', s=0.102)
    model.scatter(x2, y2, z2, c= 'orange', marker='o', s=0.181)
    plt.title("SIMULATION NUMBER")
    plt.suptitle(iteration)
    
    model.xaxis.set_tick_params(labelsize=1)
    model.yaxis.set_tick_params(labelsize=1)
    model.zaxis.set_tick_params(labelsize=1)
    
    model.set_xticklabels([])
    model.set_yticklabels([])
    model.set_zticklabels([])
    
    
    model.set_xlabel('x-axis bounds', fontsize=10)
    model.set_ylabel('y-axis bounds', fontsize=10)
    model.set_zlabel('z-axis bounds', fontsize=10)

    plt.show()
    
    
else:
    print("End of Simulation")
    
    res_listx = [] 
    res_listy = []
    res_listz = []
    output_list = []
    
    for i in range(0, len(x)):
        
        res_listx.append(x[i] - x2[i])
        res_listy.append(y[i] - y2[i])
        res_listz.append(z[i] - z2[i])
        
        output_list.append(res_listx[i] + res_listy[i] + res_listz[i])
    
    for i in range(0, len(output_list)):
        if -100 < output_list[i] < 100:
            collusions = collusions + 1 
            
print("The number of collusions are: ", collusions)  
print("The number of non_collusions are: ", 150 - collusions)

"""
© Ari Barnett - Undergraduate Research; St. Petersburg College 2021

""" 




    
