import pytest
from src.Vacancies import Vacancies

def test_validate_salary():
    v1 = Vacancies("name", "url", {"from": 1000, "to": 2000}, "desc")
    assert v1.salary == 1000

    v2 = Vacancies("name", "url", {"to": 1500}, "desc")
    assert v2.salary == 1500

    v3 = Vacancies("name", "url", {}, "desc")
    assert v3.salary == 0

    v4 = Vacancies("name", "url", None, "desc")
    assert v4.salary == 0

def test_validate_short_description():
    v1 = Vacancies("name", "url", {"from": 1000}, "some description")
    assert v1.short_description == "some description"

    v2 = Vacancies("name", "url", {"from": 1000}, None)
    assert v2.short_description == "Отсутствует описание вакансии"

    v3 = Vacancies("name", "url", {"from": 1000}, "")
    assert v3.short_description == "Отсутствует описание вакансии"

def test_comparison_methods():
    v1 = Vacancies("name1", "url1", {"from": 1000}, "desc")
    v2 = Vacancies("name2", "url2", {"from": 2000}, "desc")

    assert (v1 < v2) is True
    assert (v2 > v1) is True
    assert (v1 == v1) is True
    assert (v1 == v2) is False

def test_from_dict():
    data = {
        "name": "Vacancy name",
        "url": "https://example.com",
        "salary": {"from": 3000},
        "snippet": {"responsibility": "Do something"},
    }
    vacancy = Vacancies.from_dict(data)
    assert vacancy.name == "Vacancy name"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary == 3000
    assert vacancy.short_description == "Do something"

def test_to_dict():
    vacancy = Vacancies(
        "Vacancy",
        "https://example.com",
        {"from": 1000},
        "Description",
    )
    expected = {
        "name": "Vacancy",
        "url": "https://example.com",
        "salary": 1000,
        "short_description": "Description",
    }
    assert vacancy.to_dict() == expected

def test_str_method():
    vacancy = Vacancies("Job", "https://job.url", {"from": 1000}, "Desc")
    expected_str = "Название: Job\nСсылка на вакансию: https://job.url"
    assert str(vacancy) == expected_str