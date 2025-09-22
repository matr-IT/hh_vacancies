import pytest
from unittest.mock import patch, MagicMock
from src.HH import HH

def make_mock_response(items, status_code=200):
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = {"items": items}
    mock_resp.raise_for_status.return_value = None
    return mock_resp

@patch("src.HH.requests.get")
def test_load_vacancies_single_page(mock_get):
    vacancies_page = [{"id": 1, "name": "Vacancy1"}, {"id": 2, "name": "Vacancy2"}]
    mock_get.return_value = make_mock_response(vacancies_page)

    hh = HH()
    results = hh.load_vacancies("python")
    assert mock_get.call_count == 20
    expected = vacancies_page * 20
    assert results == expected
    assert hh.vacancies == expected
    for call in mock_get.call_args_list:
        assert call[1]["params"]["text"] == "python"

