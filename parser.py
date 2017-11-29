import requests
from bs4 import BeautifulSoup

class Parser:
    url = ''
    content = ''
    soap = None;

    def init_soap(self):
        if not isinstance(self.soap, BeautifulSoup):
            self.soap = BeautifulSoup(self.content, 'html.parser')

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_content(self):
        r = requests.get(self.url)
        if r.status_code == 200 and r.reason == 'OK':
            self.content = r.content
            self.init_soap()
        return self.content

    def get_nodes(self, tag_name):
        return self.soap.find_all(tag_name)