from abc import ABC, abstractmethod

import requests


class HHAbstract(ABC):
    """
    Абстрактный класс для получения вакансий
    """

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

    def load_vacancies(self, keyword: str):
        pass

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__()



    def __load_vacancies(self, keyword):
        """
        Получение вакансий через API HH
        """
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
            else:
                return 'Возникла ошибка запроса'
        return self.__vacancies



