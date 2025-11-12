 # read_text / write_csv (+ ensure_parent_dir)
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

def ensure_parent_dir(path: str | Path) -> None:
    """Создает родительскую директорию если не существует"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

