#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from xekatharisma.petritzikis_crawler import PetritzikisRecipeDiscoverer


def test_get_food_category():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_menu_links()
    assert result is not None or len(result) < 80
    assert result.pop().startswith('http')
    p.cleanup()


def test_get_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_links_in_page(
        'http://akispetretzikis.com/en/tags/moschari')
    assert result is not None
    assert result.pop().startswith('http')
    p.cleanup()

@pytest.mark.only
def test_get_pages_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_pages_in_page(
        'http://akispetretzikis.com/en/tags/moschari')
    assert result[0].startswith('http')
    p.cleanup()


@pytest.mark.only
def test_get_more_pages_links_in_page():
    p = PetritzikisRecipeDiscoverer()
    result = p.fetch_pages_in_page(
        'http://akispetretzikis.com/en/tags/kotopoylo')
    assert result[0].startswith('http')
    print result
    p.cleanup()
