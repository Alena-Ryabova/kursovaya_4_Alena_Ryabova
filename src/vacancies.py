import json


class FilteredVacancies():

    @staticmethod
    def save_to_json(file_name, data):
        """
        Сохранение полученного списка вакансий в файл
        """
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def __init__(self):
        self.profession = None
        self.salary = None
        self.company = None
        self.url_vacancy = None
        self.requirement = None
        self.responsibility = None
        self.vacancy_list = []
        self._open_json()

    def _open_json(self):
        """
        Открываем файл для чтения
        """
        with open('vacancies.json', 'r', encoding='utf-8') as f:
            self.data_dict = json.load(f)

    def identify_vacancies(self):
        """
        запись в словарь вакансий с наиболее сокращенной информацией
        """
        for one in self.data_dict:

            if 'salary' in one:
                self.profession = one["name"]
                if one['salary'] and one['salary']['from'] is not None:
                    self.salary = one['salary']['from']
                else:
                    self.salary = 0
                self.company = one['employer']['name']
                self.requirement = one['snippet']['requirement']
                self.responsibility = one['snippet']['responsibility']
                self.url_vacancy = one['alternate_url']
            elif 'profession' in one:
                self.profession = one["profession"]
                self.salary = one['payment_from']
                self.company = one['client'].get('title', 'Нет информации')
                self.requirement = ''
                self.responsibility = one['candidat']
                self.url_vacancy = one['link']
            else:
                print("Key 'name' does not exist in the dictionary")

            vacancy_dict = {
                'Название вакансии:': self.profession,
                'Зарплата:': self.salary,
                'Компания:': self.company,
                'Требования и обязанности:': self.requirement,
                'Описание:': self.responsibility,
                'Ссылка на вакансию:': self.url_vacancy
            }
            self.vacancy_list.append(vacancy_dict)

        return self.vacancy_list

    def sorted_vacancy(self):
        """
        Сортировка вакансий по зарплате
        """
        sorted_vacancy = sorted(self.identify_vacancies(), key=lambda x: x['Зарплата:'], reverse=True)
        return sorted_vacancy

    def display_vacancies(self, number):
        """
        Вывод результата в консоль
        """
        print("-*" * 100)  # Разделительная линия
        count = 0  # Счетчик для колличества вывода вакансий
        for one_vacancy in self.sorted_vacancy():
            if count < int(number):  # Проверка, что счетчик меньше выбранного пользователем

                if one_vacancy['Зарплата:'] != 0:
                    print(f"Название вакансии: {one_vacancy['Название вакансии:']}\n"
                          f"Зарплата от: {one_vacancy['Зарплата:']}\n"
                          f"Компания: {one_vacancy['Компания:']}\n"
                          f"Требования и обязанности: {one_vacancy['Требования и обязанности:']}\n"
                          f"Описание: {one_vacancy['Описание:']}\n"
                          f"Ссылка на вакансию: {one_vacancy['Ссылка на вакансию:']}\n")
                else:
                    print(f"Название вакансии: {one_vacancy['Название вакансии:']}\n"
                          f"Зарплата: информация отсутствует\n"
                          f"Компания: {one_vacancy['Компания:']}\n"
                          f"Требования и обязанности: {one_vacancy['Требования и обязанности:']}\n"
                          f"Описание: {one_vacancy['Описание:']}\n"
                          f"Ссылка на вакансию: {one_vacancy['Ссылка на вакансию:']}\n")

                count += 1

                if one_vacancy is not self.sorted_vacancy()[-1]:
                    print("-*" * 100)  # Разделительная линия
            else:
                break
