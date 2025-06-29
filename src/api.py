import json
from abc import ABC, abstractmethod
import requests
from pathlib import Path
from config import ROOT_DIR
from src.saver import JsonSaver

class BaseAPI(ABC):
    __slots__ = ()

    @abstractmethod
    def get_page(self, page):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI):
    __slots__ = ("text", "end_page", "url", "headers")
    def __init__(self, text, end_page):
        self.text = text
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.end_page = end_page

        super().__init__()


    def get_page(self, page):
        try:
            params = {'text': self.text, 'page': page, 'per_page': 100}
            response = requests.get(url=self.url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка: {e}")
            return {"items": []}

    def get_vacancies(self):
        page = 0
        database= []
        for page in range(self.end_page):
            database.extend(self.get_page(page)["items"])
        return database



