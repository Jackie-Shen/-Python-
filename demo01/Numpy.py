import numpy as np

A = np.array([[1,2],[3,4]])
# print(A)
# print(A.shape)
# print(A.dtype)

B = np.array([[3,0],[0,6]])
# print(A+B)
# print(A*B)
#
# print(A * 10)
#
# print(A[0])
# print(A[0][0])

# for row in A:
#     for col in row:
#         print(col)

C = A.flatten()
# print(C)
# print(C[np.array([0,3])])

print(C[C>2])