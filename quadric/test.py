import numpy as np

#диагонализируемая матрица
B = [[1, 2, 0],
     [0, 3, 0],
     [2, -4, 2]]
eigenvalues0, D = np.linalg.eig(B)

# для столбцов P нет выделенного порядка;
# изменение порядка собственных векторов в P только изменит порядок
# собственных значений в диагональной форме A

lambdas0 = np.diag(eigenvalues0)
D_inv = np.linalg.inv(D)
diagf = D_inv @ B @ D
print(diagf)
print(lambdas0)

#нельзя диагонализировать над вещественными числами
A = [[0, 1],
     [-1, 0]]
eigenvalues1, P = np.linalg.eig(A)

lambdas1 = np.diag(eigenvalues1)
print(lambdas1)

#не является диагонализируемой ни над каким полем
C = [[0, 1],
     [0, 0]]
eigenvalues2, Q = np.linalg.eig(C)

lambdas2 = np.diag(eigenvalues2)
print(lambdas2)
