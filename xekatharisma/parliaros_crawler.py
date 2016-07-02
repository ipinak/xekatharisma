#!/usr/bin/env python
# -*- coding: utf-8 -*-
from parser_base import Parser


class ParliarosRecipeDiscoverer(Parser):

    BASE_URL = "http://www.steliosparliaros.gr"

    def __init__(self):
        Parser.__init__(self)

    def fetch_menu_links(self):
        self.browser.get(self.BASE_URL)

        link_elements = self.browser.find_element_by_id('menu-menu-1')\
            .find_elements_by_tag_name('a')
        links = [link.get_attribute('href') for link in link_elements
                 if 'javascript' not in link.get_attribute('href')]

        return {
            'menu_links': set(links)
        }

    def fetch_recipe_links_in_page(self, url):
        self.browser.get(url)

        link_elements = self.browser.find_element_by_id('primary')\
            .find_element_by_class_name('subcat-articles')\
            .find_elements_by_tag_name('a')
        links = [link.get_attribute('href') for link in link_elements
                 if 'javascript' not in link.get_attribute('href')]
        return {
            'recipe_links': set(links)
        }

    def fetch_page_links_in_page(self, url):
        """Return the links that point to pages"""

        self.browser.get(url)
        link_elements = self.browser.find_element_by_class_name('catpaging')\
            .find_elements_by_tag_name('a')
        links = [link.get_attribute('href') for link in link_elements]

        return {
            'page_links': set(self.generate_pages(links))
        }

    def generate_pages(self, urls):
        page_numbers = [int(page[-2]) for page in urls]
        max_num = max(page_numbers)

        page_numbers = range(2, max_num+1)
        base_url = urls[0][:-2]
        all_pages = ["{0}{1}/".format(base_url, num)
                     for num in page_numbers]
        return all_pages


class ParliarosRecipeParser(Parser):

    def __init__(self):
        Parser.__init__(self)

    def fetch_recipe(self, url):
        self.browser.get(url)

        main = self.browser.find_element_by_id('primary')\
            .find_element_by_tag_name('article')
        title = main.find_element_by_class_name('entry-title')\
            .text

        tmp = main.find_element_by_class_name('entry-content')\
            .find_elements_by_tag_name('p')
        execution = [''.join(t.text) for t in tmp[1:]]

        time = tmp[0].text

        tmp = main.find_element_by_class_name('entry-content')\
            .find_element_by_class_name('ingredients')\
            .find_elements_by_tag_name('li')
        ingredients = [item.text for item in tmp]

        images = main.find_element_by_class_name('entry-header')\
            .find_element_by_tag_name('img').get_attribute('src')

        return {
            'title': title,
            'execution': execution,
            'ingredients': ingredients,
            'time': time,
            'images': images
        }
