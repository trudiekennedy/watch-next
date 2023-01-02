# === IMPORTS ===
import spacy

nlp = spacy.load("en_core_web_md")  # loads spaCY model.

# === GLOBAL VARIABLES ===
# Declare a dictionary to store movie objects.
movie_dict = {}


# === CLASS ===
class Movie:
    def __init__(self, title, description):
        self.title = title  # Movie title.
        self.description = description  # Movie description.
        self.description_doc = nlp(description)  # Movie description doc passed through nlp.


# === FUNCTIONS ===
# Import file
def import_file(filename):
    """ Imports file as a read file, separates each line into the title and description and saves it as a "Movie" object
    in "movies_dict" with a numerical key.
    If file is not found, display an error message to user.
    """
    try:
        with open(filename, "r") as movie_file:
            key_number = 1      # Will be the key in "movie_dict".

            # For each line in the file, splits by " :" to separate title & description then add as an object to dict.
            for line in movie_file:
                title, description = line.strip().split(" :")
                movie_dict[key_number] = Movie(title, description)
                key_number += 1     # Adds 1 so that the key for the next object in movie_dict is different.

    # Present an error message if the file isn't found.
    except FileNotFoundError:
        return f"File not found. Please check file and try again."


# FIND SIMILAR
def find_similar(description):
    """
    This function compares the passed description with the description of the Movie objects stored in "movie_dict"
    using spaCY similarity to find which object's description is most similar to the one provided.
    :param: description: A description of a movie that has been watched.
    :return: The title of a Movie object with the most similar description.
    """
    watched_description_doc = nlp(description)
    highest_similarity_score = 0  # Variable to store the highest score.
    most_similar_movie = ""  # Variable to store the movie with the highest score.

    # Gets a similarity score between passed description and each movie description of the Movie objects in "movie_dict"
    for movie in movie_dict.values():
        similarity_score = watched_description_doc.similarity(movie.description_doc)

        # If score is higher than the one stored in "highest_similarity_score", the variable is updated with the
        # highest score & the movie is stored in the "most_similar_movie" variable.
        if similarity_score > highest_similarity_score:
            highest_similarity_score = similarity_score
            most_similar_movie = movie

    # Returns the title of the "most_similar_movie".
    return f"If you liked '{watched_movie_title}', you might enjoy '{most_similar_movie.title}'..."


def recommendation_box(text):
    """
    Prints a fancy formatted box for the movie recommendation.
    """
    print(':o' + '-' * (len(text) + 2) + 'o:')
    print(' ' + 'NEED SOMETHING NEW TO WATCH?' + ' ')
    print(' ' + text + ' ')
    print(':o' + '-' * (len(text) + 2) + 'o:')


# === CODE ===
# Variables containing details of watched movie.
watched_movie_title = "Planet Hulk"
watched_movie_description = 'Will he save their world or destroy it? ' \
                            'When the Hulk becomes too dangerous for the Earth,' \
                            'the Illuminati trick Hulk into a shuttle and launch him into space to a planet ' \
                            'where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar' \
                            'where he is sold into slavery and trained as a gladiator'

# Import the file containing the movies.
import_file("movies.txt")

# Store the result of "find_similar" function in a variable called "recommendation".
recommendation = find_similar(watched_movie_description)

# Presents the recommendation in a formatted box.
recommendation_box(recommendation)
