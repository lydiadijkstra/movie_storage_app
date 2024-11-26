import statistics #library for calculating statistics
import random #library for finding a random movie
from data_fetcher import fetch_data #API File
from generate_website import replace_string_html, dump_data_to_html #File for generating website


class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _display_menu(self):
        """
        Show the menu
        :return: menu options
        """
        return """Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Generate Movie App
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Movies sorted by year
    10. Filter movies"""


    def _leave_database(self):
        """
        nr. 0 - exit the database
        """
        return "Bye!"


    def _display_movies(self):
        """
        Nr. 1 - displays the movies from the database
        :param movies: dictionary with movies-data
        """
        movies = self._storage.get_movies()

        number_of_movies = len(movies)
        print(f'{number_of_movies} movies in total')
        for title, items in movies.items():
            print(f'{title} ({items["year"]}): {items["rating"]}')


    def _add_movie(self):
        """
        Nr. 2 - User add a movie incl rating and year
        :return: new dictionary movies
        """
        movies = self._storage.get_movies()

        while True:
            new_movie = input("Enter new movie: ").strip().capitalize()  # prevents leading and ending whitespace
            if not new_movie:
                print("Movie name cannot be empty, please enter movie name!")
                continue
            if new_movie in movies:
                print("This movie is already listed!")
                continue
            movies_api = fetch_data(new_movie)
            if len(movies_api) <= 3:
                print("Movie was not found")
                continue
            break

        new_movie_year = movies_api["Year"]
        new_movie_rating = movies_api["Ratings"][0]["Value"]
        new_movie_poster_url = movies_api["Poster"]

        self._storage.add_new_movie(new_movie, new_movie_year, new_movie_rating, new_movie_poster_url)
        print(f'Movie {new_movie} was successfully added')
        #return movies

    def _delete_movie(self):
        """
        Nr.3 - Delete a movie from the dictionary
        :return: dict movies
        """
        movies = self._storage.get_movies()

        while True:
            movie_to_delete = input("Enter movie name to delete: ").capitalize()
            if movie_to_delete not in movies:
                print(f'Movie {movie_to_delete} does not exist')
                continue
            self._storage.delete_movie(movie_to_delete)
            print(f'Movie {movie_to_delete} successfully deleted')
            break
        #return movies


    def _split_rating(self, rating):
        """
        Function for splitting the rating from "/10" so it can be used in calculations
        :param rating: a string "xy/10"
        :return:
        """
        try:
            split_rating, _ = rating.split("/")
            split_rating = float(split_rating)
            return split_rating
        except ValueError as e:
            print(e)


    def _average_rating(self):
        """
        calculates the average rating
        :param movies: dict movies
        :return: average rating of movies
        """
        movies = self._storage.get_movies()

        total_rating = 0
        for title in movies:
            rating = self._split_rating(movies[title]["rating"])
            total_rating += rating
        avg_rating = round(total_rating / len(movies), 1)
        return f'Average rating: {avg_rating}'


    def _median_rating(self):
        """
        calculates the median rating
        :param movies: dict movies
        :return: median rating of movies
        """
        movies = self._storage.get_movies()

        all_ratings = []
        for title in movies:
            rating = self._split_rating(movies[title]["rating"])
            all_ratings.append(rating)
        median_ratings = statistics.median(all_ratings)
        return f'Median rating: {median_ratings}'


    def _best_rated_movie(self):
        """
        Analytics to find the best rated movie
        :param movies: dict movies
        :return: best rated movie
        """
        movies = self._storage.get_movies()

        max_rating = 0
        for title in movies:
            rating = self._split_rating(movies[title]["rating"])
            if rating > max_rating:
                max_rating = rating
                best_movie_title = title
        return f'Best movie: {best_movie_title}, {max_rating}'


    def _worst_rated_movie(self):
        """
        Analytics to find the worst rated movie
        :return: worst rated movie
        """
        movies = self._storage.get_movies()

        min_rating = 10
        for title in movies:
            rating = self._split_rating(movies[title]["rating"])
            if rating < min_rating:
                min_rating = rating
                worst_movie_title = title
        return f'Worst movie: {worst_movie_title}, {min_rating}'


    def _movie_stats(self):
        """
        Nr. 5 - Displays the statistics
        :param movies: dict movies
        """
        print(self._average_rating())
        print(self._median_rating())
        print(self._best_rated_movie())
        print(self._worst_rated_movie())


    def _random_movie(self):
        """
        Nr. 6 - Get a random suggestion for a movie with the random library
        :param movies: dictionary
        :return:random_choice_movie incl. rating
        """
        movies = self._storage.get_movies()

        random_choice_movie = random.choice(list(movies.keys()))
        return f'Your movie for tonight: {random_choice_movie}, it is rated {movies[random_choice_movie]["rating"]}'


    def _search_for_title(self):
        """
        Nr. 7 - Search for a movie with a part of the title
        :param movies: dictionary
        """
        movies = self._storage.get_movies()

        search_prompt = input("Enter part of moviename: ")
        search_outcome = {}
        for title, details in movies.items():
            if search_prompt.lower() in title.lower():
                search_outcome[title] = ["rating"]
                print(f'{title}, {details["rating"]}')


    def _get_rating_from_movie(self, movie_tuple):
        rating = movie_tuple[1]["rating"]
        return rating


    def _movies_sorted_by_ratings(self):
        """
        Nr. 8 - Sorts the dict by ratings
        :param movies:
        :return:
        """
        movies = self._storage.get_movies()

        movielist = list(movies.items())
        movielist.sort(key=self._get_rating_from_movie, reverse=True)

        for title, details in movielist:
            print(f'{title} ({details["year"]}): {details["rating"]}')


    def _movies_sorted_by_year(self):
        """
        Nr. 9 - Sorting by year, up or down
        :param movies: dict with movies
        :return: sorted products
        """
        movies = self._storage.get_movies()

        movielist = list(movies.items())
        while True:
            decision_for_year_sorting = input("Do you want the latest movies first? (Y/N) ").lower()
            if decision_for_year_sorting == "y":
                movielist.sort(key=lambda x: x[1]["year"], reverse=True)
                for title, details in movielist:
                    print(f'{title} ({details["year"]}): {details["rating"]}')
                break
            elif decision_for_year_sorting == "n":
                movielist.sort(key=lambda x: x[1]["year"])
                for title, details in movielist:
                    print(f'{title} ({details["year"]}): {details["rating"]}')
                break
            else:
                print("Please enter 'Y' or 'N'")


    def _filter_movies(self):
        """
        Nr. 10 - Filters the movies with user-criteria
        :param movies: dict with movies
        :return:
        """
        movies = self._storage.get_movies()

        while True:
            minimum_rating_user = input("Enter minimum rating (leave blank for no minimum rating): ")
            if minimum_rating_user == "":
                minimum_rating = None
                break
            try:
                minimum_rating = float(minimum_rating_user)
                break
            except ValueError:
                print("Invalid input. Please enter a valid rating.")
        while True:
            start_year_input = input("Enter start year (leave blank for no start year): ")
            if start_year_input == "":
                start_year = None
                break
            try:
                start_year = int(start_year_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        while True:
            end_year_input = input("Enter end year (leave blank for no end year):")
            if end_year_input == "":
                end_year = None
                break
            try:
                end_year = int(end_year_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")

        filtered_movies = []
        for title, details in movies.items():
            try:
                rating, _ = movies[title]["rating"].split("/")
                rating = float(rating)
            except ValueError as e:
                print(e)
            try:
                year = movies[title]["year"]
                year = float(year)
            except ValueError as e:
                print(e)
            if (minimum_rating is None or minimum_rating <= rating) and \
                    (start_year is None or start_year <= year) and \
                    (end_year is None or end_year >= year):
                filtered_movies.append(f'{title} ({details["year"]}): {details["rating"]}')
        if filtered_movies:
            for movie in filtered_movies:
                print(movie)
        else:
            print("No result match these criteria")


    def _create_website(self, output):
        """
        Nr. 4 - Running the functions in the generate_website.py
        """
        new_html_content = replace_string_html(output)
        dump_data_to_html(new_html_content)


    def _create_str_for_html(self):
        """
        Creates the new text for the html-file with the movie data
        Redirects to the serialization function
        :return: string for the new html-file
        """
        movies = self._storage.get_movies()

        output = ''
        for title, movie_data in movies.items():
            output += self._serialize_movies(title, movie_data)
        return self._create_website(output)


    def _serialize_movies(self, title, movie_data):
        """
        Serialize the movie data for usage in html
        :param movie_data, title: retrieved data from api
        :return: output with html tags incl title, url, year and rating
        """
        output = ''
        year = movie_data['year']
        movie_poster = movie_data['poster url']
        rating = movie_data['rating']

        output += "<li class='movie_grid__item'>"
        output += f"<div class='card__title'> {title}</div>\n"
        output += "<p class='card__text'>"
        if year:
            output += f"<div><strong>Year:</strong> {year}</div>\n"
        if movie_poster:
            output += f"<div><img src='{movie_poster}' alt='Poster'></div>\n"
        if rating:
            output += f"<div><strong>Rating:</strong> {rating}</div>\n"
        output += '</p>'
        output += '</li>'

        return output


    def _user_prompt(self):
        """
        prompt the user for his choice from menu
        :return: user input (prompt)
        """
        prompt = input("\nEnter choice (0-10): ")
        print("")
        if prompt == "0":
            print(self._leave_database())
            return False
        elif prompt == "1":
            self._display_movies()
        elif prompt == "2":
            self._add_movie()
        elif prompt == "3":
            self._delete_movie()
        elif prompt == "4":
            self._create_str_for_html()
            print("Website was successfully generated!")
        elif prompt == "5":
            self._movie_stats()
        elif prompt == "6":
            print(self._random_movie())
        elif prompt == "7":
            self._search_for_title()
        elif prompt == "8":
            self._movies_sorted_by_ratings()
        elif prompt == "9":
            self._movies_sorted_by_year()
        elif prompt == "10":
            self._filter_movies()
        else:
            print("Invalid input, enter a valid number (0-10)")
        input("\nPress enter to continue ")
        return prompt


    def _main(self):
        """
        contains the while loop to loop until exit
        """
        """movies = data.get_movies()
        with open("movies_data.json", "w") as file:
            json.dump(movies, file)"""

        print("\n********** My Movies Database **********\n")
        while True:
            print(self._display_menu())
            prompt = self._user_prompt()
            if prompt is False:
                break
