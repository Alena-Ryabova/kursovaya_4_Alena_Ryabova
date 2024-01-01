from src.utils import VacancyHh, VacancySj
from src.vacancies import FilteredVacancies


def user_interaction():
    print("Выберите площадку для сортировки вакансий: \n"
          "1. HeadHunter\n"
          "2. SuperJob")
    user_choice_site = input("Введите значение  ")

    user_choice_sort = input("Введите ключевое слово для фильтрации  ")

    vacancy = None

    if int(user_choice_site) == 1:  # Определяем площадку для поиска
        vacancy = VacancyHh()
    elif int(user_choice_site) == 2:
        vacancy = VacancySj()
    else:
        print("Неверное значение. Введите 1 или 2")

    vacancies_filter = vacancy.get_api(user_choice_sort)
    vacancy_filtered = FilteredVacancies()
    if vacancies_filter:
        count_vacancy = 0
        for one in vacancies_filter:
            if 'name' in one:
                count_vacancy += 1

            elif 'profession' in one:
                count_vacancy += 1

            else:
                print("Key 'name' does not exist in the dictionary")

        print(f'Найдено {count_vacancy} вакансий')

        # Сохраняем вакансии в файл JSON
        vacancy_filtered.save_to_json('vacancies.json', vacancies_filter)

        vacancy_filtered.display_vacancies()

    else:
        print("Вакансий не найдено.")


if __name__ == '__main__':
    user_interaction()
