from abc import ABC, abstractmethod


class VacanciesAbstract(ABC):
    """
    Абстрактный класс для обработки вакансий
    """

    @abstractmethod
    def __validate_salary(self, salary_from_data):
        pass

    @abstractmethod
    def __validate_short_description(self, description_from_data):
        pass


class Vacancies(VacanciesAbstract):
    """
    Класс для обработки вакансий
    """

    __slots__ = ("name", "url", "salary", "short_description")

    name: str
    url: str
    salary: int
    short_description: str

    def __init__(self, name, url, salary, short_description):
        """
        Инициализация экземпляра
        """
        self.name = name
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.short_description = self.__validate_short_description(short_description)

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
        return self.salary < other.salary

    def __gt__(self, other):
        """
        Метод сравнения "Больше"
        """
        return self.salary > other.salary

    def __eq__(self, other):
        """
        Метод сравнения "Равно"
        """
        return (
            self.name == other.name
            and self.salary == other.salary
            and self.url == other.url
            and self.short_description == other.short_description
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
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "short_description": self.short_description,
        }

    def __str__(self):
        return f"Название: {self.name}\n"
