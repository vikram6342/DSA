from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_0, col_0 =set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_0.add(i)
                col_0.add(j)
    for i in row_0:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for i in col_0:
        for j in range(len(matrix)):
            matrix[j][i] = 0
