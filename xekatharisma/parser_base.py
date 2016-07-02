#!/usr/bin/env python
# -*- coding: utf-8 -*
# TODO: switch to phantomjs when the bug is fixed
from selenium.webdriver import PhantomJS


class Parser(object):

    def __init__(self):
        self.browser = PhantomJS()

    def cleanup(self):
        self.browser.quit()
