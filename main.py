from movie_app import MovieApp
from storage.storage_csv import StorageCsv


if __name__ == "__main__":
    """
    Initialize the storage and the app.
    Run the app.
    """
    #storage = StorageJson('storage/movies.json')
    storage = StorageCsv('data/movies.csv')
    app = MovieApp(storage=storage)

    app._main()
