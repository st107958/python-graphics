import numpy as np


def to_cannonical(matrix_of_quadric, vector, constant):
    matrix_of_quadric = np.array(matrix_of_quadric)
    eigenvalues, eigenvectors = np.linalg.eig(matrix_of_quadric)
    A1 = np.diag(eigenvalues)
    a1 = eigenvectors @ vector

    # print(a1)
    # print(A1)

    eigenvectors_inv = np.linalg.inv(eigenvectors)
    assert np.array_equal(eigenvectors_inv @ a1, vector), "не верный переход между базисами"
    assert np.array_equal(eigenvectors @ A1 @ eigenvectors_inv, matrix_of_quadric), "не верно диагонализирована"

    return normalize_equation(A1, a1, constant)


def normalize_equation(matrix, vector, constant):
    matrix = np.array(matrix)
    coeffs = np.diag(matrix)
    count_below_zero_elements = np.sum(coeffs < 0)
    if count_below_zero_elements > 1:  #даже учитывая что какие то нули
        constant = -constant
        vector = -1*vector
        matrix = -1*matrix
        print(matrix)
        assert np.sum(coeffs < 0) > 1, "нормализация не работает"
    return matrix, vector, constant


class TreeNode:
    def __init__(self, rule, true_branch=None, false_branch=None, result=None):
        self.rule = rule  # правило для данного узла
        self.true_branch = true_branch  # если правило истинно
        self.false_branch = false_branch  # если правило ложно
        self.result = result  # если это лист, здесь будет класс или результат

    def classify(self, arr1, arr2, arr3):
        # Если это лист, возвращаем результат
        if self.result is not None:
            return self.result

        # Если правило выполняется, идем по true ветке, иначе по false
        if self.rule(arr1, arr2, arr3):
            return self.true_branch.classify(arr1, arr2, arr3)
        else:
            return self.false_branch.classify(arr1, arr2, arr3)

def classify(matrix, vector, constant):
    rule1 = lambda matrix, vector, constant: np.linalg.det(matrix) == 0
    def rule3(matrix, vector, constant):
        if constant > 0:
            return


c = 1
a = np.array([1, 2, 3])
A = np.array([1, 1, 1, 2, 0, 0])  # a11, a22, a33, a12, a13, a23
matrix = np.array([[A[0], A[3]/2, A[4]/2],
                    [A[3]/2, A[1], A[5]/2],
                    [A[4]/2, A[5]/2, A[2]]])

to_cannonical(matrix, a, c)



