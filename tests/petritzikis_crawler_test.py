#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        'http://akispetretzikis.com/en/tags/moschari',
        0
    )
    assert result is not None
    assert result.pop().startswith('http')
    print result
    p.cleanup()

