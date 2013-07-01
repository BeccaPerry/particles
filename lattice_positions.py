#There should be quicker ways to compute these
#lattice positions, but this way is easy to read
#and easy to adapt to different lattices.

#eg:
#coords = squareLattice(1.3,100,100)
#figure(); plot(coords[:,0],coords[:,1],'ro')

def sqLattice(const, rows, cols):
    '''
    const: spacing between closest two points
    rows, cols: number of rows and columns of points requested
    '''
    coords = zeros([rows*cols, 2])

    k = 0
    for i in range(0,rows):
        for j in range(0,cols):
            coords[k,0] = i
            coords[k,1] = j 
            k += 1
    return coords

def hexLattice(const, rows, cols):
    '''
    const: spacing between closest two points
    rows, cols: number of rows and columns of points requested
    '''
    coords = zeros([rows*cols,2])

    k = 0
    for i in range(0,rows):
        for j in range(0,cols):
            if j%2==0:
                coords[k,0] = i +.5 #shifted every other row
            else:
                coords[k,0] = i
            coords[k,1] = sqrt(3)/2.0*j 
            k += 1  
    return coords
