import csv
from pathlib import Path
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 

    def _read_all(self):
        """Считывает CSV как список словарей"""
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != ["fio", "birthdate", "group", "gpa"]:
                raise ValueError("Неверный заголовок CSV-файла")
            for row in reader:
                # if not any(row.values()):
                #     continue
                rows.append(row)
        return rows

    def _write_all(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            fieldnames = ["fio", "birthdate", "group", "gpa"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def list(self):
        """Возвращает список"""
        rows = self._read_all()
        students = []
        for d in rows:
            j = {
                "fio": d["fio"],
                "birthdate": d["birthdate"],
                "group": d["group"],
                "gpa": float(d["gpa"])
            }
            students.append(Student.from_dict(j))
        return students

    def add(self, student: Student):
        rows = self._read_all()
        row = student.to_dict()
        row["gpa"] = str(row["gpa"])
        rows.append(row)
        self._write_all(rows)

    def find(self, substr: str):
        """Поиск по ФИО"""
        rows = self._read_all()
        substr = substr.lower()
        found = []
        for d in rows:
            if substr in d["fio"].lower():
                j = {
                    "fio": d["fio"],
                    "birthdate": d["birthdate"],
                    "group": d["group"],
                    "gpa": float(d["gpa"])
                }
                found.append(Student.from_dict(j))
        return found

    def remove(self, fio: str):
        """Удаляет запись по точному ФИО. Возвращает количество удалённых."""
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed = len(rows) - len(new_rows)

        if removed:
            self._write_all(new_rows)

        return removed

    def update(self, fio: str, **fields):
        rows = self._read_all()

        for r in rows:
            if r["fio"] == fio:
                r.update({k: str(v) for k, v in fields.items()})

        self._write_all(rows)