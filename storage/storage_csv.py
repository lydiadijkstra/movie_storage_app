import csv
from storage.istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_movies(self):
        """
        Retrieves the data from the CSV file and returns it as a dictionary.
        """
        movies = {}
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row["title"]] = {
                        "rating": row["rating"],
                        "year": int(row["year"]),
                        "poster url": row["poster url"]
                    }
        except FileNotFoundError:
            pass  # Return an empty dictionary if the file doesn't exist
        return movies

    def add_new_movie(self, title, year, rating, poster_url):
        """
        Adds a movie to the CSV file.
        """
        movies = self.get_movies()

        movies[title] = {
            "rating": rating,
            "year": year,
            "poster url": poster_url
        }
        self._save_movies_to_csv(movies)


    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV file.
        """
        movies = self.get_movies()

        if title in movies:
            movies[title]["rating"] = rating
        self._save_movies_to_csv(movies)


    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file.
        """
        movies = self.get_movies()

        if title in movies:
            del movies[title]
        self._save_movies_to_csv(movies)


    def _save_movies_to_csv(self, movies):
        """
        Helper method to save movies to the CSV file.
        """
        with open(self.file_path, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["title", "rating", "year", "poster url"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header and all rows
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    "title": title,
                    "rating": details["rating"],
                    "year": details["year"],
                    "poster url": details["poster url"]
                })
