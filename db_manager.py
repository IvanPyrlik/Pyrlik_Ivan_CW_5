import psycopg2


class DBManager:
    """
    Класс для подключения к БД
    """
    @staticmethod
    def get_companies_and_vacancies_count():
        """
        Метод получает список всех компаний и
        количество вакансий у каждой компании
        """
        with psycopg2.connect(host="localhost", database="db_hh",
                              user="postgres", password="ivan9675") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT company_name, COUNT(vacancies_name) AS count_vacancies  "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id) "
                            f"GROUP BY employers.company_name")
                result = cur.fetchall()
            conn.commit()
        return result

    @staticmethod
    def get_all_vacancies():
        """
        Метод получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        with psycopg2.connect(host="localhost", database="db_hh",
                              user="postgres", password="ivan9675") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT employers.company_name, vacancies.vacancies_name, "
                            f"vacancies.payment, vacancies_url "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id)")
                result = cur.fetchall()
            conn.commit()
        return result

    @staticmethod
    def get_avg_salary():
        """
        Метод получает среднюю зарплату по вакансиям
        """
        with psycopg2.connect(host="localhost", database="db_hh",
                              user="postgres", password="ivan9675") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT AVG(payment) as avg_payment FROM vacancies ")
                result = cur.fetchall()
            conn.commit()
        return result

    @staticmethod
    def get_vacancies_with_higher_salary():
        """
        Метод получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям
        """
        with psycopg2.connect(host="localhost", database="db_hh",
                              user="postgres", password="ivan9675") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE payment > (SELECT AVG(payment) FROM vacancies) ")
                result = cur.fetchall()
            conn.commit()
        return result

    @staticmethod
    def get_vacancies_with_keyword(keyword):
        """
        Метод получает список всех вакансий,
        в названии которых содержатся переданные в метод слова
        """
        with psycopg2.connect(host="localhost", database="db_hh",
                              user="postgres", password="ivan9675") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE lower(vacancies_name) LIKE '%{keyword}%' "
                            f"OR lower(vacancies_name) LIKE '%{keyword}'"
                            f"OR lower(vacancies_name) LIKE '{keyword}%';")
                result = cur.fetchall()
            conn.commit()
        return result
