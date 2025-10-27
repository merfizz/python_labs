 # read_text / write_csv (+ ensure_parent_dir)
import csv
from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# def read_text(path: str | Path, encoding: str = "utf-8") -> str:
#     with open(path, 'r', encoding=encoding) as file:
#         return file.read()

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
   
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

try:
    content = read_text("./data/lab04/a.txt")
    print(content)
    
    # Получаем частоты слов
    freq_dict = frequencies_from_text(content)
    
    # # Сортируем по убыванию частоты
    # sorted_freq = sorted_word_counts(freq_dict)
    
    # # Сохраняем в CSV
    # write_csv(sorted_freq, "./data/lab04/word_freq.csv", 
    #           header=("Word", "Frequency"))
    
    # print("CSV файл успешно создан!")
    # print("Топ-5 слов:")
    # for word, count in sorted_freq[:5]:
    #     print(f"  {word}: {count}")

except FileNotFoundError:
    print("Ошибка: Файл не найден!")
except UnicodeDecodeError:
    print("Ошибка: Проблема с кодировкой файла!")
