from typing import *

def transpose(mat: list[list[float | int]]) -> list[list]:
    
    if not mat:
        return mat
    
    row=len(mat)
    col=len(mat[0])
    

    for rows in mat:
        if ( len(rows)!=col):
            raise ValueError ("Матрица рваная ")

    i=0
    j=0

    result = [[] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j].append(mat[i][j])

    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if mat==[]:
        return(mat)
    
    row=len(mat)
    col=len(mat[0])
    
    for rows in mat:
        if ( len(rows)!=col):
            raise ValueError ("Матрица рваная ")
        result=[0]*row

    for i in range(row):
        for j in range(col):
            result[i]=result[i]+mat[i][j]

    return result

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if mat==[]:
        return(mat)
    
    row=len(mat)
    col=len(mat[0])
    
    
    for rows in mat:
        if ( len(rows)!=col):
            raise ValueError ("Матрица рваная ")
        result=[0]*col

    for i in range(row):
        for j in range(col):
            result[j]=result[j]+mat[i][j]

    return result

'''
try:
    matrix=[[1, 2], [3]]
    res=transpose(matrix)
    print(res)
except ValueError as e:
    print(e)

try:
    matrix=[[1, 2], [3]]
    res=row_sums(matrix)
    print(res)
except ValueError as e:
    print(e)

try:
    matrix=[[1, 2], [3]]
    res=col_sums(matrix)
    print(res)
except ValueError as e:
    print(e)
    '''
