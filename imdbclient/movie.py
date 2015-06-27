#!/usr/bin/python

#docs go here
# license text goes here

#version text

import imdb


def get_movie(title):
    options = {}
    options['t'] = title
    json = imdb.get_json(options)
    return json

class Movie:
	"""
		The data is stored in a dictionary. 
                keys:
                    Plot
                    Rated
                    *Response*
                    Title
                    Country
                    Writer
                    Metascore
                    imdbRating
                    Director
                    Released
                    Actors
                    Year
                    Genre
                    Awards
                    Runtime
                    Type
                    Poster
                    imdbVotes
                    imdbID

	"""
        def _get_by_title(self,title):
            options = {}
            options['t'] = title
            self.data = imdb.get_json(options)
        
        def _get_by_id(self,ID):
            options = {}
            options['i'] = ID
            self.data = imdb.get_json(options)

	def __init__(self,title = None, ID = None):
            """
                In order to initialise this object, either a title is required or imdbID is required.
                One can also specify a year while title is given. 
            """
            if (title is None) and (ID is None):
                print "Error: Either title or ID must be specified.\n No title or ID"
                del(self)
            elif (title and ID):
                print "Error: Both title and ID given."
                del(self)
            else:
                options = {}
                if title:
                    options['t'] = title
                else:
                    options['i'] = ID
                self.data = imdb.get_json(options)

        @property
        def rating(self):
            return self.data['imdbRating']

        @property
        def plot(self):
            return self.data['Plot']

        @property
        def title(self):
            return self.data['Title']

        @property
        def director(self):
            return self.data['Director']

        @property
        def actors(self):
            return self.data['Actors']

        def print_data(self):
            print "Title: %s - %s [%s]" %( self.title,self.data['Year'],self.data['Type'])
            print "*******************************"
            print "Rating   : ", self.rating
            print "Director : ", self.director
            print "Actors   : ", self.actors
            print "Plot     : \n", self.plot
            print "******************************"
             
         
if __name__ == "__main__":
    """
    testing the module with sample data
    """
    title = "V for Vendetta"
    movie = Movie(title=title)
    movie.print_data()

