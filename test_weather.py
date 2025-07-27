import pytest
from weather import get_weather

def test_get_weather(mocker):
    
    mock_get = mocker.patch('weather.requests.get')

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 25, "condition": "Sunny"}

    result  = get_weather("Dubai")

    assert result == {"temp": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("http://api.weather.com/v1/Dubai")