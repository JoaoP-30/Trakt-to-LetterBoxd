import json
import csv


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

        title = item.get("movie", {}).get("title")
        year = item.get("movie", {}).get("year")
        imdb = item.get("movie", {}).get("ids", {}).get("imdb")

        movie_info = [title, year, imdb]

        filtred_movies.append(movie_info)

    return filtred_movies


def export_to_csv(processed_data):
    file_path = "out/movies.csv"

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Title", "Year", "IMDb"])

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
