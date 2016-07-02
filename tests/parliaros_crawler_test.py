#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xekatharisma.parliaros_crawler import ParliarosRecipeDiscoverer,\
    ParliarosRecipeParser
import pytest


def test_get_menu_links():
    p = ParliarosRecipeDiscoverer()
    result = p.fetch_menu_links()
    p.cleanup()

    assert result.get('menu_links') is not None
    assert len(result.get('menu_links')) > 0


def test_get_recipe_links_in_page():
    p = ParliarosRecipeDiscoverer()
    result = p.fetch_recipe_links_in_page(
        'http://www.steliosparliaros.gr/efkola/')
    p.cleanup()

    assert result.get('recipe_links') is not None
    assert len(result.get('recipe_links')) > 0


def test_get_page_links_in_page():
    p = ParliarosRecipeDiscoverer()
    result = p.fetch_page_links_in_page(
        'http://www.steliosparliaros.gr/efkola/')
    p.cleanup()

    assert result.get('page_links', None) is not None
    assert len(result.get('page_links', None)) > 0


def test_generate_pages():
    p = ParliarosRecipeDiscoverer()
    result = p.generate_pages([
        u'http://www.steliosparliaros.gr/efkola/page/6/',
        u'http://www.steliosparliaros.gr/efkola/page/3/',
        u'http://www.steliosparliaros.gr/efkola/page/2/'])
    assert result == [
        u'http://www.steliosparliaros.gr/efkola/page/2/',
        u'http://www.steliosparliaros.gr/efkola/page/3/',
        u'http://www.steliosparliaros.gr/efkola/page/4/',
        u'http://www.steliosparliaros.gr/efkola/page/5/',
        u'http://www.steliosparliaros.gr/efkola/page/6/'
    ]


@pytest.mark.only
def test_fetch_recipe():
    p = ParliarosRecipeParser()
    result = p.fetch_recipe(
        'http://www.steliosparliaros.gr/efkola/efkola_diafora/\
efkolo-ekmek-kantaifi/')
    p.cleanup()

    assert result.get('title', None) == u'Εύκολο εκμέκ κανταΐφι'
    assert result.get('execution', None) is not None
    assert u'100 γρ. ζάχαρη' in result.get('ingredients', None)
    assert u' Προετοιμασία – παρασκευή: 50΄' in result.get('time', None)
    assert result.get('images', None).startswith('http')
