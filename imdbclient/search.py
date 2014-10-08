# Docstrings 
# License 
from imdb import get_json
class NoKeywordException(Exception):
    def __init__(self):
        self.value = "No keyword to search"
    def __str__(self):
        return repr(self.value)

class Search:
    def __init__(self,keyword = ""):
        self.keyword = keyword
        self.results = []

    def search(self):
        if self.keyword == "":
            raise NoKeywordException
        options = {}
        options['s'] = self.keyword
        self.results = get_json(options)['Search']

    def dump_results(self):
        print self.results

    def format_results(self):
        if not self.results:
            return 
        res_string = ""
        for index,i in enumerate(self.results):
            res_string +=  "%d) %s [%s]\n Type: %s\n" %(index,i['Title'],i['Year'],i['Type'])  

        return res_string

if __name__ == "__main__":
    obj = Search("V for Vendetta")
    obj.search()
    string = obj.format_results()
    print string
