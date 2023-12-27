from abc import ABC, abstractmethod
import requests
import json
import time


class Vacancy(ABC):

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
            "area": 1,  # Код региона (1 для Москвы)
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

    def get_api(self):
        pass


class FilteredVacancies():

    @staticmethod
    def save_to_json(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
