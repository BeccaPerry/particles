Rebecca W. Perry
Sept. 3, 2014

import numpy as np
import matplotlib.pyplot as plt

#set the colors to be used for sphere types A and B
#my experiments used silica and polystyrene
pscolor = [186/256.,186/256.,186/256.]
silicacolor = [213/256.,62/256.,79/256.]


def adj_binary(x_coords, y_coords, material, distance_limit):
    num = len(x_coords) #determine the number of particles
    assert len(y_coords) == num
    assert len(material) == num

    dist = np.zeros([num,num]) #initialize the distance matrix
    material_pair = np.zeros([num,num]) #initialize the pair material matrix

    #zeros along diagonal, compute upper right half of symmetrical matrix
    for i in range(0,num):
        for j in range(i+1,num):
            dist[i,j] = dist[j,i] = np.hypot(x_coords[i]-x_coords[j], 
            y_coords[i]-y_coords[j])
            material_pair[i,j] = material_pair[j,i] = 1 + material[i] + material[j]

    return ((dist > 0) & (dist < distance_limit)).astype('int')*material_pair, dist


#############################################
# One
#############################################

x = np.array([0])
y = np.array([0])

clusterlayouts = [[1],[0]]


t = []
for material in clusterlayouts:
    a = adj_binary(x, y, material, 1.1)
    metric = list(np.sort(a[0].sum(1)))
    integerslist = [int(m) for m in metric]
    t.append(integerslist)


plt.figure(figsize=[10,5]); 
j = 0
for i in clusterlayouts:
    j+=1
    plt.subplot(2,5,j,aspect='equal')
    plt.title(str(j-1)+') \n'+str(i)+'\n'+ str(t[j-1]))
    plt.plot(np.array(x-x.mean())[np.array(i)==0],np.array(y-y.mean())[np.array(i)==0],'o',color=silicacolor,markersize=32,markeredgecolor=silicacolor)
    plt.plot(np.array(x-x.mean())[np.array(i)==1],np.array(y-y.mean())[np.array(i)==1],'o',color=pscolor,markersize=32,markeredgecolor=pscolor)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.xticks([])
    plt.yticks([])


#############################################
# Two
#############################################

x = np.array([-.5,.5])
y = np.array([0,0])

clusterlayouts = [
[1,1],
[0,1],
[0,0],
]

t = []
for material in clusterlayouts:
    a = adj_binary(x, y, material, 1.1)
    metric = list(np.sort(a[0].sum(1)))
    integerslist = [int(m) for m in metric]
    t.append(integerslist)


plt.figure(figsize=[10,5]); 
j = 0
for i in clusterlayouts:
    j+=1
    plt.subplot(2,5,j,aspect='equal')
    plt.title(str(j-1)+') \n'+str(i)+'\n'+ str(t[j-1]))
    plt.plot(np.array(x-x.mean())[np.array(i)==0],np.array(y-y.mean())[np.array(i)==0],'o',color=silicacolor,markersize=32,markeredgecolor=silicacolor)
    plt.plot(np.array(x-x.mean())[np.array(i)==1],np.array(y-y.mean())[np.array(i)==1],'o',color=pscolor,markersize=32,markeredgecolor=pscolor)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.xticks([])
    plt.yticks([])


#############################################
# Three
#############################################

x = np.array([-.5,.5,0])
y = np.array([0,0,np.sqrt(3)/2.])

clusterlayouts = [
[1,1,1],
[0,1,1],
[1,0,0],
[0,0,0],
]

t = []
for material in clusterlayouts:
    a = adj_binary(x, y, material, 1.1)
    metric = list(np.sort(a[0].sum(1)))
    integerslist = [int(m) for m in metric]
    t.append(integerslist)


plt.figure(figsize=[10,5]); 
j = 0
for i in clusterlayouts:
    j+=1
    plt.subplot(2,5,j,aspect='equal')
    plt.title(str(j-1)+') \n'+str(i)+'\n'+ str(t[j-1]))
    plt.plot(np.array(x-x.mean())[np.array(i)==0],np.array(y-y.mean())[np.array(i)==0],'o',color=silicacolor,markersize=32,markeredgecolor=silicacolor)
    plt.plot(np.array(x-x.mean())[np.array(i)==1],np.array(y-y.mean())[np.array(i)==1],'o',color=pscolor,markersize=32,markeredgecolor=pscolor)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.xticks([])
    plt.yticks([])


#############################################
# Four
#############################################

x = np.array([-.5,.5,0,0])
y = np.array([0,0,np.sqrt(3)/2.,-np.sqrt(3)/2.])

clusterlayouts = [
[1,1,1,1],
[0,1,1,1],
[1,1,0,1],
[0,0,1,1],
[1,1,0,0],
[0,1,0,1],
[1,0,0,0],
[0,0,1,0],
[0,0,0,0]
]

t = []
for material in clusterlayouts:
    a = adj_binary(x, y, material, 1.1)
    metric = list(np.sort(a[0].sum(1)))
    integerslist = [int(m) for m in metric]
    t.append(integerslist)


plt.figure(figsize=[10,5]); 
j = 0
for i in clusterlayouts:
    j+=1
    plt.subplot(2,5,j,aspect='equal')
    plt.title(str(j-1)+') \n'+str(i)+'\n'+ str(t[j-1]))
    plt.plot(np.array(x-x.mean())[np.array(i)==0],np.array(y-y.mean())[np.array(i)==0],'o',color=silicacolor,markersize=32,markeredgecolor=silicacolor)
    plt.plot(np.array(x-x.mean())[np.array(i)==1],np.array(y-y.mean())[np.array(i)==1],'o',color=pscolor,markersize=32,markeredgecolor=pscolor)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.xticks([])
    plt.yticks([])


#############################
# Five
#############################
x = np.array([-1,0,1,-.5,.5])
y = np.array([0,0,0,-np.sqrt(3)/2.,-np.sqrt(3)/2.])

clusterlayouts = [
[1,1,1,1,1],
[1,1,1,0,1],
[0,1,1,1,1],
[1,0,1,1,1],
[1,1,1,0,0],
[0,1,0,1,1],
[0,1,1,0,1],
[0,1,1,1,0],
[0,0,1,1,1],
[1,0,1,0,1],
[0,0,0,1,1],
[1,0,1,0,0],
[1,0,0,1,0],
[1,0,0,0,1],
[1,1,0,0,0],
[0,1,0,1,0],
[0,0,0,1,0],
[1,0,0,0,0],
[0,1,0,0,0],
[0,0,0,0,0]
]

t = []
for material in clusterlayouts:
    a = adj_binary(x, y, material, 1.1)
    metric = list(np.sort(a[0].sum(1)))
    integerslist = [int(m) for m in metric]
    t.append(integerslist)


plt.figure(figsize=[10,10]); 
j = 0
for i in clusterlayouts:
    j+=1
    plt.subplot(4,5,j,aspect='equal')
    plt.title(str(j-1)+') \n'+str(i)+'\n'+ str(t[j-1]))
    plt.plot(np.array(x-x.mean())[np.array(i)==0],np.array(y-y.mean())[np.array(i)==0],'o',color=silicacolor,markersize=32,markeredgecolor=silicacolor)
    plt.plot(np.array(x-x.mean())[np.array(i)==1],np.array(y-y.mean())[np.array(i)==1],'o',color=pscolor,markersize=32,markeredgecolor=pscolor)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.xticks([])
    plt.yticks([])

plt.show()