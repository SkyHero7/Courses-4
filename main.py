from src.api import HeadHunterAPI, SuperJobAPI
from src.models import Vacancy
from src.utils import JSONSaver


def main():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI(api_key='3276')
    json_saver = JSONSaver()

    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    for hh_vacancy in hh_vacancies:
        vacancy = Vacancy(**hh_vacancy)
        json_saver.add_vacancy(vacancy)

    for superjob_vacancy in superjob_vacancies:
        vacancy = Vacancy(**superjob_vacancy)
        json_saver.add_vacancy(vacancy)

    json_saver.save_to_json()
    json_saver.load_from_json()

    filtered_vacancies = json_saver.get_vacancies_by_salary(50000, 100000)

    for vacancy in filtered_vacancies:
        print(vacancy)


if __name__ == "__main__":
    main()