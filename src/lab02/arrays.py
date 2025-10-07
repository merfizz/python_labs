
from typing import *


def min_max(nums: List[float | int]) -> Tuple[[float | int], [float | int]]:
    if not nums:
        raise ValueError("Список пуст")
    min_n=nums[0]
    max_n=nums[0]

    for n in nums:
        if min_n>n :
            min_n=n
        if max_n<n :
            max_n=n
    
    return (min_n, max_n)
'''
try:
    numbers = [1.5, 2, 2.0, -3.1]
    res = min_max(numbers)
    print(res)
except ValueError as e:
    print(e)
'''

def unique_sorted(nums: list[float | int]) -> list[float | int]:
  return sorted(set(nums))
'''
numbers= [1.0, 1, 2.5, 2.5, 0]
res=unique_sorted(numbers)
print(res)
'''

def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for n in mat :
        if not isinstance(n, (list, tuple)):
            raise TypeError("Строка не строка строк матрицы")
        
        result.extend(n)
        
    return result

try:
    matrix = [[1, 2], "ab"]
    res = flatten(matrix)
    print(res)
except TypeError as e:
    print(e)
    

'''
[3, -1, 5, 5, 0] → (-1, 5)
[42] → (42, 42)
[-5, -2, -9] → (-9, -2)
[] → ValueError
[1.5, 2, 2.0, -3.1] → (-3.1, 2)
'''

'''
[3, 1, 2, 1, 3] → [1, 2, 3]
[] → []
[-1, -1, 0, 2, 2] → [-1, 0, 2]
[1.0, 1, 2.5, 2.5, 0] → [0, 1.0, 2.5] (допускаем смешение int/float)
'''

'''
[[1, 2], [3, 4]] → [1, 2, 3, 4]
[[1, 2], (3, 4, 5)] → [1, 2, 3, 4, 5]
[[1], [], [2, 3]] → [1, 2, 3]
[[1, 2], "ab"] → TypeError («строка не строка строк матрицы»)
'''