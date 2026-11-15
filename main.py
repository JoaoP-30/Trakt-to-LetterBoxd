from filehandler import read_file, export_to_csv
from datamanager import process_json_file, process_json_file_ratings
from config import FILE_PATHS


def main():

    # 1. Read the JSON files

    watched_movies_file = read_file(file_path=FILE_PATHS["input_watched-movies"])
    ratings_movies_file = read_file(file_path=FILE_PATHS["input-ratings-movies"])

    # 2. Process the JSON files

    ratings = process_json_file_ratings(ratings_movies_file)

    processed_data = process_json_file(watched_movies_file, ratings)

    # 3. Export the processed data to a CSV file

    export_to_csv(processed_data)


if __name__ == "__main__":
    main()
