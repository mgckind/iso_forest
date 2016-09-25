import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
import iso
mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance
x, y = np.random.multivariate_normal(mean, cov, 500).T
#plt.plot(x, y, 'ko')
#plt.axis('equal')
#plt.show()
X=np.array([x,y]).T
C=iso.iTree(X,0,100)
