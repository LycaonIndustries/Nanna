import requests
from src.content import *
import json


def response_parser(response: dict) -> Content:
    """Read the json response and extracts important information from the chaos."""
    data = Content(
        name=response.get("Title"),
        year=response.get("Year"),
        content_type=response.get("Type"),
    )
    return data


def imdb_search(query : str):

    response = requests.get(f"http://www.omdbapi.com/?t={query}&apikey=1ceb3181")
    response_json = response.json()

    response_json = dict(json.load(open("sample/movie.json")))

    data = response_parser(response_json)

    if data.content_type == "Movie":
        handle_movie(data)
    elif data.content_type == "Series":
        handle_series(data)
    elif data.content_type == "Music":
        handle_music(data)
    elif data.content_type == "Book":
        handle_book(data)
    else:
        print("Unsupported or unspecified data.")
        exit()


def handle_movie(content):
    print(f"Handling Movie: {content}")


def handle_music(content):
    print(f"Handling Music: {content}")


def handle_series(content):
    print(f"Handling Series: {content}")


def handle_book(content):
    print(f"Handling Book: {content}")


if __name__ == "__main__":
    imdb_search(input("Title:\t"))
