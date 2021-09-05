"""Interpolate the scalar values from
one Mesh or Points object onto another one"""
from vedo import *
import numpy as np
from dsi_24_montage import ch_pos


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
mesh = Mesh("Head.obj",alpha=0.7, computeNormals=True)

# Change Rotation and Scale to match the Sensors location
mesh.rotateX(90)
mesh.scale(0.005)
mesh.origin(0,-0.05,0)

# pick random points where we assume that some scalar value is known
# (can be ANY points, not necessarily taken from the mesh)
pts2 = mesh.points()[10:100]



    

# assume the value is random
scalars = np.random.randint(-100,100, len(pts2))

# create a set fo points with this scalar values
points = Points(pts2, r=10).cmap('rainbow', scalars)

# interpolate from points onto the mesh, by averaging the 5 closest ones
mesh.interpolateDataFrom(points, N=len(pts2)).cmap('rainbow').addScalarBar()

show(mesh, points,  axes=9).close()
