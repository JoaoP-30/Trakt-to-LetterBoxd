# This file is responsible for handling file operations such as reading and writing files.

import json
import csv
from config import FILE_PATHS


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        exit(1)
    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)


def export_to_csv(processed_data):
    file_path = FILE_PATHS["output_csv"]

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Title", "Year", "WatchedDate", "imdbID"])

            writer.writerows(processed_data)

            print("CSV file exported with success")

    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)
