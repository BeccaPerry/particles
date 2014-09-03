#for plt.plotting all the colorings of a 6 particle triangle
#the checks for symmetry are hard coded in for this particular shape

import itertools as it
import numpy as np
import matplotlib.pyplot as plt


#the coordinates of the particles in the ground state clusters
bigTri_coords = np.array([
       [0,4*np.sqrt(3)/6.,0],
       [.5,np.sqrt(3)/6.,0],
       [1,-2*np.sqrt(3)/6,0],
       [0,-2*np.sqrt(3)/6.,0],
       [-1,-2*np.sqrt(3)/6.,0],
       [-.5,np.sqrt(3)/6.,0]])

parl_coords = np.array([
       [-1.25,np.sqrt(3)/4.,0],
       [-.25,np.sqrt(3)/4.,0],
       [.75,np.sqrt(3)/4.,0],
       [-.75,-np.sqrt(3)/4.,0],
       [.25,-np.sqrt(3)/4.,0],
       [1.25,-np.sqrt(3)/4.,0]])

che_coords = np.array([
       [np.sqrt(3)/2.,2/3.,0],
       [-np.sqrt(3)/2.,2/3.,0],
       [0,-5/6.,0],
       [0,1/6.,0],
       [np.sqrt(3)/2.,-1/3.,0],
       [-np.sqrt(3)/2.,-1/3.,0]]) 


#colors =['ro','bo','go','co','ko','mo']

colors= ['#e41a1c',
'#377eb8',
'#4daf4a',
'#984ea3',
'#ff7f00',
'#ffff33']

thiscoloring= ['a','b','c','d','e','f']

colorings = []

l = it.permutations(range(6))

i = -1
plt.figure(figsize=[22,12],facecolor='black') #black background good for presentations
ax = plt.axes([0,0,1,1])
ax.set_axis_bgcolor('black')
bad = 0

for k in range(720): #check all 6 factorial colors

    #get a new permutaion
    permutation = l.next()

    for c in range(6):
        thiscoloring[c] = colors[permutation[c]]

    #check if this permutation has been used before
    if thiscoloring[2:]+thiscoloring[0:2] not in colorings: #rotation by 120 degrees (triangle specific)
        if thiscoloring[4:]+thiscoloring[0:4] not in colorings: #rotation by 240 degrees (triangle specific)

            i = i+1
            #found a good one, so add to the list of found colorings
            colorings.append(list(np.copy(thiscoloring)))

            for j in range(6):
              print 'plotting'
              print thiscoloring[j]
              plt.plot(bigTri_coords[j,0]+np.mod(4*i,80), bigTri_coords[j,1]+i/20*4,markerfacecolor=thiscoloring[j], marker='o',markeredgecolor='black', markersize=20)

            if thiscoloring[0:1]+thiscoloring[5:]+thiscoloring[4:5]+thiscoloring[3:4]+thiscoloring[2:3]+thiscoloring[1:2] in colorings:
                print thiscoloring[0:1]+thiscoloring[5:]+thiscoloring[4:5]+thiscoloring[3:4]+thiscoloring[2:3]+thiscoloring[1:2]
                bad = bad+1
                for j in range(6):
                    plt.plot(bigTri_coords[j,0]+np.mod(4*i,80), bigTri_coords[j,1]+i/20*4,markerfacecolor='black',marker='o', markeredgecolor='black', markersize=20)

plt.ylim(-2,46)
plt.xlim(-2,78)
plt.show()


'''
#code I used to plot single examples of the three shapes

#a single parallelogram
plt.figure();
ax = plt.axes([0,0,1,1])
ax.set_axis_bgcolor('black')

for j in range(6):
    print j
    plt.plot(parl_coords[j,0], parl_coords[j,1],'o',markerfacecolor=[.8,.8,.8], markeredgecolor='black', markersize=145)
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-1.25,1.75)

#a single chevron
plt.figure();
ax = plt.axes([0,0,1,1])
ax.set_axis_bgcolor('black')

for j in range(6):
    print j
    plt.plot(che_coords[j,0], che_coords[j,1],'o',markerfacecolor=[.8,.8,.8], markeredgecolor='black', markersize=145)
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-1.5,1.75)

#a single triangle
plt.figure();
ax = plt.axes([0,0,1,1])
ax.set_axis_bgcolor('black')

for j in range(6):
    print j
    plt.plot(bigTri_coords[j,0], bigTri_coords[j,1],'o',markerfacecolor=[.8,.8,.8], markeredgecolor='black', markersize=145)
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-1.25,1.75)


#a single colored triangle
colors= ['#e41a1c',
'#377eb8',
'#4daf4a',
'#984ea3',
'#ff7f00',
'#ffff33']

plt.figure();
ax = plt.axes([0,0,1,1])
ax.set_axis_bgcolor('black')

for j in range(6):
    print j
    plt.plot(bigTri_coords[j,0], bigTri_coords[j,1],'o',markerfacecolor=colors[j], markeredgecolor='black', markersize=145)
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-1.25,1.75)'''