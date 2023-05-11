from dataclasses import dataclass


@dataclass
class Content:
    name: str
    year: int
    content_type: str = ""

    def __str__(self) -> str:
        return f"{self.name} is a {self.content_type}, released in {self.year}"


@dataclass
class Movie(Content):
    director: str = None
    duration: float = 0.0
    content_type: str = "Movie"

    def __str__(self) -> str:
        return f"{self.name} is a {self.duration} long {self.content_type}, released in {self.year}, directed by {self.director}"


@dataclass
class Music(Content):
    artist: str = ""
    duration: float = 0.0
    content_type: str = "Music"

    def __str__(self) -> str:
        return f"{self.name} is a {self.duration} long {self.content_type}, released in {self.year}, created by {self.artist}"


@dataclass
class Series(Content):
    season: int = 0
    duration: float = 0.0
    content_type: str = "Series"

    def __str__(self) -> str:
        return f"{self.name} is a {self.season} long {self.content_type}, released in {self.year}."


@dataclass
class Book(Content):
    author: str = ""
    pages: int = 0
    content_type: str = "Book"

    def __str__(self) -> str:
        return f"{self.name} is a {self.pages} long {self.content_type}, released in {self.year}, written by {self.author}"
