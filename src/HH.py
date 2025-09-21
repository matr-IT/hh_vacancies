import requests
from abc import ABC, abstractmethod


class HHAbstract(ABC):
    """
    Абстрактный класс для получения вакансий
    """

    def __init__(self):
        self.vacancies = []

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """
        Получение вакансий
        """
        pass


class HH(HHAbstract):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        super().__init__()

    def load_vacancies(self, keyword):
        """
        Получение вакансий через API HH
        """
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies


# Проверка работы методов класса
hh = HH()
print(hh.load_vacancies('Инженер'))