import pytest
from src.vacancies_sorting import vacancies_sorting


def test_sorting_integers():
    data = [3, 1, 4, 2]
    sorted_data = vacancies_sorting(data)
    assert sorted_data == [4, 3, 2, 1]


def test_sorting_strings():
    data = ["banana", "apple", "cherry"]
    sorted_data = vacancies_sorting(data)
    assert sorted_data == ["cherry", "banana", "apple"]


def test_sorting_empty_list():
    data = []
    sorted_data = vacancies_sorting(data)
    assert sorted_data == []