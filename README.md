
```markdown
# **Movie Project with OOP**

This is a Python-based movie management application designed using Object-Oriented Programming (OOP) principles. The project allows users to manage their movie database, perform various operations like adding, deleting, and filtering movies, and generate an HTML website to showcase the collection.

---

## **Features**

- **List Movies**: View all movies in the database along with their year and rating.
- **Add Movies**: Fetch movie details (title, year, rating, and poster URL) from an API and add them to the database.
- **Delete Movies**: Remove movies from the database.
- **Generate Website**: Create an HTML page showcasing the movies in a user-friendly format.
- **Movie Statistics**:
  - Calculate the average and median ratings.
  - Display the best- and worst-rated movies.
- **Search and Sort**:
  - Search for movies by title.
  - Sort movies by rating or release year.
- **Random Movie Recommendation**: Suggest a random movie from the collection.
- **Filter Movies**: Filter movies by rating or release year range.

---

## **Project Structure**

```
movieprojectoop/
│
├── data/                   # Contains movie data files
│   ├── movies.csv          # Movies stored in CSV format
│   └── movies.json         # Movies stored in JSON format
│
├── static/                 # Static assets for the website
│   └── style.css           # CSS file for styling the website
│
├── storage/                # Module for data storage handling
│   ├── __init__.py         # Initializes the storage package
│   ├── istorage.py         # Interface defining storage methods
│   ├── storage_csv.py      # Handles CSV-based storage
│   └── storage_json.py     # Handles JSON-based storage
│
├── templates/              # HTML templates for website generation
│   ├── index_template.html # Base template for movie website
│   └── movie_index_template.html  # Template for movie listings
│
├── .env                    # Environment variables (e.g., API keys)
├── .gitignore              # Files and directories to ignore in Git
├── data_fetcher.py         # Script for fetching movie data from an API
├── generate_website.py     # Logic to generate the movie website
├── main.py                 # Entry point for the application
├── movie_app.py            # Core application logic and user menu
├── requirements.txt        # Python dependencies for the project
└── README.md               # Project documentation
```

---

## **Technologies Used**

- **Programming Language**: Python
- **Data Storage**: JSON and CSV
- **Libraries**:
  - `abc`: Abstract base classes for defining interfaces
  - `statistics`: Calculate average and median ratings
  - `random`: Provide random movie recommendations
  - Custom API integration for fetching movie data

---

## **Getting Started**

### **Prerequisites**

- Python 3.8 or higher
- Internet connection (to fetch movie details via an API)

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-project-oop.git
   cd movie-project-oop
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Verify that `movies.json` exists in the `data` directory. Add sample content if needed:
   ```json
   {
       "Titanic": {
           "year": 1997,
           "rating": 7.9,
           "poster_url": "https://link-to-titanic-poster.com"
       }
   }
   ```

---

## **How to Run**

1. Start the application:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu for various options:
   - Add movies
   - View movie collection
   - Generate the website
   - Delete movies
   - Perform analytics or search/sort/filter movies

---

## **How It Works**

1. **Storage**:
   - Data is managed through the `IStorage` interface, ensuring flexibility in using different storage backends (`storage_csv.py` or `storage_json.py`).
   - JSON or CSV files are used to persist movie data.

2. **Fetching Data**:
   - The `data_fetcher.py` script fetches movie details (like rating and poster) from an API using the movie title.

3. **Website Generation**:
   - The `generate_website.py` script uses templates in the `templates` folder to create an HTML page.
   - Styling is handled through the `static/style.css` file.

4. **Modular Design**:
   - The project is organized with clear separation of concerns, making it easy to extend or modify.

---

## **Customizing the Project**

1. **Switch Storage Backend**:
   - Update the implementation in the `MovieApp` class to use either `StorageJson` or `StorageCsv` for data handling.
