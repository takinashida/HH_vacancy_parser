from src.saver import JsonSaver
from src.vacancies import Vacancy
from src.api import HeadHunterAPI
from pathlib import Path
from config import ROOT_DIR



if __name__ == "__main__":
    text = input("Введите ключевые слова по которым будет производиться поиск: ")
    end_page = int(input("Введите количество страниц которые будут показаны(не более 20): "))
    try:
        while not 0 <= end_page <= 20:
            print(f"Количество страниц не должно быть отрицательным или превышать 20, вы ввели {end_page}: ")
            end_page = int(input("Введите количество страниц которые будут показаны(не более 20): "))
    except ValueError:
        print(f"Количество страниц должно быть числом, вы ввели {end_page}: ")
    print("Получаем данные с HH.ru")
    vacancy = HeadHunterAPI(text, end_page)
    path = input(r"Введите директорию в которой сохраниться файл(по умолчанию \data\vacancies.json): ")
    if path == "":
        path = Path.joinpath(ROOT_DIR, "data", "vacancies.json")
    print("Сохраняем файл")
    file_vacancy = JsonSaver(path)
    file_vacancy.json_save(vacancy.get_vacancies())
    data = file_vacancy.json_load()
    print("Обрабатываем данные")
    database =Vacancy.from_list(data)
    if input("Сортировать вакансии по средней зарплате?(Y/N): ").lower() == "y":
        database = sorted(database, reverse=True)
    it = 0
    area = input("Введите id региона который хотите видеть(1: Москва, 113: Россия): ")
    for i in database:
        if i.area_id == area and i.avg_salary > 0:
            it +=1
            print(i.name, i.avg_salary, i.currency, i.published_at, "\n", i.requirement, "\n", i.url, "\n")
    print(f"Всего соответствующих требованиям найдено {it} вакансий")
    if input("Очистить данные?(Y/N): ").lower() == "y":
        file_vacancy.json_clear()
        print("Очищаем файл")
        print(file_vacancy.json_load())