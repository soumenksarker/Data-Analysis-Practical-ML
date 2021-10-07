from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('dark_background')
fig =plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y= [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]
#ax1.plot_wireframe(x,y,z)
##x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
##y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
##z2 = [-1,-2,-6,-3,-2,-7,-3,-3,-7,-2]

#ax1.scatter(x1, y1,z1, c='r', marker='o')
#ax1.scatter(x2,y2,z2, c='k', marker='o')
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 =[1,2,3,4,5,6,7,4,5,1]


dx = np.ones(10)
dy = np.ones(10)
dz =[1,2,6,3,2,7,3,3,7,2]

ax1.bar3d(x3,y3,z3,dx,dy,dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
