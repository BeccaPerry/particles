#compute all the rigid shapes for a given number of
#particles on a given grid

#start with:
#spherical particles on a hexagonal lattice

#correct numbers of clusters:
'''
n = 1, 1 
n = 2, 1
n = 3, 1
n = 4, 1
n = 5, 1
n = 6, 3
n = 7, ?
'''

#nxn choose any n
#check sum of adjacency matrix to check rigidity
#check that this rigid adjacency matrix has not been found already

#too slow?
rshapes(n, lattice='hexagonal'):

    return shapes #list of shapes where each shape is a set of (x,y) coordinates
    #and no two have the same adjacency matrix
