#!/usr/bin/env python3
"""
This module contains a function that calculates the start and end index
for a slice from a list to implement pagination.
"""


import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page from the dataset.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the requested page.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]
