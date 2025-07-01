from abc import ABC, abstractmethod


class BaseVacancies(ABC):
    """Базовый класс вакансий"""

    __slots__ = ()

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
    """Класс вакансий"""

    __slots__ = (
        "name",
        "area_id",
        "url",
        "salary_from",
        "salary_to",
        "avg_salary",
        "currency",
        "published_at",
        "requirement",
    )

    def __init__(
        self,
        name: str,
        area_id: str,
        url: str,
        salary_from: int,
        salary_to: int,
        currency: str,
        published_at: str,
        requirement: str,
    ):
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
    def from_dict(cls, data: dict):
        """
        Метод из словаря вакансии достает информацию
        :param data: Словарь вакансии
        :return: Обьект класса Vacancy
        """
        salary = data.get("salary") or {}
        return cls(
            name=data["name"],
            area_id=data["area"]["id"],
            url=data["alternate_url"],
            salary_from=salary.get("from") or 0,
            salary_to=salary.get("to") or 0,
            currency=salary.get("currency") or None,
            published_at=data["published_at"],
            requirement=data["snippet"]["requirement"],
        )

    @classmethod
    def from_list(cls, data_list: list) -> list:
        """
        Проходится по списку словарей вакансий
        :param data_list: Список вакансий
        :return: Список объектов вакансий
        """

        return [cls.from_dict(item) for item in data_list]

    def __lt__(self, other):
        """Дандр метод меньше по средней зарплате"""
        return self.avg_salary < other.avg_salary

    def __eq__(self, other):
        """Дандр метод равно по средней зарплате"""
        return self.avg_salary == other.avg_salary

    def _str_validator(self, item):
        """Валидатор по строке"""
        return item if isinstance(item, str) else "None"

    def _num_validator(self, item):
        """Валидатор по целому числу"""
        return item if isinstance(item, int or float) else 0
