from db_manager import DBManager
from utils import create_table, add_to_table


def main():
    employers_list = [3127, 3776, 4934, 4181, 54979, 3093544, 1740, 15478, 8620, 3529, 78638, 4006, 561525, 64174]
    dbmanager = DBManager()
    create_table()
    add_to_table(employers_list)

    while True:
        user_input = input("Введите нужную цифру\n"
                           "1 - чтобы получить список всех компаний и количество вакансий у каждой компании\n"
                           "2 - чтобы получить список всех вакансий с указанием названия компании,\n "
                           "названия вакансии и зарплаты и ссылки на вакансию\n"
                           "3 - чтобы получить среднюю зарплату по вакансиям\n"
                           "4 - чтобы получить список всех вакансий, "
                           "у которых зарплата выше средней по всем вакансиям\n"
                           "5 - чтобы получить список всех вакансий, "
                           "в названии которых содержатся переданные в метод слова\n"
                           "6 - чтобы завершить работу\n")
        if user_input == "6":
            print("Завершение работы")
            break
        elif user_input == "1":
            company_vacancy = dbmanager.get_companies_and_vacancies_count()
            print("Список компаний и количество вакансий:")
            for company, count_vacancy in company_vacancy:
                print(f"{company}: {count_vacancy} вакансия(й).")
        elif user_input == "2":
            all_vacancies = dbmanager.get_all_vacancies()
            print("Список всех вакансий:")
            for vacancy in all_vacancies:
                print(f"Компания: {vacancy[0]}, вакансия: {vacancy[1]}, з/п: {vacancy[2]}")
        elif user_input == "3":
            avg_salary = dbmanager.get_avg_salary()
            print(f"Средняя з/п по вакансиям: {int(avg_salary[0][0])}")
        elif user_input == "4":
            salary_high = dbmanager.get_vacancies_with_higher_salary()
            print(f"Список вакансий с зарплатой выше среднего:")
            for vacancy in salary_high:
                print(vacancy[1])
        elif user_input == "5":
            keyword = input('Введите ключевое слово для поиска: ')
            vacancies_seach = dbmanager.get_vacancies_with_keyword(keyword)
            if len(vacancies_seach) <= 0:
                print("Извините, по вашему запросу вакансий не найдено!")
            else:
                print(f"Список вакансий по запросу:")
                for vacancy in vacancies_seach:
                    print(vacancy[0])
        else:
            print('Неправильный запрос, читайте внимательнее!')


if __name__ == "__main__":
    main()
