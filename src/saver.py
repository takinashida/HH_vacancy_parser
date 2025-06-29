import json
from abc import ABC, abstractmethod



class BaseSaver(ABC):
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
    __slots__ = ("path")
    def __init__(self, path):
        self.path = path

    def json_save(self, data):
        with open(self.path, "r", encoding="utf-8") as f:
            vacancies = json.load(f)
        old_list = [item.get("id") for item in vacancies]
        new_list = [item for item in data if item.get("id") not in old_list]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([*vacancies, *new_list], f, ensure_ascii=False)



    def json_load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def json_clear(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([], f)
