from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):
    """Базовый класс для api"""

    __slots__ = ()

    @abstractmethod
    def get_page(self, page):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI):
    """Класс для подключений к HeadHunter"""

    __slots__ = ("text", "end_page", "url", "headers")

    def __init__(self, text: str, end_page: int) -> None:
        """Файл инициации"""
        self.text = text
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.end_page = end_page

        super().__init__()

    def get_page(self, page: int) -> dict:
        """
        Делает http-запрос к hh.ru/vacancies
        :param page: номер страницы с которой нужно получить информацию
        :return: Словарь с ответом на запрос
        """
        params = {"text": self.text, "page": page, "per_page": 100}
        response = requests.request("GET", url=self.url, headers=self.headers, params=params)
        status_code = response.status_code
        if status_code == 200:
            return response.json()
        else:
            print(f"Код ошибки: {status_code}")
            return {"items": []}

    def get_vacancies(self) -> list:
        """
        Создает цикл для просмотра страниц
        :return: Список с вакансиями
        """
        page = 0
        database = []
        for page in range(self.end_page):
            database.extend(self.get_page(page)["items"])
        return database
