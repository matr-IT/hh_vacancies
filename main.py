from src.FileWorker import JsonFileWorker
from src.HH import HH
from src.Vacancies import Vacancies
from src.vacancies_sorting import vacancies_sorting


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    api_hh = HH()
    file_worker_json = JsonFileWorker()
    user_input = input("Требуется ввод: ")

    vacancies_hh = api_hh.load_vacancies(user_input)

    vacancy_examples = []
    for vacancy in vacancies_hh:
        vac = Vacancies.from_dict(vacancy)
        vacancy_examples.append(vac)

    vacancy_dicts = []
    for vacancy in vacancy_examples:
        vacancy_dicts.append(vacancy.to_dict())

    for vacancy in vacancy_dicts:
        file_worker_json.add_vacancy(vacancy)

    vacancies_amount = int(input("Сколько вакансий необходимо вывести?\n"))
    top_vacancies = vacancies_sorting(vacancy_examples)[:vacancies_amount]
    for vacancy in top_vacancies:
        print(vacancy)


user_interaction()
