#Determine the adjacency matrix for an input of particle coordinates.
#Matrix will have 1's for particles that are adjacent and 0's for
#those that are not adjacent. The diagonal has 0's by definition.
#Input: rows and columns (must be same length) and a cutoff distance
#below which particles are considered adjacent.

#Rebecca W. Perry
#5/30/2013

import numpy as np

'''
rows = np.array([ 13.30440646,  14.62345577,  15.93533988,  12.50255448,
        13.81666774,  15.13362928])

cols = np.array([ 19.60213683,  19.43949687,  19.25496336,  18.51739021,
        18.34397836,  18.17318798])

distance = 1.4
'''

def adj(x_coords, y_coords, distance_limit):
    num = len(x_coords) #determine the number of particles
    assert len(y_coords) == num

    dist = np.zeros([num,num]) #initialize the distance matrix

    #zeros along diagonal, compute upper right half of symmetrical matrix
    for i in range(0,num):
        for j in range(i+1,num):
            dist[i,j] = dist[j,i] = np.hypot(x_coords[i]-x_coords[j], 
            y_coords[i]-y_coords[j])

    return ((dist > 0) & (dist < distance_limit)).astype('int')
