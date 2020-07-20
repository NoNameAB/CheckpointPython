import numpy as np
a1 = np.array([0,1,2])
a2 = np.array([2,1,0])
matrix = np.cov(a1,a2)
print("Original Array 1 : ", a1)
print("Original Array 2 : ", a2)
print("Covariance matrix of the said arrays : \n", matrix)
