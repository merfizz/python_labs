from typing import *


def transpose(mat: list[list[float | int]]) -> list[list]:

    if not mat:
        return mat

    row = len(mat)
    col = len(mat[0])

    for rows in mat:
        if len(rows) != col:
            raise ValueError("Матрица рваная ")

    i = 0
    j = 0

    result = [[] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j].append(mat[i][j])

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if mat == []:
        return mat

    c = len(mat[0])

    for rows in mat:
        if len(rows) != c:
            raise ValueError("Матрица рваная ")

    result = [sum(row) for row in mat]

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:

    if mat == []:
        return mat

    c = len(mat[0])

    for rows in mat:
        if len(rows) != c:
            raise ValueError("Матрица рваная ")

    result = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

    return result


try:
    matrix = [[1, 2], [4, 3]]
    res = transpose(matrix)
    print(res)
except ValueError as e:
    print(e)

try:
    matrix = [[1, 2], [4, 3]]
    res = row_sums(matrix)
    print(res)
except ValueError as e:
    print(e)

try:
    matrix = [[1, 2], [4, 3]]
    res = col_sums(matrix)
    print(res)
except ValueError as e:
    print(e)
