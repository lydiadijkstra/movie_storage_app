# run > pip3 install python-dotenv < in Terminal
import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')
REQUEST_URL = f"http://www.omdbapi.com/?i=tt1630029&apikey={API_KEY}&t="
#Poster API: http://img.omdbapi.com/?i=tt1630029&h=600&apikey=39fb6edd


def fetch_data(title):
    """
    Uses the Movie API to retrieve chosen movie data
    :param title: user choice for title
    :return: movie data from API
    """
    try:
        response = requests.get(REQUEST_URL + title)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectionError as e:
        print("Error, lost connection: ", e)
    except requests.exceptions.ConnectTimeout as f:
        print("Timeout: ", f)
    except requests.exceptions.RequestException as g:
        print("There is an error: ", g)

    return data
