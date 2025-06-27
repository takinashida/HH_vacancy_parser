import json
from pathlib import Path

root = Path(__file__).parent
path_to_file = Path.joinpath(root, "data", "vacancies.json")

with open(path_to_file, "r", encoding= "utf-8") as f:
    result = json.load(f)["items"][0]

print(result)

          {'id': '93353083',
          'premium': False,
          'name': 'Тестировщик комфорта квартир',
          'department': None,
          'has_test': False,
          'response_letter_required': False,
          'area':
              {'id': '26',
               'name': 'Воронеж',
               'url': 'https://api.hh.ru/areas/26'
               },
          'salary':
              {'from': 350000,
               'to': 450000,
               'currency': 'RUR',
               'gross': False
               },
          'type':
              {'id': 'open',
               'name': 'Открытая'
               },
          'address': None,
          'response_url': None,
          'sort_point_distance': None,
          'published_at': '2024-02-16T14:58:28+0300',
          'created_at': '2024-02-16T14:58:28+0300',
          'archived': False,
          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93353083',
          'branding':
              {'type': 'CONSTRUCTOR',
               'tariff': 'BASIC'
               },
          'show_logo_in_search': True,
          'insider_interview': None,
          'url': 'https://api.hh.ru/vacancies/93353083?host=hh.ru',
          'alternate_url': 'https://hh.ru/vacancy/93353083',
          'relations': [],
          'employer':
              {'id': '3499705',
               'name': 'Специализированный застройщик BM GROUP',
               'url': 'https://api.hh.ru/employers/3499705',
               'alternate_url': 'https://hh.ru/employer/3499705',
               'logo_urls':
                   {'original': 'https://hhcdn.ru/employer-logo-original/1214854.png',
                    '240': 'https://hhcdn.ru/employer-logo/6479866.png',
                    '90': 'https://hhcdn.ru/employer-logo/6479865.png'
                    },
               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3499705',
               'accredited_it_employer': False, 'trusted': True
               }, 'snippet':
              {'requirement': 'Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...',
               'responsibility': 'Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне. Оценивать инфраструктуру района: ежедневно ходить на...'
               },
          'contacts': None,
          'schedule':
              {'id': 'flexible',
               'name': 'Гибкий график'
               },
          'working_days': [],
          'working_time_intervals': [],
          'working_time_modes': [],
          'accept_temporary': False,
          'professional_roles': [{'id': '107', 'name': 'Руководитель проектов'}],
          'accept_incomplete_resumes': False,
          'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'full', 'name': 'Полная занятость'},
          'adv_response_url': None,
          'is_adv_vacancy': False,
          'adv_context': None
          }

