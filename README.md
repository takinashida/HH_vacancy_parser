# HH Vacancy Parser

Поисковый Python‑парсер для сбора вакансий с [hh.ru](https://hh.ru) через публичное API.

Проект поддерживает:
- Ввод ключевых слов
- Задание количества страниц (до 20)
- Фильтрацию по городу (по `area_id`)
- Сортировку по зарплате
- Сохранение в `.json` без дублирования
- Тесты на основе `pytest` (покрытие ~95%)

---

## Как запустить

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/takinashida/HH_vacancy_parser.git
cd HH_vacancy_parser
````

### 2. Установите зависимости

```bash
poetry install
```

### 3. Запуск парсера

```bash
python src/main.py
```

---

## Тестирование

```bash
pytest --cov=src
```

HTML-отчёт покрытия:

```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html  
```

---

## Структура проекта

```
HH_vacancy_parser/
├── src/
│   ├── api.py          # Класс API-запроса к hh.ru
│   ├── saver.py        # Абстрактный и конкретный JSON-сейвер
│   ├── vacancy.py      # Классы вакансий с валидацией и сортировкой
│   └── main.py         # Точка входа CLI
│
├── data/               # Каталог для сохранения вакансий
├── tests/              # Юнит-тесты на Pytest
└── config.py           # Глобальные константы
```

---

##  SOLID и ООП

Проект спроектирован с учётом принципов SOLID:

* `S`: каждая сущность делает одну вещь (API, Saver, Vacancy)
* `O`: можно добавлять другие API или форматы (CSV) без переписывания старых классов
* `L`: соблюдается иерархия базовых/наследуемых классов
* `I`: разделение интерфейсов (BaseAPI, BaseSaver, BaseVacancy)
* `D`: внедрение зависимостей через параметры конструктора (например, путь для сохранения)

---

## Пример вакансии (структура)

```json
{
  "id": "93353083",
  "name": "Тестировщик комфорта квартир",
  "salary": {
    "from": 350000,
    "to": 450000,
    "currency": "RUR"
  },
  "area": {
    "id": "26",
    "name": "Воронеж"
  },
  "published_at": "2024-02-16T14:58:28+0300",
  "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083"
}
```

