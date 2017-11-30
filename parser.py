import requests
from bs4 import BeautifulSoup
from file_helper import FileHelper
from urllib.parse import urlparse
from pprint import pprint

class Parser:
    url = ''
    content = ''
    soap = None;

    def __init__(self):
        self.init_soap()

    def init_soap(self):
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
        return self.soap.find_all(tag_name)

    @staticmethod
    def form_script_url(main_url, script_url):
        host = Parser.get_host_from_url(main_url)
        pprint(host)
        url = main_url.rstrip("/")
        print(url)
        if FileHelper.is_path_absolute(script_url):
            url += script_url
        else:
            url += "/" + script_url

    @staticmethod
    def get_host_from_url(url):
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        print(domain)


    @staticmethod
    def get_content_from_url(url):
        r = requests.get(url)
        content = ''
        if r.status_code == 200 and r.reason == 'OK':
            content = r.content
        return content
