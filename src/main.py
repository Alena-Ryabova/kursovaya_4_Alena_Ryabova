from src.utils import VacancyHh, VacancySj
from src.vacancies import FilteredVacancies


def user_interaction():
    print("Выберите площадку для сортировки вакансий: \n"
          "1. HeadHunter\n"
          "2. SuperJob")
    user_choice_site = input("Введите значение  ")

    user_choice_sort = input("Введите ключевое слово для фильтрации  ")

    vacancy = None # Переменная для выбранной пользователем площадки

    if int(user_choice_site) == 1:  # Определяем площадку для поиска
        vacancy = VacancyHh()
    elif int(user_choice_site) == 2:
        vacancy = VacancySj()
    else:
        print("Неверное значение. Введите 1 или 2")

    vacancies_filter = vacancy.get_api(user_choice_sort)
    vacancy_filtered = FilteredVacancies()

    if vacancies_filter:
        count_vacancy = 0  # Счетчик для подсчета кол-ва найденых вакансий
        for one in vacancies_filter:
            count_vacancy += 1

        print(f'Найдено {count_vacancy} вакансий')

        # Сохраняем вакансии в файл JSON
        vacancy_filtered.save_to_json('vacancies.json', vacancies_filter)
        print(f'Вакансии отсортированы по зарплате от большей к меньшей')

        number_of_vacancy = input(f'Какое колличество вакансий вывести?  Введите значение от 1 до {count_vacancy}   \n')

        vacancy_filtered.display_vacancies(number_of_vacancy)

    else:
        print("Вакансий не найдено.")


if __name__ == '__main__':
    user_interaction()
