import json
from pathlib import Path
from .models import Student

def students_to_json(students, path_):
    """Сохранение списка студентов в JSON файл."""
    data = [s.to_dict() for s in students]
    path=Path(path_)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def students_from_json(path_) -> list[Student]:
    """Загрузка студентов из JSON файла."""
    path=Path(path_)
    with open(path, "r", encoding="utf-8") as f:
        row = json.load(f)

    result = []
    for i in row:
        result.append(Student.from_dict(i))

    return result