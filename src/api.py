from abc import ABC, abstractmethod
from typing import List, Dict
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query: str) -> List[Dict]:
        raise NotImplementedError("Subclasses must implement this method.")

class HeadHunterAPI(AbstractVacancyAPI):
    base_url = "https://api.hh.ru"
    def get_vacancies(self, query: str) -> List[Dict]:
        url = "https://api.hh.ru/vacancies"
        params = {
            'text': query,
        }

        response = requests.get(url, params=params)
        data = response.json()

        if 'items' in data:
            return data['items']
        else:
            return []


class SuperJobAPI(AbstractVacancyAPI):
    base_url = "https://api.superjob.ru/2.0"
    def __init__(self, api_key):
        self.api_key = api_key

    def get_vacancies(self, query: str) -> List[Dict]:
        url = f"{self.base_url}/vacancies/"
        params = {
            'keywords': query,
        }
        headers = {
            'X-Api-App-Id': self.api_key,
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if 'objects' in data:
            return data['objects']
        else:
            return []
        # # Параметры запроса
        # params = {
        #     'keyword': query,
        #     'town': 'Москва',  # Укажите свой город
        #     'count': 10,  # Количество вакансий для получения
        #     'page': 0,  # Номер страницы (первая страница)
        #     'api_key': self.api_key
        # }
        #
        # # Выполняем запрос
        # response = requests.get(f"{self.base_url}/vacancies/", params=params)
        #
        # # Проверяем успешность запроса
        # if response.status_code == 200:
        #     # Получаем данные в формате JSON
        #     data = response.json()
        #
        #     # Извлекаем интересующую информацию о вакансиях
        #     vacancies = []
        #     for item in data['objects']:
        #         vacancy = {
        #             'title': item['profession'],
        #             'link': item['link'],
        #             'salary': item['payment'],
        #             'description': item['candidat']
        #         }
        #         vacancies.append(vacancy)
        #
        #     return vacancies
        # else:
        #     # В случае неудачного запроса выводим ошибку
        #     print(f"Error {response.status_code}: {response.text}")
        #     return []