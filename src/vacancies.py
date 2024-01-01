import json


class FilteredVacancies():

    @staticmethod
    def save_to_json(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def open_json():

        with open('vacancies.json', 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
            return data_dict

    def __init__(self):
        self.profession = None
        self.salary = None
        self.company = None
        self.url_vacancy = None
        self.requirement = None
        self.responsibility = None
        self.vacancy_list = []

    def identify_vacancies(self):
        for one in self.open_json():
            if 'name' in one:
                self.profession = one["name"]
            elif 'profession' in one:
                self.profession = one["profession"]
            else:
                print("Key 'name' does not exist in the dictionary")

            if 'salary' in one:
                self.salary = one['salary']
            elif 'profession' in one:
                pass
            else:
                print("Key 'salary' does not exist in the dictionary")

            if 'employer' in one:
                self.company = one['employer']['name']
            elif 'client' in one:
                self.company = one['client']['title']
            else:
                print("Key 'employer' does not exist in the dictionary")

            if 'snippet' in one:
                self.requirement = one['snippet']['requirement']
                self.responsibility = one['snippet']['responsibility']
            elif 'profession' in one:
                pass
            else:
                print("Key 'snippet' does not exist in the dictionary")

            if 'alternate_url' in one:
                self.url_vacancy = one['alternate_url']
            elif 'profession' in one:
                pass
            else:
                print("Key 'alternate_url' does not exist in the dictionary")

            vacancy_dict = {
                'Название вакансии:': self.profession,
                'Зарплата:': self.salary,
                'Компания:': self.company,
                'Требования и обязанности:': self.requirement,
                'Описание:': self.responsibility,
                'Ссылка на вакансию:': self.url_vacancy
            }
            self.vacancy_list.append(vacancy_dict)
        sorted_from_salary = sorted(self.vacancy_list,
                                    key=lambda x: x.get('Зарплата:', {}).get('from') if isinstance(x.get('Зарплата:'),
                                                                                                   dict) else 0
                                    )
        print(sorted_from_salary)
        return sorted_from_salary

    def display_vacancies(self):
        for one_vacancy in self.identify_vacancies():
            if one_vacancy.get('Зарплата:') is not None:
                salary_from = one_vacancy['Зарплата:'].get('from')
                if salary_from is not None:
                    print(f"Название вакансии: {one_vacancy['Название вакансии:']}\n"
                          f"Зарплата: {salary_from}\n"
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
            else:
                print(f"Название вакансии: {one_vacancy['Название вакансии:']}\n"
                      f"Зарплата: информация отсутствует\n"
                      f"Компания: {one_vacancy['Компания:']}\n"
                      f"Требования и обязанности: {one_vacancy['Требования и обязанности:']}\n"
                      f"Описание: {one_vacancy['Описание:']}\n"
                      f"Ссылка на вакансию: {one_vacancy['Ссылка на вакансию:']}\n")




