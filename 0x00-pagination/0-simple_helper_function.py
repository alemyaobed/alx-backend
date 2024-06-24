#!/usr/bin/env python3
'''
Write a function named index_range that takes two integer arguments page
and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
'''
from typing import Union, Tuple


def index_range(page: int, page_size: int) -> Tuple[Union[int, int]]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    # Calculate the start index
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    # Return the calculated indices as a tuple
    return start_index, end_index
