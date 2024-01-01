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
            elif 'profession' in one:
                pass
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
                print("Key 'snippet' does not exist in the dictionary")

            vacancy_dict = {
                'Название вакансии:': self.profession,
                'Зарплата:': self.salary,
                'Компания:': self.company,
                'Требования и обязанности:': self.requirement,
                'Описание:': self.responsibility,
                'Ссылка на вакансию:': self.url_vacancy
            }
            self.vacancy_list.append(vacancy_dict)
            print(self.vacancy_list)
            return self.vacancy_list
