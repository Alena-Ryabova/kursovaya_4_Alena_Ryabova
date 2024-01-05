from src.utils import VacancyHh, VacancySj
from src.vacancies import FilteredVacancies


def user_interaction():
    print("Выберите площадку для сортировки вакансий: \n"
          "1. HeadHunter\n"
          "2. SuperJob")

    vacancy = None  # Переменная для выбранной пользователем площадки

    while vacancy is None:  # Пока vacancy не была установлена
        user_choice_site = input("Введите значение: \n")

        if user_choice_site == "1":
            vacancy = VacancyHh()
        elif user_choice_site == "2":
            vacancy = VacancySj()
        else:
            print("Неверное значение. Введите 1 или 2: \n")

    user_choice_sort = input("Введите ключевое слово для фильтрации:  \n")

    vacancies_filter = vacancy.get_api(user_choice_sort)
    vacancy_filtered = FilteredVacancies()

    if vacancies_filter:
        count_vacancy = 0  # Счетчик для подсчета кол-ва найденых вакансий
        for one in vacancies_filter:
            count_vacancy += 1

        print(f'Найдено {count_vacancy} вакансий \n')

        # Сохраняем вакансии в файл JSON
        vacancy_filtered.save_to_json('vacancies.json', vacancies_filter)
        print(f'Вакансии отсортированы по зарплате от большей к меньшей \n')

        number_of_vacancy = 0
        while int(number_of_vacancy) > count_vacancy or int(number_of_vacancy) < 1:
            number_of_vacancy = input(
                f'Какое колличество вакансий вывести?  Введите значение от 1 до {count_vacancy}   \n')
            if int(number_of_vacancy) > count_vacancy or int(number_of_vacancy) < 1:
                number_of_vacancy = input(
                    f'Неверное значение!  Введите значение от 1 до {count_vacancy}   \n')

        vacancy_filtered.display_vacancies(number_of_vacancy)

    else:
        print("Вакансий не найдено.")


if __name__ == '__main__':
    user_interaction()
