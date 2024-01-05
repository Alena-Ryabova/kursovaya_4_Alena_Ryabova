# _Курсовая работа №4. ООП_.
### _Выполнила Алена Анатольевна Рябова_. Поток №29


Программа, которая получает информацию о вакансиях с 
разных платформ в России, сохраняет ее в файл и 
позволяет удобно работать с ней 
(добавлять, фильтровать, удалять).

### Проект состоит из модулей и файлов:

##### - main.py 
В данном модуле находится функция user_interaction() для взаимодействия с пользователем
через консоль. Она позволяет пользователю указать с какой платформы он хочет получить вакансии,
ввести ключевое слово для фильтра вакансий. Вакансии сортируются по зарплате и пользователь может выбрать колличество
самых высокооплачиваемых вакансий.

##### - utils.py 

Модуль содержит --абстрактный класс с общим методом для работы с Hh.ru и Sj.ru. 
--Класс VacancyHh для получения вакансий, отфильтрованных по ключевому слову с сайта Hh.ru. --Класс VacancySj 
для получения информации с сайта Sj.ru.

##### - vacancies.py 
В данном модуле, в классе FilteredVacancies() осуществляется сохранение вакансий в файл vacancies.json,
чтение файла и работа с вакансиями (инициализация, сбор характеристики вакансии, сортировка по зарплате).
После чего, настраивается читаемый вывод в консоль, отсортированных по зарплате вакансий,
в колличестве выбраннном пользователем.

##### - vacancies.json
Файл, в котором хранятся полученные вакансии, с выбранной пользователем площадки и отфильтрованные по ключевому слову,
которое ввел пользователь.


#### Платформы для сбора вакансий

 - [Hh.ru](https://github.com/hhru/api) 
 - [SuperJob.ru](https://api.superjob.ru) 