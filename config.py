# This file contains configuration settings for the Trakt to Letterboxd script.

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILE_PATHS = {
    "input-watched-movies": BASE_DIR / "in" / "watched-movies.json",
    "input-ratings-movies": BASE_DIR / "in" / "ratings-movies.json",
    "output-csv": BASE_DIR / "out" / "movies.csv",
}
