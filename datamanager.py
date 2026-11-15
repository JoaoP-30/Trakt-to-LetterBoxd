# This file process is responsible for processing data from a JSON file

from datetime import datetime

def process_json_file(file, ratings):

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

        rate = ""

        if imdb in ratings:
            rate = ratings[imdb]

        movie_info = [title, year, rate, watched_date, imdb]

        filtred_movies.append(movie_info)

    return filtred_movies


def process_json_file_ratings(file):

    filtred_movies_ratings = {}

    for item in file:
        rating = float(item.get("rating")) / 2

        imdb = item.get("movie", {}).get("ids", {}).get("imdb")

        filtred_movies_ratings[imdb] = rating

    return filtred_movies_ratings
