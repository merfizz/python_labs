#Лаба 4
##io_txt_csv
```
import csv
from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Функция считывает текстовый файл и возвращает строку"""
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Функция создает cvs файл"""
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def frequencies_from_text(text: str) -> dict[str, int]:
    """Функция возврашает словарь: слово - частота """
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортировка по убыванию частоты"""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
```
##text_report
```
import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab04.io_txt_csv import read_text, write_csv,sorted_word_counts,frequencies_from_text
from lib.text import summary

def main():
    try:
      content = read_text("./data/lab04/input.txt")
      if not content.strip():
          print("Файл пуст")
          write_csv([], "./data/lab04/report.csv", header=("word", "count"))
      else:
          print (summary(content))
          content = write_csv(sorted_word_counts(frequencies_from_text(content)),"./data/lab04/report.csv", header=("word", "freq") )
      print ()
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except UnicodeDecodeError:
        print("Ошибка: Проблема с кодировкой файла!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
```
##Проверка A
![pic 1](/image/lab04/a.png)
##Проверка B
![pic 2](/image/lab04/b.png)
##Проверка c
![pic 3](/image/lab04/c.png)
