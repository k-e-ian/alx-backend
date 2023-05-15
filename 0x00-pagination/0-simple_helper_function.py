#!/usr/bin/env python3.8
'''
File: 0-simple_helper_function.py
'''


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns the start and end indexes of a list for a given page and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
