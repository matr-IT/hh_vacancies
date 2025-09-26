from abc import ABC


class VacanciesAbstract(ABC):
    """
    Абстрактный класс для обработки вакансий
    """

    pass


class Vacancies(VacanciesAbstract):
    """
    Класс для обработки вакансий
    """

    __slots__ = ("name", "url", "salary", "short_description")

    __name: str
    __url: str
    __salary: int
    __short_description: str

    def __init__(self, name, url, salary, short_description):
        """
        Инициализация экземпляра
        """
        super().__init__()
        self.__name = name
        self.__url = url
        self.__salary = self.__validate_salary(salary)
        self.__short_description = self.__validate_short_description(short_description)

    def __validate_salary(self, salary_from_data) -> int:
        """
        Метод валидации зарплаты
        """
        if not salary_from_data:
            return 0
        if salary_from_data.get("from"):
            return int(salary_from_data.get("from"))
        return salary_from_data.get("to", 0)

    def __validate_short_description(self, description_from_data) -> str:
        """
        Метод валидации краткого описания
        """
        if description_from_data:
            return description_from_data
        else:
            return "Отсутствует описание вакансии"

    def __lt__(self, other):
        """
        Метод сравнения "Меньше"
        """
        return self.__salary < other.__salary

    def __gt__(self, other):
        """
        Метод сравнения "Больше"
        """
        return self.__salary > other.__salary

    def __eq__(self, other):
        """
        Метод сравнения "Равно"
        """
        return (
            self.__name == other.__name
            and self.__salary == other.__salary
            and self.__url == other.__url
            and self.__short_description == other.__short_description
        )

    @classmethod
    def from_dict(cls, dict_vacancies):
        """
        Метод преобразования словаря в экземпляр класса
        """
        return cls(
            name=dict_vacancies.get("name", ""),
            url=dict_vacancies.get("url", ""),
            salary=dict_vacancies.get("salary"),
            short_description=dict_vacancies.get("snippet", {}).get(
                "responsibility", ""
            ),
        )

    def to_dict(self):
        """
        Метод преобразования экземпляра класса в словарь
        """
        return {
            "name": self.__name,
            "url": self.__url,
            "salary": self.__salary,
            "short_description": self.__short_description,
        }

    def __str__(self):
        return f"Название: {self.__name}\nСсылка на вакансию: {self.__url}\nЗарплата: {self.__salary/100}"
