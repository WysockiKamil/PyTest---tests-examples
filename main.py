def get_weather(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number")
    
    if temp > 20:
        return "Hot"
    else:
        return "Cold"