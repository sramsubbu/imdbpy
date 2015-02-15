from sys import argv
import argparse
from movie import Movie
VERSION = "0.1.0"

def print_version():
    print  "%s %s\n%s" %(prog_name, version,license)

def main():
    parser = argparse.ArgumentParser(description = "get imdb data in the command line")
    parser.add_argument("-V","--version", action = "version", version = "%(prog)s version 0.1.0")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s","--search", action = "store_true", help= "display the imdb search results for the movie")
    group.add_argument("-r","--rating",action = "store_true", help = "display the rating of the movie")
    group.add_argument("-d","--description",action = "store_true",help = "display the plot of the movie")
    group.add_argument("-A", "--actors",action = "store_true",help = "display the actors in the movie")
    parser.add_argument("title" )
    args = parser.parse_args()

    if args.search:
        search(args.title)
    else:
        movie = Movie(args.title)
        if args.rating:
            print "Rating: ", movie.rating
        elif args.description:
            print "Plot: ",movie.plot
        elif args.actors:
            print "Actors:",movie.actors
        else:
            movie.print_data()

def search(title):
    print "Search results for %s:" %title
    print "not yet implemented"

def my_movie(title,option):
    m = Movie(title)
    if not option:
        m.print_data()
    elif option == "Rating":
        print "%s\nRating: %s" %(title,m.rating)


if __name__ == "__main__":
    ret = main()
    exit(ret)
