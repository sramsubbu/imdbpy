# Docs required
# License text required

import urllib
import json

apiurl = "http://www.omdbapi.com/"
supported_options = ["i","s","t","y"]

def is_internet_available():
    """
        Checks if internet connection is available
    """
    import socket
    REMOTE_SERVER = "www.google.com"
    try:
        #checks if the hostname can be resolved
        host = socket.gethostbyname(REMOTE_SERVER)
        
        #checks if the host is reachable
        s = socket.create_connection((host,80))
        return True
    except Exception as e:
        pass
    return False
    

class IMDb: 
    def __init__(self,options = {}):
        self.options = options
        self.url = ""

    @property
    def options(self):
        return self.options

    @options.setter
    def options(self,value):
        for i in value:
            self.options[i] = value[i]

    def build_url(self):
        #No option available
        url = apiurl
        if not self.options:
            print "Option required"
            return False
        prefix = "?"
        for i in self.options:
            url = url+prefix+i+"="+self.options[i]
            prefix = "&"
        
        self.url = url
        return True
    
    def print_url(self):
        print self.url

    def get_json(self):
        jsontext = urllib.urlopen(self.url).read()
        out = json.loads(jsontext) 
        return out

def get_json(options):
    if options is None:
        return None
    obj = IMDb(options)
    if obj.build_url():
        return obj.get_json()


    

if __name__ == "__main__":
    print "Internet connection: ",is_internet_available()
    print "Getting the details of 'The Godfather'"
    options = {}
    options["t"] = "The Godfather"
    options['y'] = "1972"
    obj = IMDb(options)
    obj.build_url()
    obj.print_url()
    results = obj.get_json()
    print results

    print "Searching for 'V for Vendetta'"
    options = {}
    options['s'] = "V for Vendetta"
    print get_json(options)

        
        
        
