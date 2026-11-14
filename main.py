import json


def read_file():
    file_path = "in/example.json"

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
        rating = item.get("rating")
        imdb = item.get("movie", {}).get("ids", {}).get("imdb")

        movie_info = [title, year, rating, imdb]

        filtred_movies.append(movie_info)

    return filtred_movies


def main():
    file = read_file()

    process_json_file(file)


if __name__ == "__main__":
    main()
