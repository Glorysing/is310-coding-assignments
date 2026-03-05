# list of favorite movies
favorite_movies = [
    ("Titanic", 1997),
    ("Avatar", 2009),
    ("The Matrix", 1999),
    ("Avengers", 2012)
]

# function to check movie release year
def check_movie(movie):
    name, year = movie
    
    if year < 2000:
        print(name + " was released before 2000")
    else:
        print(name + " was released after 2000")
        return name


# empty list
recent_movies = []


# loop through movies
for movie in favorite_movies:
    
    result = check_movie(movie)
    
    if result is not None:
        recent_movies.append(result)


# print result
print("Movies released after 2000:")
print(recent_movies)