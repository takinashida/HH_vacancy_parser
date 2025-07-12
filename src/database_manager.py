import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute("CREATE SCHEMA IF NOT EXISTS schema_1;")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS schema_1.employer (
            employer_id INT PRIMARY KEY,
            employer_name TEXT,
            url VARCHAR(255),
            is_trusted BOOLEAN
        );''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS schema_1.vacancies (
            vacancy_id INT PRIMARY KEY,
            employer_id INT REFERENCES Schema_1.employer(employer_id),
            vacancy_name VARCHAR(100),
            area_id INT,
            url VARCHAR(255),
            salary_from NUMERIC,
            salary_to NUMERIC,
            currency VARCHAR(3),
            published_at DATE,
            requirement TEXT
        );''')
        self.conn.commit()

    def add_information(self, data):
        for vacancy in data:
            if ((vacancy.get("employer") or {}).get("id") or None):
                self.cur.execute(
                    "INSERT INTO schema_1.employer (employer_id, employer_name, url, is_trusted) VALUES (%s, %s, %s, %s) ON CONFLICT (employer_id) DO NOTHING",
                    (vacancy["employer"]["id"], vacancy["employer"]["name"], vacancy["employer"]["url"],
                     vacancy["employer"]["trusted"]))

                self.cur.execute('''INSERT INTO schema_1.vacancies
                (vacancy_id, employer_id, vacancy_name, area_id, url, salary_from, salary_to, currency, published_at, requirement)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_id) DO NOTHING''',
                            (vacancy["id"], vacancy["employer"]["id"], vacancy["name"],
                             vacancy["area"]["id"], vacancy["alternate_url"],
                             ((vacancy.get("salary") or {}).get("from") or 0),
                             ((vacancy.get("salary") or {}).get("to") or 0),
                             ((vacancy.get("salary") or {}).get("currency") or None),
                             vacancy["published_at"], (vacancy.get("snippet") or {}).get("requirement") or None))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        self.cur.execute('''SELECT employer.employer_name, COUNT(*)
                        FROM schema_1.vacancies
                        JOIN schema_1.employer USING(employer_id)
                        GROUP BY employer_name
                        ORDER BY COUNT(*) DESC''')
        return self.cur.fetchall()

    def get_all_vacancies(self):
        self.cur.execute('''SELECT employer.employer_name, vacancy_name, salary_from, currency, vacancies.url 
                        FROM schema_1.vacancies
                        JOIN schema_1.employer USING(employer_id)
                        ORDER BY salary_from DESC''')
        return self.cur.fetchall()

    def get_avg_salary(self):
        self.cur.execute('''SELECT employer.employer_name, vacancy_name, CASE
                    WHEN salary_from!=0 AND salary_to!=0 THEN ROUND((salary_from+salary_to)/2, 0)
                    WHEN salary_from=0 AND salary_to!=0 THEN salary_to
                    WHEN salary_from!=0 AND salary_to=0 THEN salary_from
                    WHEN salary_from=0 AND salary_to=0 THEN 0
                    END AS avg_salary, currency
                    FROM schema_1.vacancies
                    JOIN schema_1.employer USING(employer_id)
                    ORDER BY avg_salary DESC''')
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        self.cur.execute('''WITH case_result AS (SELECT vacancy_id, 
                            CASE
                                WHEN salary_from!=0 AND salary_to!=0 THEN ROUND((salary_from+salary_to)/2, 0)
                                WHEN salary_from=0 AND salary_to!=0 THEN salary_to
                                WHEN salary_from!=0 AND salary_to=0 THEN salary_from
                                WHEN salary_from=0 AND salary_to=0 THEN 0
                            END AS avg_salary
                        FROM schema_1.vacancies
                        WHERE currency = 'RUR')
                        SELECT employer.employer_name, vacancy_name, avg_salary, currency
                        FROM schema_1.vacancies
                        JOIN schema_1.employer USING(employer_id)
                        JOIN case_result USING(vacancy_id)
                        WHERE (avg_salary > (SELECT AVG(avg_salary) FROM case_result))  
                        ORDER BY avg_salary DESC''')
        return self.cur.fetchall()


    def get_vacancies_with_keyword(self, user_input):
        self.cur.execute('''SELECT employer.employer_name, vacancy_name, salary_from, currency, vacancies.url 
                        FROM schema_1.vacancies
                        JOIN schema_1.employer USING(employer_id)
                        WHERE vacancy_name LIKE %s
                        ORDER BY salary_from DESC''', (user_input,))
        return self.cur.fetchall()

