fio = str(input("ФИО: "))
new_fio = fio.split()
fio_new = f"{new_fio[0]} {new_fio[1]} {new_fio[2]}"
res = f"{new_fio[0][0]}{new_fio[1][0]}{new_fio[2][0]}."
len = len(fio_new)
print(f"Инициалы: {res} \nДлина:{len}")
