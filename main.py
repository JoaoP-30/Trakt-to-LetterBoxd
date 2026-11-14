import json
import csv
from datetime import datetime, timedelta


def read_file():
    file_path = "in/watched-movies.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            print("File read with sucess")

            return json.load(file)

    except FileNotFoundError:
        print("File not found")
        exit(1)
    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)


def process_json_file(file):

    filtred_movies = []

    for item in file:

        raw_date = item.get("last_watched_at")

        formated_date = None

        if raw_date:
            dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%fZ")

            formated_date = dt.strftime("%Y-%m-%d")

        title = item.get("movie", {}).get("title")
        year = item.get("movie", {}).get("year")
        watched_date = formated_date
        imdb = item.get("movie", {}).get("ids", {}).get("imdb")

        movie_info = [title, year, watched_date, imdb]

        filtred_movies.append(movie_info)

    return filtred_movies


def export_to_csv(processed_data):
    file_path = "out/movies.csv"

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Title", "Year", "WatchedDate", "imdbID"])

            writer.writerows(processed_data)

            print("CSV file exported with success")

    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)


def main():
    file = read_file()

    processed_data = process_json_file(file)

    export_to_csv(processed_data)


if __name__ == "__main__":
    main()
