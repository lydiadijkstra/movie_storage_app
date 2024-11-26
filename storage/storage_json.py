from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def get_movies(self):
        """
        Retrieves the data from the JSON file so it can be used in the programm
        :return: data from JSON File
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist


    def add_new_movie(self, title, year, rating, poster_url):
        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.get_movies()

        movies[title] = {
            "rating": rating,
            "year": year,
            "poster url": poster_url
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4)


    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.get_movies()

        movies[title]["rating"] = rating

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4)


    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.get_movies()

        del movies[title]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4)
