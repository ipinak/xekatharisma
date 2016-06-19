#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from xekatharisma.petritzikis_crawler import PetritzikisRecipeDiscoverer,\
    PetritzikisRecipeParser


def test_get_food_category():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_menu_links()
    p.cleanup()

    assert result is not None or len(result) < 80
    assert result.pop().startswith('http')
    print(result)


def test_get_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_links_in_page(
        'http://akispetretzikis.com/en/tags/moschari')
    p.cleanup()

    assert result is not None
    assert result.pop().startswith('http')
    print(result)


def test_get_pages_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_pages_in_page(
        'http://akispetretzikis.com/en/tags/moschari')
    p.cleanup()

    assert result[0].startswith('http')
    print(result)


def test_get_more_pages_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_pages_in_page(
        'http://akispetretzikis.com/en/tags/kotopoylo')
    p.cleanup()

    assert result[0].startswith('http')
    print(result)


@pytest.mark.only
def test_get_recipt_in_page():
    p = PetritzikisRecipeParser()
    url = 'http://akispetretzikis.com/en/categories/almyres-pites-tartes/agglikh-kotopita'
    result = p.fetch_recipe(url)
    p.cleanup()

    ing = result.get('ingredients', None)
    time = result.get('time', None)
    ex = result.get('execution', None)
    imgs = result.get('images', None)

    assert ing is not None and time is not None
    assert ing[0] is not None and '' not in ing
    assert ex[0] is not None and '' not in ex
    assert imgs[0] is not None and '' not in imgs
    assert imgs[0].startswith('http://akis')
    print(result)
