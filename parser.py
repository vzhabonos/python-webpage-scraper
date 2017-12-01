import requests
from bs4 import BeautifulSoup
from file_helper import FileHelper
from urllib.parse import urlparse
import re

class Parser:
    url = ''
    content = ''
    soap = None;

    def init_soap(self, content):
        self.soap = BeautifulSoup(self.content, 'html.parser')

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_content(self):
        r = requests.get(self.url)
        if r.status_code == 200 and r.reason == 'OK':
            self.content = r.content
        return self.content

    def get_nodes(self, tag_name):
        self.init_soap(self.content)
        return self.soap.find_all(tag_name)

    @staticmethod
    def form_script_url(main_url, script_url):
        if Parser.url_is_remote(script_url):
            return script_url
        host = Parser.get_host_from_url(main_url)
        url = main_url.rstrip("/")
        if Parser.is_url_absolute(script_url):
            url = host + "/" + script_url
        elif Parser.url_have_two_dots(script_url):
            url = Parser.handle_two_dots(url) + script_url.lstrip('.')
        else:
            url += "/" + script_url
        return url

    @staticmethod
    def is_url_absolute(url):
        if isinstance(url, str) and url[0] == '/':
            return True
        else:
            return False

    @staticmethod
    def url_have_two_dots(url):
        if isinstance(url, str) and url[0] == '.' and url[1] == '.':
            return True
        else:
            return False

    @staticmethod
    def handle_two_dots(url):
        routes = url.split('/');
        del routes[len(routes) - 1]
        del routes[len(routes) - 1]
        return "/".join(routes)

    @staticmethod
    def get_host_from_url(url):
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain


    @staticmethod
    def get_content_from_url(url):
        r = requests.get(url)
        content = ''
        if r.status_code == 200 and r.reason == 'OK':
            content = r.content
        return content

    @staticmethod
    def url_is_remote(url):
        return re.compile('^(https://|http://|//)', re.IGNORECASE).search(url)