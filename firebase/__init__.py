import requests
import urlparse #for urlparse and urljoin
import os #for os.path.dirname
import json #for dumps



class Firebase():
    ROOT_URL = '' #no trailing slash

    def __init__(self, root_url):
        self.ROOT_URL = root_url.rstrip('/')

    #These methods are intended to mimic Firebase API calls.

    def child(self, path):
        root_url = '%s/' % self.ROOT_URL
        url = urlparse.urljoin(root_url, path.lstrip('/'))
        return Firebase(url)

    def parent(self):
        url = os.path.dirname(self.ROOT_URL)
        #If url is the root of your Firebase, return None
        up = urlparse.urlparse(url)
        if up.path == '':
            return None #maybe throw exception here?
        return Firebase(url)

    def name(self):
        return os.path.basename(self.ROOT_URL)

    def toString(self):
        return self.__str__()
    def __str__(self):
        return self.ROOT_URL

    def set(self, value):
        return self.put(value)

    def push(self, data):
        return self.post(data)

    def remove(self):
        return self.delete()

    
    #These mirror REST API functionality

    def put(self, data):
        return self.__request('put', data = data)

    def get(self):
        return self.__request('get')

    #POST differs from PUT in that it is equivalent to doing a 'push()' in
    #Firebase where a new child location with unique name is generated and
    #returned
    def post(self, data):
        return self.__request('post', data = data)

    def delete(self):
        return self.__request('delete')


    #Private

    def __request(self, method, **kwargs):
        #Firebase API does not accept form-encoded PUT/POST data. It needs to
        #be JSON encoded.
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])

        r = requests.request(method, self.__url(), **kwargs)
        r.raise_for_status() #throw exception if error
        return r.json


    def __url(self):
        #We append .json to end of ROOT_URL for REST API.
        return '%s.json' % self.ROOT_URL
