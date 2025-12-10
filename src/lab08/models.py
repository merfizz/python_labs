from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # валидацию формата даты и диапазона gpa
        try:
           datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
                raise ValueError(
                    "birthdate must be in format YYYY-MM-DD"
                )
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        """Возвращает полный возраст в годах."""
        today = date.today()
        birth =  datetime.strptime(self.birthdate, "%Y-%m-%d")
        
        years = today.year - birth.year

        # Если день рождения ещё не был в этом году — вычитаем 1
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1

        return years

    def to_dict(self) -> dict:
        """Сериализация объекта в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        """Создание объекта Student из словаря."""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],  # __post_init__ сам распарсит строку
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self):
        """Человекочитаемое представление студента."""
        return f"{self.fio}, группа {self.group}, GPA: {self.gpa}"