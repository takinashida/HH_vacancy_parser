# HH Vacancy Parser

CLI‑утилита на Python для загрузки вакансий с [hh.ru](https://hh.ru) через
публичное API и сохранения их в базу данных PostgreSQL.

Возможности:
- ввод ключевых слов;
- указание количества страниц (0–20);
- загрузка вакансий в таблицы PostgreSQL;
- интерактивные запросы к базе (список компаний, вакансии, средняя зарплата и т.д.);
- тесты на `pytest` (покрытие ~95%).
- класс `JsonSaver` для экспорта вакансий в `.json` файл.

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

### 3. Создайте файл `.env`

Укажите параметры подключения к PostgreSQL:

```dotenv
DB_NAME=your_db
DB_USER=postgres
DB_PASSWORD=secret
DB_HOST=localhost
DB_PORT=5432
```

### 4. Запуск парсера

```bash
python src/main.py
```

После загрузки данных программа предложит выбрать один из пунктов меню:
1. Список компаний и количество вакансий.
2. Все вакансии с указанием средней зарплаты и ссылки.
3. Средняя зарплата по всем вакансиям.
4. Вакансии с зарплатой выше средней.
5. Поиск вакансий по ключевому слову.

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
│   ├── api.py            # Работа с hh.ru API
│   ├── database_manager.py # Работа с PostgreSQL
│   ├── saver.py          # JSON-сейвер
│   ├── vacancies.py      # Класс вакансии и валидация
│   └── main.py           # Точка входа CLI
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
* `D`: внедрение зависимостей через параметры конструктора 

---

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

