#!/usr/bin/env python
# -*- coding: utf-8 -*-
from parser_base import Parser


class PetritzikisRecipeDiscoverer(Parser):

    BASE_URL = 'http://akispetretzikis.com'

    def __init__(self, lang=''):
        Parser.__init__(self)

    def fetch_menu_links(self):
        """Return a set of links from the menu"""

        self.browser.get(self.BASE_URL)
        menu = self.browser.find_element_by_id('menu')
        sub_menu = menu.find_elements_by_class_name('sub')
        all_links = [link.get_attribute('href')
                     for menu_item in sub_menu
                     for link in menu_item.find_elements_by_tag_name('a')
                     if 'javascript' not in link.get_attribute('href')
                     ]
        # remove duplicates
        return set(all_links)

    def fetch_links_in_page(self, url):
        """Return the links to recipes in paginated pages"""

        self.browser.get(url)
        main = self.browser.find_element_by_id('tag')\
            .find_elements_by_tag_name('div')
        all_links = [link.get_attribute('href')
                     for links in main
                     for link in links.find_elements_by_tag_name('a')]
        return set(all_links)

    def fetch_pages_in_page(self, url):
        """Returns the links that point to the pages
        <nav class="pagination">
            ...
            <span class="page">
                <a href="/en/tags/moschari?page=5">5</a>
            </span>
            <span class="next">
                <a rel="next" href="/en/tags/moschari?page=2">&gt;</a>
            </span>
            <span class="last">
                <a href="/en/tags/moschari?page=5">Last »</a>
            </span>
        </nav>
        """

        self.browser.get(url)
        last_link = self.browser.find_element_by_id('tag')\
            .find_element_by_tag_name('nav')\
            .find_element_by_class_name('last')\
            .find_element_by_tag_name('a')\
            .get_attribute('href')
        last_page = int(last_link[-1])

        return self._generate_pages(last_link, last_page)

    def _generate_pages(self, url, last_page):
        """Generate the pages based on a schema:
            http://domain.com/something?page={num}"""

        url_without_num = url[:-1]
        return ["{0}{1}".format(url_without_num, page)
                for page in xrange(2, last_page+1)]


class PetritzikisRecipeParser(Parser):

    def __init__(self):
        Parser.__init__(self)

    def fetch_recipe(self, url):
        """Fetch the recipe i.e. ingredients, execution, images"""

        self.browser.get(url)

        main = self.browser.find_element_by_class_name('recipe-main')
        ingredients = main.find_elements_by_class_name('text')[2]\
            .find_elements_by_tag_name('li')
        time = main.find_element_by_class_name('time')\
            .find_element_by_class_name('value').text
        ingredients_items = [item.text for item in ingredients]

        method_el = main.find_elements_by_class_name('text')[1]\
            .find_elements_by_tag_name('li')
        method_items = [item.text for item in method_el]

        images = main.find_element_by_class_name('ipad_media')\
            .find_elements_by_tag_name('img')
        images_items = [img.get_attribute('src') for img in images]

        return {
            'ingredients': ingredients_items,
            'time': time,
            'execution': method_items,
            'images': images_items
        }
