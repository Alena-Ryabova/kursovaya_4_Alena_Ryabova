import json
import os
from abc import ABC, abstractmethod
import requests


# Файл для работы с площадками вакансии. Поиск, фильтрация и сохранение в JSON - файл.
class Vacancy(ABC):
    """
    Абстрактный класс с общим методом для Hh.ru и Sj.ru
    """

    @abstractmethod
    def get_api(self, search_query):
        pass


class VacancyHh(Vacancy):
    """
    Класс для работы с hh.ru
    """
    url = "https://api.hh.ru/vacancies"

    def get_api(self, search_query):
        """Метод получает вакансии,
         найденные по ключевому слову
         """

        params = {
            "area": 113,  # Код региона (1 для Москвы)
            "text": search_query,  # Ключевое слово для поиска, предоставленное пользователем
            "per_page": 10  # Количество вакансий на странице
        }
        try:
            response_hh = requests.get(url=self.url, params=params,
                                       headers={'User-Agent': 'YourApp/1.0 (alena1987.12@gmail.com)'})
            if response_hh.status_code == 200:
                data = response_hh.json()
                vacancies = data['items']
                return vacancies

        except requests.RequestException as error:
            print(f'Ошибка при получении данных. {error}')


class VacancySj(Vacancy):
    """
    Класс для работы с Sj.ru
    """
    url = "https://api.superjob.ru/2.0/vacancies"
    sj_api = os.environ.get('SJ_API')

    def get_api(self, key):
        """Метод получает вакансии,
         найденные по ключевому слову
        """
        try:
            response_sj = requests.get(url=self.url, headers={'X-Api-App-Id': self.sj_api}, params={'keyword': key})
            if response_sj.status_code == 200:
                data = response_sj.json()
                print(data)
                vacancies = data['objects']
                return vacancies

        except requests.RequestException as error:
            print(f'Ошибка при получении данных. {error}')
