# генерация data/report.csv + ★
from pathlib import Path
from lib.io_txt_csv import (
    read_text,
    write_csv,
    sorted_word_counts,
    frequencies_from_text,
)
from lib.text import summary


def main():
    try:
        content = read_text("./data/lab04/input.txt")
        if not content.strip():
            print("Файл пуст")
            write_csv([], "./data/lab04/report.csv", header=("word", "count"))
        else:
            print(summary(content))
            content = write_csv(
                sorted_word_counts(frequencies_from_text(content)),
                "./data/lab04/report.csv",
                header=("word", "freq"),
            )
        print()
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except UnicodeDecodeError:
        print("Ошибка: Проблема с кодировкой файла!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
