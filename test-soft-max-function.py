# SOURCE https://python.plainenglish.io/python-snippets-7e8dcbeae26e

'''
======================
3D surface (color map)
======================
Plotting a softmax function in 3D
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
#Creating the figure
fig = plt.figure()
ax = fig.gca(projection='3d')
#Mking the data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
#Softmax
Z = (np.exp(X)/ (np.exp(X)+ np.exp(Y)))
#Ploting the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=10)
#Customize the z axis setting it t0 the range(0,1)
ax.set_zlim(0, 1.0)
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()