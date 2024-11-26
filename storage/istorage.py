from abc import ABC, abstractmethod


class IStorage(ABC): # i = interface
    @abstractmethod
    def get_movies(self):
        """
        Interface function Purpose: Retrieve all movies stored in the database.
        Return Dictionary:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
          },
          "..." {
            ...
          },
        }
        """
        pass


    @abstractmethod
    def add_new_movie(self, title, year, rating, poster_url):
        """
        Interface function purpose: Adds a movie to the movies database.
        Updates the Database.
        Parameters: Title
        """
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """
        Interface function purpose: Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass


    @abstractmethod
    def delete_movie(self, title):
        """
        Interface function purpose: Deletes a movie from the movies database.
        Updates the Database
        """
        pass
