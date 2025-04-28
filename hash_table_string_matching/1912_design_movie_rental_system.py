"""
LeetCode Question #1912: Design Movie Rental System

Problem Statement:
You are tasked with implementing a movie rental system that supports the following operations:

1. **Search**: Given a query `search(query)`, return a list of movies that match the query. Each movie has a unique ID and a title. The result should be sorted by movie ID in ascending order.

2. **Rent**: Given a movie ID `rent(movie_id)`, mark the movie as rented. If the movie is already rented, return an error.

3. **Return**: Given a movie ID `return(movie_id)`, mark the movie as available. If the movie is not rented, return an error.

4. **Get Rented Movies**: Return a list of all rented movies sorted by movie ID in ascending order.

Implement the system with efficient time and space complexity.

Constraints:
- The number of movies is at most 10^5.
- Each movie ID is unique.
- Each movie title is a string of length at most 100.
"""

# Python Solution
class MovieRentalSystem:
    def __init__(self):
        self.movies = {}  # Dictionary to store movie details {movie_id: {"title": str, "rented": bool}}
        self.rented_movies = set()  # Set to store rented movie IDs

    def add_movie(self, movie_id: int, title: str) -> None:
        """Add a movie to the system."""
        if movie_id not in self.movies:
            self.movies[movie_id] = {"title": title, "rented": False}

    def search(self, query: str) -> list:
        """Search for movies matching the query."""
        result = []
        for movie_id, details in self.movies.items():
            if query.lower() in details["title"].lower():
                result.append(movie_id)
        return sorted(result)

    def rent(self, movie_id: int) -> str:
        """Rent a movie by its ID."""
        if movie_id not in self.movies:
            return "Movie not found"
        if self.movies[movie_id]["rented"]:
            return "Movie already rented"
        self.movies[movie_id]["rented"] = True
        self.rented_movies.add(movie_id)
        return "Movie rented successfully"

    def return_movie(self, movie_id: int) -> str:
        """Return a rented movie by its ID."""
        if movie_id not in self.movies:
            return "Movie not found"
        if not self.movies[movie_id]["rented"]:
            return "Movie is not rented"
        self.movies[movie_id]["rented"] = False
        self.rented_movies.remove(movie_id)
        return "Movie returned successfully"

    def get_rented_movies(self) -> list:
        """Get a list of all rented movies sorted by movie ID."""
        return sorted(self.rented_movies)


# Example Test Cases
if __name__ == "__main__":
    system = MovieRentalSystem()
    
    # Adding movies
    system.add_movie(1, "The Matrix")
    system.add_movie(2, "Inception")
    system.add_movie(3, "Interstellar")
    system.add_movie(4, "The Matrix Reloaded")
    
    # Searching movies
    print(system.search("Matrix"))  # Output: [1, 4]
    print(system.search("Inception"))  # Output: [2]
    
    # Renting movies
    print(system.rent(1))  # Output: "Movie rented successfully"
    print(system.rent(1))  # Output: "Movie already rented"
    print(system.rent(5))  # Output: "Movie not found"
    
    # Returning movies
    print(system.return_movie(1))  # Output: "Movie returned successfully"
    print(system.return_movie(1))  # Output: "Movie is not rented"
    
    # Getting rented movies
    print(system.rent(2))  # Output: "Movie rented successfully"
    print(system.get_rented_movies())  # Output: [2]

"""
Time and Space Complexity Analysis:

1. **add_movie(movie_id, title)**:
   - Time Complexity: O(1) (Dictionary insertion is O(1) on average)
   - Space Complexity: O(1) per movie added.

2. **search(query)**:
   - Time Complexity: O(n * m), where `n` is the number of movies and `m` is the average length of movie titles.
   - Space Complexity: O(k), where `k` is the number of matching movies.

3. **rent(movie_id)**:
   - Time Complexity: O(1) (Dictionary lookup and set insertion are O(1) on average)
   - Space Complexity: O(1).

4. **return_movie(movie_id)**:
   - Time Complexity: O(1) (Dictionary lookup and set removal are O(1) on average)
   - Space Complexity: O(1).

5. **get_rented_movies()**:
   - Time Complexity: O(r * log(r)), where `r` is the number of rented movies (due to sorting).
   - Space Complexity: O(r) (to store the sorted list).

Topic: Hash Table, String Matching
"""