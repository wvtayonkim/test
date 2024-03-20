import numpy as np

b = np.array([0,4,1]) # r vector (-1.5 feet)
c = np.array([5,6,0]) # p cos(gama=30), p sin(gama=30), 0

cross_result = np.cross(b,c)

#print the cross-product result
print("cross_result =", cross_result)

a = np.array([2,0,3])

scaler_triple = np.dot(a,cross_result)

#print the scaler_triple result
print("scaler_triple =", scaler_triple)

Touched by user2
