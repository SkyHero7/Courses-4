import json
from .models import Vacancy

class JSONSaver:
    def __init__(self, filename='vacancies.json'):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy.__dict__)

    def save_to_json(self):
        with open(self.filename, 'w') as file:
            json.dump(self.vacancies, file)

    def load_from_json(self):
        with open(self.filename, 'r') as file:
            self.vacancies = json.load(file)

    def get_vacancies_by_salary(self, min_salary, max_salary):
        min_salary = int(min_salary)
        max_salary = int(max_salary)
        return [
            Vacancy(**vacancy) for vacancy in self.vacancies
            if vacancy.get('salary') and self.is_valid_salary(vacancy['salary'])
               and min_salary <= self.extract_salary(vacancy['salary']) <= max_salary
        ]

    @staticmethod
    def is_valid_salary(salary):
        return '-' in salary and 'руб.' in salary

    @staticmethod
    def extract_salary(salary):
        return int(salary.split('-')[0].replace(' ', ''))

    def delete_vacancy(self, title):
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy['title'] != title]
        self.save_to_json()