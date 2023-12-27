from src.utils import VacancyHh, VacancySj, FilteredVacancies


def user_interaction():
    print("Выберите площадку для сортировки вакансий: \n"
          "1. HeadHunter\n"
          "2. SuperJob")
    user_choice_site = input("Введите значение  ")

    user_choice_sort = input("Введите ключевое слово для фильтрации  ")

    vacancy = VacancyHh()
    vacancies_filter = vacancy.get_api(user_choice_sort)
    vacancy_filtered = FilteredVacancies()
    if vacancies_filter:
        for one in vacancies_filter:
            print(one['name'])

        # Сохраняем вакансии в файл JSON
        vacancy_filtered.save_to_json('vacancies.json', vacancies_filter)
    else:
        print("Вакансий не найдено.")


if __name__ == '__main__':
    user_interaction()
