from filehandler import read_file, export_to_csv
from datamanager import process_json_file
from config import FILE_PATHS


def main():
    file = read_file(FILE_PATHS["input_watched-movies"])

    processed_data = process_json_file(file)

    export_to_csv(processed_data)


if __name__ == "__main__":
    main()
