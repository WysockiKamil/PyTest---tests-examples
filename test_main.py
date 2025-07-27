import pytest
from main import get_weather

@pytest.mark.parametrize("temp, expected", [
    (15, "Cold"),
    (19, "Cold"),
    (20, "Cold"),
    (21, "Hot"),
    (30, "Hot")
])
def test_get_weather(temp, expected):
    assert get_weather(temp) == expected

@pytest.mark.parametrize("invalid_input", ["abc", None, [10], {"temp": 15}])
def test_get_weather_invalid_type(invalid_input):
    with pytest.raises(TypeError, match="Temperature must be a number"):
        get_weather(invalid_input)