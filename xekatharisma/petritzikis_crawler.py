#!/usr/bin/env python
# -*- coding: utf-8 -*-
from parser_base import Parser


class PetritzikisCrawler(Parser):

    BASE_URL = 'http://akispetretzikis.com'

    def __init__(self, lang=''):
        Parser.__init__(self)
        self.url = "{0}/{1}".format(self.BASE_URL, lang)

    def fetch_front_page(self):
        self.read_page(self.url)
        return self.browser.find_element_by_id('homepage')

    def fetch_latest_recipes(self):
        self.read_page(self.url)
        return self.browser.find_element_by_class_name('latest_recipes')

    def read_page(self, url):
        self.browser.get(url)
