from abc import ABC, abstractmethod
from src.saver import JsonSaver
from config import ROOT_DIR
from pathlib import Path

class BaseVacancies(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass

    @classmethod
    @abstractmethod
    def from_list(cls, data_list):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

class Vacancy(BaseVacancies):
    __slots__=("name", "area_id", "url", "salary_from", "salary_to","avg_salary", "currency", "published_at", "requirement")
    def __init__(self, name, area_id, url, salary_from, salary_to, currency, published_at, requirement):
        self.name = self._str_validator(name)
        self.area_id = self._str_validator(area_id)
        self.url = url
        self.salary_from = self._num_validator(salary_from)
        self.salary_to = self._num_validator(salary_to)
        self.currency = self._str_validator(currency)
        self.published_at = self._str_validator(published_at)
        self.requirement = self._str_validator(requirement)
        if self.salary_from and self.salary_to:
            self.avg_salary = (self.salary_from + self.salary_to) / 2
        elif self.salary_from:
            self.avg_salary = self.salary_from
        elif salary_to:
            self.avg_salary = self.salary_to
        else:
            self.avg_salary = 0

    @classmethod
    def from_dict(cls, data):
        salary = data.get("salary") or {}
        return cls(name = data["name"],
        area_id = data["area"]["id"],
        url = data["apply_alternate_url"],
        salary_from = salary.get("from")or 0,
        salary_to = salary.get("to")or 0,
        currency = salary.get("currency") or None,
        published_at = data["published_at"],
        requirement = data["snippet"]["requirement"])


    @classmethod
    def from_list(cls, data_list):
        return [cls.from_dict(item) for item in data_list]

    def __lt__(self, other):
        return self.avg_salary < other.avg_salary

    def __eq__(self, other):
        return self.avg_salary == other.avg_salary

    def _str_validator(self, item):
        return item if isinstance(item, str) else "None"

    def _num_validator(self, item):
        return item if isinstance(item, int or float) else 0



