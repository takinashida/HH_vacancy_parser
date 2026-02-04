import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

from config import ROOT_DIR
from src.api import HeadHunterAPI
from src.database_manager import DBManager
from src.saver import JsonSaver
from src.vacancies import Vacancy


def main() -> None:
    """
    Точка входа
    :return: Все через print
    """
    text = input("Введите ключевые слова по которым будет производиться поиск: ")
    while True:
        end_page = input("Введите количество страниц (не более 20): ")
        if not end_page.isdigit():
            print(f"Количество страниц должно быть числом, вы ввели: {end_page}")
            continue
        end_page = int(end_page)
        if not 0 <= end_page <= 20:
            print(f"Число должно быть от 0 до 20, вы ввели: {end_page}")
            continue
        break
    print("Получаем данные с HH.ru")
    vacancy = HeadHunterAPI(text, end_page)
    load_dotenv()
    pg_database = DBManager(
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
    )
    pg_database.create_tables()
    pg_database.add_information(vacancy.get_vacancies())
    while True:
        user_choice = input(
            """Выберите действие из списка(1 - 5):
            1. Получить список всех компаний и количество вакансий у каждой компании.
            2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
            3. Получить среднюю зарплату по вакансиям.
            4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
            5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например python.\n"""
        )
        if not user_choice.isdigit():
            print(f"Выберите действие (число от 1 до 5), вы ввели: {user_choice}")
        else:
            user_choice = int(user_choice)
            if not 0 < user_choice <= 5:
                print(f"Число должно быть от 1 до 5, вы ввели: {user_choice}")
            else:
                break
    if int(user_choice) == 1:
        print(pg_database.get_companies_and_vacancies_count())
    elif int(user_choice) == 2:
        print(pg_database.get_all_vacancies())
    elif int(user_choice) == 3:
        print(pg_database.get_avg_salary())
    elif int(user_choice) == 4:
        print(pg_database.get_vacancies_with_higher_salary())
    elif int(user_choice) == 5:
        key_word = input("Введите слово искомое в названии вакансии: ")
        print(pg_database.get_vacancies_with_keyword(key_word))
    pg_database.close()


if __name__ == "__main__":
    main()
