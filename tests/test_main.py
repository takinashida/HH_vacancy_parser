import os
from pathlib import Path
from unittest.mock import Mock, patch

from config import ROOT_DIR
from src.main import main


@patch("builtins.input")
@patch("requests.request")
def test_main(mock_request, mock_input, capsys):
    path = Path.joinpath(ROOT_DIR, "data", "test.json")
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {
                "id": "92223870",
                "premium": False,
                "name": "Удаленный специалист службы поддержки (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
                "salary": {"from": 40000, "to": 54000, "currency": None, "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:39:01+0300",
                "created_at": "2024-01-25T17:39:01+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223870",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223870?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223870",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "92223756",
                "premium": False,
                "name": "Удаленный диспетчер чатов (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
                "salary": {"from": None, "to": 44000, "currency": "RUR", "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:37:04+0300",
                "created_at": "2024-01-25T17:37:04+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223756?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223756",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "92223870",
                "premium": False,
                "name": "Удаленный специалист службы поддержки (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
                "salary": {"from": 30000, "to": None, "currency": "RUR", "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:39:01+0300",
                "created_at": "2024-01-25T17:39:01+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223870",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223870?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223870",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "92223870",
                "premium": False,
                "name": "Удаленный специалист службы поддержки (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
                "salary": {"from": None, "to": None, "currency": "RUR", "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:39:01+0300",
                "created_at": "2024-01-25T17:39:01+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223870",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223870?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223870",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "92223870",
                "premium": False,
                "name": "Удаленный специалист службы поддержки (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
                "salary": {"from": None, "to": None, "currency": None, "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:39:01+0300",
                "created_at": "2024-01-25T17:39:01+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223870",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223870?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223870",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ]
    }
    mock_response.status_code = 200
    mock_request.return_value = mock_response
    mock_input.side_effect = ["Some", "one", "101", "1", str(path), "Y", "113", "Y"]
    main()
    captured = capsys.readouterr()
    assert captured.out == (
        "Количество страниц должно быть числом, вы ввели: one\n"
        "Число должно быть от 0 до 20, вы ввели: 101\n"
        "Получаем данные с HH.ru\n"
        "Сохраняем файл\n"
        "Обрабатываем данные\n"
        "Удаленный специалист службы поддержки (в Яндекс) 47000.0 None "
        "2024-01-25T17:39:01+0300 \n"
        " Способен работать в команде. Способен принимать решения самостоятельно. "
        "Готов учиться и узнавать новое. Опыт работы в колл-центре или службе... \n"
        " https://hh.ru/vacancy/92223870 \n"
        "\n"
        "Удаленный диспетчер чатов (в Яндекс) 44000 RUR 2024-01-25T17:37:04+0300 \n"
        " Способен работать в команде. Способен принимать решения самостоятельно. "
        "Готов учиться и узнавать новое. Опыт работы в колл-центре или службе... \n"
        " https://hh.ru/vacancy/92223756 \n"
        "\n"
        "Удаленный специалист службы поддержки (в Яндекс) 30000 RUR "
        "2024-01-25T17:39:01+0300 \n"
        " Способен работать в команде. Способен принимать решения самостоятельно. "
        "Готов учиться и узнавать новое. Опыт работы в колл-центре или службе... \n"
        " https://hh.ru/vacancy/92223870 \n"
        "\n"
        "Всего соответствующих требованиям найдено 3 вакансий\n"
        "Очищаем файл\n"
        "[]\n"
    )
    os.remove(path)
