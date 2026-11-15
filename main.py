from filehandler import read_file, export_to_csv
from datamanager import process_json_file


def main():
    file = read_file("in/watched-movies.json")

    processed_data = process_json_file(file)

    export_to_csv(processed_data)


if __name__ == "__main__":
    main()
