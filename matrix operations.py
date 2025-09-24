#matrix operations 
import numpy as np
mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = np.array([[3,2,1],[6,5,4],[9,8,7]])
print("addition of matrices:",mat1 + mat2)
print(mat1**2)
print(mat1*mat2)
print(mat1-mat2)
#dot()
print(np.dot(mat1,mat2))
#transpose
print(np.transpose(mat1))