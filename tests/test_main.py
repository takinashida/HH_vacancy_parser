import os
from unittest.mock import Mock, patch
from src.main import main

@patch("src.main.DBManager")
@patch("builtins.input")
@patch("requests.request")
@patch("os.getenv")
def test_main(mock_getenv, mock_request, mock_input, mock_dbmanager, capsys):
    mock_getenv.side_effect = lambda key, default=None: {
        "DB_NAME": "test",
        "DB_USER": "postgres",
        "DB_PASSWORD": "12345",
        "DB_HOST": "localhost",
        "DB_PORT": "5432"
    }.get(key, default)

    mock_response = Mock()
    mock_response.json.return_value = {"items": []}
    mock_response.status_code = 200
    mock_request.return_value = mock_response

    mock_db_instance = Mock()
    mock_dbmanager.return_value = mock_db_instance

    mock_db_instance.get_companies_and_vacancies_count.return_value = "FAKE_COMPANIES"
    mock_db_instance.get_all_vacancies.return_value = "FAKE_VACANCIES"
    mock_db_instance.get_avg_salary.return_value = "FAKE_AVG"
    mock_db_instance.get_vacancies_with_higher_salary.return_value = "FAKE_HIGHER"
    mock_db_instance.get_vacancies_with_keyword.return_value = "FAKE_KEYWORD"

    mock_input.side_effect = ["Some", "one", "101", "1", "Some", "one", "101", "2"]
    main()
    captured = capsys.readouterr()
    assert captured.out == ('Количество страниц должно быть числом, вы ввели: one\n'
 'Число должно быть от 0 до 20, вы ввели: 101\n'
 'Получаем данные с HH.ru\n'
 'Выберите действие (число от 1 до 5), вы ввели: Some\n'
 'Выберите действие (число от 1 до 5), вы ввели: one\n'
 'Число должно быть от 1 до 5, вы ввели: 101\n'
 'FAKE_VACANCIES\n')

    mock_input.side_effect = ["Some", "1", "1"]
    main()
    captured = capsys.readouterr()
    assert captured.out == ('Получаем данные с HH.ru\nFAKE_COMPANIES\n')

    mock_input.side_effect = ["Some", "1", "3"]
    main()
    captured = capsys.readouterr()
    assert captured.out == ('Получаем данные с HH.ru\nFAKE_AVG\n')

    mock_input.side_effect = ["Some", "1", "4"]
    main()
    captured = capsys.readouterr()
    assert captured.out == ('Получаем данные с HH.ru\nFAKE_HIGHER\n')

    mock_input.side_effect = ["Some", "1", "5", "Python"]
    main()
    captured = capsys.readouterr()
    assert captured.out == ('Получаем данные с HH.ru\nFAKE_KEYWORD\n')