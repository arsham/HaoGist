import os
import json

try:
    import requests
except:
    from .. import requests

from .lib import util

GIST_BASE_URL = "https://api.github.com/%s"

class GistApi(object):
    """Gist API wrapper"""

    def __init__(self, token):
        self.res = None
        self._token = token
        self.headers = {
            "Accept": "application/json",
            "Authorization": "token %s" % self._token
        }

    def list(self, force=False):
        """Return a list of Gist objects."""

        self.res = requests.get(GIST_BASE_URL % "gists", 
            headers=self.headers)
        return self.res

    def get(self, url):
        self.res = requests.get(url, headers=self.headers)
        return self.res

    def retrieve(self, raw_url):
        self.headers["Accept"] = "application/text"
        self.res = requests.get(raw_url, headers=self.headers)
        self.res.encoding = "utf-8"
        return self.res

    def post(self, post_url, params):
        """POST to the web form"""
        
        print (params)
        self.res = requests.post(post_url, data=json.dumps(params), 
            headers=self.headers)
        return self.res

    def patch(self, patch_url, params):
        """POST to the web form"""

        self.res = requests.patch(patch_url, data=json.dumps(params), 
            headers=self.headers)
        return self.res

    def delete(self, url):
        self.res = requests.delete(url, headers=self.headers)
        return self.res
