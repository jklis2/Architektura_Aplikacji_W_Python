# -*- coding: utf-8 -*-
import pytest
from sort_numbers import sort_numbers

@pytest.fixture(params=[
    ([5, 2, 8, 1, 3], [1, 2, 3, 5, 8]),  # Przypadek: Sortowanie w kolejności rosnącej
    ([], []),                            # Przypadek: Obsługa pustej listy
    ([5], [5]),                          # Przypadek: Lista z jednym elementem
    ([5, 2, 8, 1, 3, 5, 2], [1, 2, 2, 3, 5, 5, 8])  # Przypadek: Lista zawierająca duplikaty
])
def numbers(request):
    return request.param

def test_sort_numbers(numbers):
    input_list, expected_output = numbers
    sorted_numbers = sort_numbers(input_list)
    assert sorted_numbers == expected_output
