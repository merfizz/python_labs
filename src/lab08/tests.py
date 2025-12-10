from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

def test_student():
    print(" Класс Student")
    student1 = Student(
        fio = "Кириллов Кирилл Кириллович",
        birthdate = "2007-04-25",
        group = "SE-01",
        gpa = 4.5
    )
    print("Студент создан")
    print(student1)
    print(f'Возраст: {student1.age()} лет')
    print(f'Словарь:{student1.to_dict()}')
    print()


def test_serialization():
    print("Сериализация...")
    students = [
        Student("Алексеев Алексей Алексеевич","2007-04-25", "SE-01", 4.5),
        Student("Петров Пётр Петрович", "2007-04-05", "SE-02", 3.8),
    ]
    students_to_json(students,"data/lab08/students_output.json")
    print("Студенты сохранены в students_output.json")

    loaded_students = students_from_json("data/lab08/students_input.json")
    print("Студенты выгружены: ")
    for student in loaded_students:
        print(f" - {student}")
    print()

def test_validation():
    print("Валидация...")
    try:
        Student('Тест', "2020-13-45", "SE-01", 3.0)
    except ValueError as e:
        print(f"Произошла валидации: {e} ")


    try:
        Student("Тест", "2020-01-01", "SE-02", 6)
    except ValueError as e:
        print(f"Произошла ошибка валидации GPA: {e} ")
if __name__ == "__main__":
    test_student()
    test_validation()
    test_serialization()