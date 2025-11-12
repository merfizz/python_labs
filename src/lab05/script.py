from pathlib import Path
from lib.json_csv import json_to_csv,csv_to_json
from lib.csv_xlsx import csv_to_xlsx

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
