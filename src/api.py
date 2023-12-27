from abc import ABC, abstractmethod
from typing import List, Dict
from urllib.parse import urlencode
import requests
from .models import Vacancy

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query: str) -> List[Dict]:
        raise NotImplementedError("Subclasses must implement this method.")

class HeadHunterAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        params = {
            "text": keyword,
            "api_key": self.api_key,
        }
        response = requests.get(self.base_url, params=params)

        return response.json()



class SuperJobAPI:
    def __init__(self, app_id, secret_key):
        self.app_id = app_id
        self.secret_key = secret_key
        self.base_url = "https://api.superjob.ru/2.33"

    def get_vacancies(self, keyword):
        params = {
            "keyword": keyword,
            "X-Api-App-Id": self.app_id
        }
        vacancies_data = self._fetch_vacancies_data(keyword)

        vacancies = [Vacancy(**data) for data in vacancies_data]
        return vacancies

    def _fetch_vacancies_data(self, keyword):
        data = [
            {'title': 'Python Developer', 'salary': '100,000 руб.', 'description': '...'},
            {'title': 'Data Scientist', 'salary': '120,000 руб.', 'description': '...'},
        ]
        return data