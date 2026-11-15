# This file process is responsible for processing data from a JSON file

from datetime import datetime


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
