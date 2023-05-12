from functools import partial
import requests
from bs4 import BeautifulSoup, SoupStrainer


def google_search(query):
    response = requests.get(f"https://www.google.com/search?q={query}")
    if response.status_code == 200:
        soup = BeautifulSoup(
            response.content, parse_only=SoupStrainer("a"), features="html.parser"
        )
        soup = [link["href"] for link in soup if link.has_attr("href")]
    else:
        print("Error: Request failed with status code", response.status_code)

    guess = any([True for s in soup if "movie" in s.lower()])
    # for s in soup:
    #     if "movie" in s:
    #         print(s)
    print(guess)
    # results = response.json()
    # content_type = extract_content_type(results)
    # return content_type


def extract_content_type(results):
    content_type = "Movie"
    return content_type


def handle_movie(content):
    print(f"Handling Movie: {content}")


def handle_music(content):
    print(f"Handling Music: {content}")


def handle_series(content):
    print(f"Handling Series: {content}")


def handle_book(content):
    print(f"Handling Book: {content}")


def search_content(query):
    get_content_type = partial(google_search, query)
    content_type = get_content_type()
    print(content_type)
