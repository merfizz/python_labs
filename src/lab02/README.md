# Лабораторная работа 2

## Задание 1 - arrays
```
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
```
![pic 1](/image/lab02/min_max.png)

```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
  return sorted(set(nums))
```
![pic 2](/image/lab02/unique_sorted.png)

```
def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for n in mat :
        if not isinstance(n, (list, tuple)):
            raise TypeError("Строка не строка строк матрицы")
        
        result.extend(n)
        
    return result
```
![pic 3](/image/lab02/flatten.png)

## Задание 2 - matrix
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    
    if not mat:
        return mat

    i=0
    j=0
    row=len(mat)
    col=len(mat[0])

    for rows in mat:
        if ( len(rows)!=col):
            raise ValueError ("Матрица рваная ")

    result = [[] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j].append(mat[i][j])

    return result
```
![pic 4](/image/lab02/transpose.png)

```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if mat==[]:
        return(mat)
    
    c=len(mat[0])

    for rows in mat:
        if ( len(rows)!=c):
            raise ValueError ("Матрица рваная ")

    result= [sum(row) for row in mat]
    

    return result
```
![pic 5](/image/lab02/row_sums.png)

```
def col_sums(mat: list[list[float | int]]) -> list[float]:

    if mat==[]:
        return(mat)
    
    c=len(mat[0])
    
    for rows in mat:
        if ( len(rows)!=c):
            raise ValueError ("Матрица рваная ")

    
    result= [sum (mat[i][j] for i in range (len(mat))) for j in range (len(mat[0])) ]

    return result
```
![pic 6](/image/lab02/col_sums.png)

## Задание 3 - tuples

```
def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec, tuple):
        raise ValueError("Невернsq ввод")
      
    fio,group,gpa=rec
    
    if not fio.strip() or not isinstance(fio,str):
        raise ValueError("Неверное ФИО")
    
    if not group.strip() or not isinstance(group,str):
        raise ValueError("Неверная группа")

    if not isinstance(gpa, (float, int)):
        raise TypeError("Неверный тип GPA")
    

   
    names = fio.strip().split()
    initials = ''.join([name[0].upper() + '.' for name in names[1:]])  
    group= group.strip()
    new_string=f"{names[0].capitalize()} {initials}, гр. {group}, GPA {gpa:.2f}"
    
    return new_string
```
![pic 7](/image/lab02/tuples.png)
