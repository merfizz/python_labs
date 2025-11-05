from openpyxl import Workbook
import csv
from pathlib import Path

# with open("data/samples/people.csv", encoding="utf-8") as f:
#     """
#         ws.append for row in csv.reader(f)
        
#         wb.save("data/out/people.xlsx")
#     """

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    Проверка ошибок:
    неверный тип файла, пустой JSON или CSV → ValueError.
    осутствующий файл → FileNotFoundError
    Результат — открываемый XLSX с корректной структурой таблицы.
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV-файл {csv_path} не найден")
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    with open("data/samples/people.csv", encoding="utf-8") as csv_file:
        csv_read = csv.DictReader(csv_file)

        if not csv_read.fieldnames:
            raise ValueError("CSV без заголовков или пуст")
        
        ws.append(csv_read.fieldnames)
        for row in csv_read:
            ws.append([row[field] for field in csv_read.fieldnames])

    xlsx_path = Path(xlsx_path)
    wb.save(xlsx_path)

csv_to_xlsx(
    csv_path="data/samples/cities.csv",
    xlsx_path="data/out/cities.xlsx",
)


