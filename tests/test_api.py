from unittest.mock import Mock, patch
import pytest
from src.api import BaseAPI, HeadHunterAPI


def test_BaseAPI():
    with pytest.raises(TypeError):
        thing = BaseAPI()


@patch("requests.request")
def test_HeadHunterAPI(mock_request):
    mock_response = Mock()
    mock_response.json.return_value = {"items": [{"Я": "Барабун"}, {"Ты": "Какун"}]}
    mock_response.status_code = 200
    mock_request.return_value = mock_response
    api = HeadHunterAPI("Текст", 2)
    result = api.get_vacancies()
    assert result == [{"Я": "Барабун"}, {"Ты": "Какун"}, {"Я": "Барабун"}, {"Ты": "Какун"}]
    assert mock_request.call_count == 2


@patch("requests.request")
def test_err_api(mock_requests, capsys):
    mock_response = Mock()
    mock_response.json.return_value = {"items": [{"Я": "Барабун"}, {"Ты": "Какун"}]}
    mock_response.status_code = 300
    mock_requests.return_value = mock_response
    api = HeadHunterAPI("Текст", 1)
    result = api.get_vacancies()
    captured = capsys.readouterr()
    assert captured.out == "Код ошибки: 300\n"
    assert result == []