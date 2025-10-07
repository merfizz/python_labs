from typing import *

def format_record(rec: tuple[str, str, float]) -> str:

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

try:
    student=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
    res=format_record(student)
    print(res)
except (ValueError,TypeError) as e:
    print(e)
