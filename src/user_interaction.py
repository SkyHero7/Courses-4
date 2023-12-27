from api import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from utils import JSONSaver

def user_interaction():
    app_key = "your_headhunter_app_key"
    app_id = "your_superjob_app_id"

    hh_api = HeadHunterAPI(app_key)
    sj_api = SuperJobAPI(app_id)

    json_saver = JSONSaver()

    platform = input("Choose platform (hh, sj, or both): ")

    if platform in ["hh", "both"]:
        hh_query = input("Enter your HeadHunter query: ")
        hh_vacancies = hh_api.get_vacancies(hh_query)
        hh_vacancies = [Vacancy(id=vacancy["id"], name=vacancy["name"], salary=vacancy["salary"], employer=vacancy["employer"]["name"]) for vacancy in hh_vacancies]
        json_saver.save_to_json([vars(vacancy) for vacancy in hh_vacancies], "hh_vacancies.json")

    if platform in ["sj", "both"]:
        sj_query = input("Enter your SuperJob query: ")
        sj_vacancies = sj_api.get_vacancies(sj_query)
        sj_vacancies = [Vacancy(id=vacancy["id"], name=vacancy["profession"], salary=vacancy["payment"], employer=vacancy["firm_name"]) for vacancy in sj_vacancies]
        json_saver.save_to_json([vars(vacancy) for vacancy in sj_vacancies], "sj_vacancies.json")

if __name__ == "__main__":
    user_interaction()
