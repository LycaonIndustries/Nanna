import sys
import unittest
from io import StringIO

from src.content import Book, Movie, Music, Series


class ContentTestCase(unittest.TestCase):
    def test_print_content(self):
        content = Movie("Inception", 2010, director="Christopher Nolan", duration=2.5)
        expected_output = "Inception is a 2.5 long Movie, released in 2010, directed by Christopher Nolan\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print(content)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_movie(self):
        movie = Movie("Inception", 2010, director="Christopher Nolan", duration=2.5)
        expected_output = "Inception is a 2.5 long Movie, released in 2010, directed by Christopher Nolan\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print(movie)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_music(self):
        music = Music("Bohemian Rhapsody", 1975, artist="Queen", duration=5.5)
        expected_output = "Bohemian Rhapsody is a 5.5 long Music, released in 1975, created by Queen\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print(music)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_series(self):
        series = Series("Friends", 1994, season=10, duration=22.0)
        expected_output = "Friends is a 10 long Series, released in 1994.\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print(series)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_book(self):
        book = Book("To Kill a Mockingbird", 1960, author="Harper Lee", pages=336)
        expected_output = "To Kill a Mockingbird is a 336 long Book, released in 1960, written by Harper Lee\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print(book)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
