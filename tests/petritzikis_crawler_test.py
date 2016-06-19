#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xekatharisma.petritzikis_crawler import PetritzikisCrawler


def test_get_front_page():
    p = PetritzikisCrawler()
    result = p.fetch_front_page()
    assert result != [] or result is not None

    print result
    p.cleanup()


def test_get_latest_recipes_page():
    p = PetritzikisCrawler()
    result = p.fetch_latest_recipes()
    assert result != [] or result is not None

    print result
    p.cleanup()
