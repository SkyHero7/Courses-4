from .utils import AbstractSaver
import json
from typing import List, Dict

class JSONSaver(AbstractSaver):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy: 'Vacancy'):
        if vacancy.validate():
            self.vacancies.append({
                'title': vacancy.title,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'description': vacancy.description
            })
            self._save_to_file()

    def get_vacancies_by_criteria(self, criteria: str) -> List[Dict]:
        # Реализация получения вакансий из JSON-файла по критериям
        filtered_vacancies = [v for v in self.vacancies if criteria in v['description']]
        return filtered_vacancies

    def delete_vacancy(self, vacancy: 'Vacancy'):
        # Реализация удаления вакансии из JSON-файла
        self.vacancies = [v for v in self.vacancies if v != {
            'title': vacancy.title,
            'link': vacancy.link,
            'salary': vacancy.salary,
            'description': vacancy.description
        }]
        self._save_to_file()

    def _save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.vacancies, file)