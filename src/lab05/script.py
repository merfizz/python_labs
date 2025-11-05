import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab05.json_csv import json_to_csv,csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    json_to_csv(
        json_path="data/samples/people.json",
        csv_path="data/out/people.csv"
        )

    csv_to_json(
        csv_path="data/samples/people.csv",
        json_path="data/out/people.json",
        )

    csv_to_xlsx(
        csv_path="data/samples/cities.csv",
        xlsx_path="data/out/cities.xlsx",
        )


if __name__ == "__main__":
    main()
