# Define custom exceptions for specific error conditions
class MovieAlreadyRentedError(Exception):
    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.message = f"Movie '{movie_title}' is already rented out."
        super().__init__(self.message)

class MovieNotFoundError(Exception):
    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.message = f"Movie '{movie_title}' not found in the store."
        super().__init__(self.message)

class ExceededMaxMoviesError(Exception):
    def __init__(self, max_movies_per_user):
        self.max_movies_per_user = max_movies_per_user
        self.message = f"Maximum movies ({max_movies_per_user}) already rented by the user."
        super().__init__(self.message)

# Define a class representing the movie rental store
class RentalStore:
    def __init__(self, max_movies_per_user=2):
        self.movies = []  # List to store movie objects
        self.max_movies_per_user = max_movies_per_user  # Maximum number of movies a user can rent

    # Method to add a movie to the store
    def add_movie(self, movie):
        self.movies.append(movie)

    # Method to remove a movie from the store
    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                self.movies.remove(movie)
                return
        raise MovieNotFoundError(title)

    # Method to list all available movies in the store
    def list_movies(self):
        for movie in self.movies:
            print(movie.title)

    # Method to rent a movie
    def rent_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                if movie.rented:
                    raise MovieAlreadyRentedError(title)
                movie.rented = True
                return
        raise MovieNotFoundError(title)

    # Method to return a rented movie
    def return_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                if not movie.rented:
                    raise ValueError(f"Movie '{title}' is not currently rented.")
                movie.rented = False
                return
        raise MovieNotFoundError(title)

# Define a class representing a movie
class Movie:
    def __init__(self, title, genre, director, release_year):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.rented = False  # Flag to indicate if the movie is currently rented

# Function to validate input as a non-empty string
def validate_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

# Function to validate input as a positive integer within a specified range
def validate_integer(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Input must be between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
rental_store = RentalStore()

# Adding movies to the store
movie1 = Movie("Inception", "Sci-Fi", "Christopher Nolan", 2010)
movie2 = Movie("The Dark Knight", "Action", "Christopher Nolan", 2008)
movie3 = Movie("Pulp Fiction", "Crime", "Quentin Tarantino", 1994)

rental_store.add_movie(movie1)
rental_store.add_movie(movie2)
rental_store.add_movie(movie3)

# Renting a movie
try:
    print("Available movies:")
    rental_store.list_movies()
    movie_title = validate_input("Enter the title of the movie you want to rent: ")
    rental_store.rent_movie(movie_title)
    print(f"Successfully rented '{movie_title}'.")
except (MovieAlreadyRentedError, MovieNotFoundError) as e:
    print(f"Error: {e}")

# Returning a movie
try:
    print("\nMovies currently rented:")
    rental_store.list_movies()
    movie_title = validate_input("Enter the title of the movie you want to return: ")
    rental_store.return_movie(movie_title)
    print(f"Successfully returned '{movie_title}'.")
except (MovieNotFoundError, ValueError) as e:
    print(f"Error: {e}")
