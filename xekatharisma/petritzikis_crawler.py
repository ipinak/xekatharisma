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
        all_links = [link.get_attribute('href')\
                     for menu_item in sub_menu\
                        for link in menu_item.find_elements_by_tag_name('a')\
                            if 'javascript' not in link.get_attribute('href')
                     ]
        # remove duplicates
        links_sets = set(all_links)
        return links_sets

    def fetch_links_in_page(self, url, page=0):
        """Return the links to recipes in paginated pages"""

        self.browser.get(url)
        main = self.browser.find_element_by_id('tag')\
            .find_elements_by_tag_name('div')
        all_links = [link.get_attribute('href')\
                     for links in main
                        for link in links.find_elements_by_tag_name('a')
                    ]
        aset = set(all_links)
        return aset
