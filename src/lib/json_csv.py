import json
import csv
from pathlib import Path


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    Проверка ошибок:
    неверный тип файла, пустой JSON или CSV → ValueError.
    осутствующий файл → FileNotFoundError
    """
    json_path = Path(json_path)

    if not json_path.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    with json_path.open("r", encoding="utf-8") as json_file:
        try:
            data_json = json.load(json_file)
        except json.JSONDecodeError as e:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data_json or not isinstance(data_json, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not all(isinstance(row, dict) for row in data_json):
        raise ValueError("JSON должен содержать список словарей")

    csv_path = Path("./data/out/people.csv")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=tuple(data_json[0].keys()))
        writer.writeheader()
        writer.writerows(data_json)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    Проверка ошибок:
    неверный тип файла, пустой JSON или CSV → ValueError.
    осутствующий файл → FileNotFoundError
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    with csv_path.open("r", encoding="utf-8") as csv_file:
        csv_read = csv.DictReader(csv_file)  # читает CSV как список словарей;
        if not csv_read.fieldnames:
            raise ValueError("CSV-файл не содержит заголовков или пуст")
        data_csv = [row for row in csv_read]

    if not data_csv:
        raise ValueError("Пустой CSV")
    json_path = Path(json_path)

    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(data_csv, json_file, ensure_ascii=False, indent=2)
