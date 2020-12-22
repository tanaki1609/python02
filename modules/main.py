from pprint import pprint
import random
from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url):
        self.html = BeautifulSoup(requests.get(url).text, 'lxml')