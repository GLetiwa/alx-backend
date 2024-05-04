#!/usr/bin/env python3
"""
This module contains a function that calculates the start and end index
for a slice from a list to implement pagination and a Server class
to paginate a database of popular baby names.
"""


import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int, total_items: int) -> tuple:
    """
    Calculate the start and end index for pagination of a list.

    Args:
        page (int): The current page number in the pagination sequence.
        page_size (int): The number of items per page.
        total_items (int): The total number of items in the dataset.

    Returns:
        tuple: A tuple containing the start and end index for the page.
    """
    total_pages = math.ceil(total_items / page_size)
    start_index = (page - 1) * page_size
    end_index = min(start_index + page_size, total_items)
    return (start_index, end_index, total_pages)


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

        start, end, total_pages = index_range(page, page_size, len(
            self.dataset()))
        dataset = self.dataset()
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Return paginated dataset along with hypermedia metadata.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, any]: A dictionary containing paginated dataset
                along with hypermedia metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        start, end, total_pages = index_range(page, page_size, total_items)
        next_page = page + 1 if end < total_items else None
        prev_page = page - 1 if start > 0 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
