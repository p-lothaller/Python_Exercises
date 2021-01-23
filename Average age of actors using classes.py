
class Actor:
    
   def __init__(self, name, age):
        self.name = name
        self.age = age

class Movie:

    def __init__(self, title):
        self.name = title
        self.actors = []

    def calculate_average_age(self):
        total_age = 0
        for i in range(len(self.actors)):
            total_age += int(self.actors[i].age)

        if len(self.actors) == 0:
            return None
        else:
            return total_age/len(self.actors)
            


class MovieCollection:
    

    def __init__(self):
        self.movies = []

    def read_from_files(self, actors_filename, movies_filename):
        actor_dictionary = dict()
        with open(actors_filename, 'r') as actor_file:
            for line in actor_file:
                line= line.rsplit(":")
                actor = Actor(line[0],line[1].rstrip())
                actor_dictionary[actor.name] = actor
        with open(movies_filename, 'r') as movie_file:
            for line in movie_file:
                line = line.split(":")
                movie = Movie(line[0])
                actors_list = line[1].split(',')
                for actors in actors_list:
                    if actors.strip() in actor_dictionary:
                        movie.actors.append(actor_dictionary.get(actors.strip()))
                self.movies.append(movie)

    def get_avg_age_per_movie(self):
        dictionary = dict()
        for movie in self.movies:
            dictionary[movie.name] = movie.calculate_average_age()
        return print(dictionary)
                        

collection = MovieCollection()
collection.read_from_files("one_word.txt", "movies_small.txt")
print(collection.movies[0].actors)
