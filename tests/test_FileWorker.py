import pytest
import tempfile
import os
import json
from src.FileWorker import JsonFileWorker


@pytest.fixture
def temp_json_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tf:
        tf.write(b"[]")
        tf_path = tf.name
    yield tf_path
    os.remove(tf_path)


def test_file_creation(temp_json_file):
    os.remove(temp_json_file)
    worker = JsonFileWorker(temp_json_file)
    with open(temp_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == []

def test_add_vacancy(temp_json_file):
    worker = JsonFileWorker(temp_json_file)
    vacancy = {"name": "Dev", "salary": 1000}

    worker.add_vacancy(vacancy)
    vacancies = worker.get_vacancies()
    assert vacancy in vacancies

    worker.add_vacancy(vacancy)
    vacancies = worker.get_vacancies()
    assert vacancies.count(vacancy) == 1


def test_get_vacancies(temp_json_file):
    worker = JsonFileWorker(temp_json_file)
    vacancy1 = {"name": "Dev", "salary": 1000}
    vacancy2 = {"name": "QA", "salary": 900}
    worker.add_vacancy(vacancy1)
    worker.add_vacancy(vacancy2)

    vacancies = worker.get_vacancies()
    assert vacancy1 in vacancies
    assert vacancy2 in vacancies