fio=str(input("ФИО: "))
ini=''
len_=0
i=1
for i in range (len(fio)):
    if (ord(fio[i])>=1040)and(ord(fio[i])<=1071) : 
       ini= ini + fio[i]
    if fio[i]!=" ":
        len_+=1



print(f"Инициалы: {ini}.\nДлина (символов): {len_+2} ")
