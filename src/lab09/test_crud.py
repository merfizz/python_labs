from src.lab09.group import Group
from src.lab08.models import Student
from pathlib import Path

def main():
    path = Path("data/lab09/students.csv")
    group = Group(path)

    print("Файл без изменений")
    for s in group.list():
        print("  ", s)

    print("Добавляем студентика...")
    new_student = Student(
        fio="Студентов Студент",
        birthdate="2006-12-07",
        group="БИВТ-25-1",
        gpa=4.7
    )
    group.add(new_student)

    print("Список после добавления: ")
    for s in group.list():
        print("  ", s)

    print("Поиск по подстроке по ФИО 'Студент'")
    found = group.find("Студент")
    for s in found:
        print("  Обнаружен:", s)

    print(" Обновляем GPA...")
    group.update("Студентов Студент", gpa=5.0)
 
    print(" Обновленный список: ")
    for s in group.list():
        print("  ", s)

    print("Удаление...")
    group.remove("Студентов Студент")

    print("Список после всех преобразований: ")
    for s in group.list():
        print("  ", s)


if __name__ == "__main__":
    main()