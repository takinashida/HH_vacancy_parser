import json
from abc import ABC, abstractmethod
from pathlib import Path

from config import ROOT_DIR


class BaseSaver(ABC):
    """Абстрактный класс всех сейверов"""

    __slots__ = ()

    @abstractmethod
    def json_save(self, data):
        pass

    @abstractmethod
    def json_load(self):
        pass

    @abstractmethod
    def json_clear(self):
        pass


class JsonSaver(BaseSaver):
    """Класс работающий с json"""

    __slots__ = "path"

    def __init__(self, path: str) -> None:
        self.path = path

    def json_save(self, data: list) -> None:
        """
        Сохраняет файл, если он есть то перезаписывает без дубликатов
        :param data: Файл
        :return: Ничего
        """
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []
        old_list = [item.get("id") for item in vacancies]
        if len(old_list):
            new_list = [item for item in data if item.get("id", 0) not in old_list]
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([*vacancies, *new_list], f, ensure_ascii=False)
        else:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)

    def json_load(self) -> list:
        """
        Подгружает файл
        :return: список
        """
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def json_clear(self) -> None:
        """
        Очищает файл
        :return: None
        """
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([], f)
