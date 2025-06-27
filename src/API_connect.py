from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    __slots__ = ()

    @abstractmethod
    def connect_API(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass


class API(BaseAPI):
    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def connect_API(self):
        response = requests.get()




