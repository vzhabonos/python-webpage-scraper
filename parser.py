import requests
from bs4 import BeautifulSoup

class Parser:
    url = ''
    content = ''

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_content(self):
        r = requests.get(self.url)
        if r.status_code == 200 and r.reason == 'OK':
            self.content = r.content;
        return self.content