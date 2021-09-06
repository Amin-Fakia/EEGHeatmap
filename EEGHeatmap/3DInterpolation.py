"""Interpolate the scalar values from
one Mesh or Points object onto another one"""
from vedo import *
import numpy as np
from dsi_24_montage import ch_pos
import mne

raw = mne.io.read_raw_edf("Sara2_M_filtered_0001.edf")
data = raw.get_data()


# 3D sensor locations

x = []
y = []
z = []
pts = []
for i, k in ch_pos.items():
    if(i != 'TRG'):
        x.append(k[0])
        y.append(k[1])
        z.append(k[2])
        pts.append([k[0],k[1],k[2]])
# 
# Import the Mesh as obj wavefront
mesh = Mesh("Head_detailed.obj",alpha=1)

# Change Rotation and Scale to match the Sensors location
mesh.rotateX(90)
mesh.scale(0.005)
mesh.origin(0,-0.03,-0.05)
pts2 = mesh.points()[5000:6000]



def findMinD(x):
    dist = []
    for p in mesh.points():
        dist.append(np.linalg.norm(pts[x]-p))
    return dist.index(min(dist))






# calculate the shortest distance between head model and the Sensors

#r =[]
# for i in range(0,len(pts)):
#     r.append(findMinD(i))

# the calculated values to save time
r_high = [74914, 74849, 12307, 53678, 53601, 197667, 197603, 142731, 86142, 86090, 81899, 81813, 180619, 
180544, 11539, 191237, 191182, 60085, 60047, 91754, 91677] # for the detailed model

pts3 = [mesh.points()[i] for i in r_high]







# pick random points where we assume that some scalar value is known
# (can be ANY points, not necessarily taken from the mesh)




    

# assume the value is random
scalars = np.random.uniform(-0.00001,0.00001, len(pts3))
t1 = []

c = 1
for i in data: 
    if(c <22):
        
        t1.append(i[4000])
    c += 1


# # create a set fo points with this scalar values
points = Points(pts3, r=10).cmap('rainbow', [*t1])
# #points2 = Points(pts, r=10).cmap('rainbow', scalars)

# # interpolate from points onto the mesh, by averaging the  closest ones
mesh.interpolateDataFrom(points,N=len(pts3)).cmap('jet').addScalarBar()

show(mesh,points).close()
