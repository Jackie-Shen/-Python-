import numpy as np
import sigmoid

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
#
# print(A.shape)
# print(np.ndim(A))
# print(np.dot(A,B))

X = np.array([1, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
print(A1)
print(sigmoid.sigmoid(A1))

W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(A1, W2) + B2
print(A2)
print(sigmoid.sigmoid(A2))

W3 = np.array([[0.1, 0.3],[0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(A2, W3) + B3
print(A3)
