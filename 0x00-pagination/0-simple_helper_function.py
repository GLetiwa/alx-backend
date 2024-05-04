#!/usr/bin/env python3
"""
This module contains a function that calculates the start and end index
for a slice from a list to implement pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination of a list.

    Args:
    page (int): The current page number in the pagination sequence.
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start and end index for the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
