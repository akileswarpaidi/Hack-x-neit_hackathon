import requests
def weather_s(city):
    # WeatherAPI URL
    url = "http://api.weatherapi.com/v1/current.json"

    # WeatherAPI key
    api_key = "b503e28300064bb8b9874442230805"

    # Location
    location = city

    # API request parameters
    params = {
        "q": location,
        "key": api_key
    }

    # Send HTTP GET request to the API and fetch the response
    response = requests.get(url, params=params)

    # Parse the JSON response and extract the relevant weather data
    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        condition = data["current"]["condition"]["text"]
        if "sunny" in condition.lower():
            return "sunny"
        elif "rain" in condition.lower():
            return "rainy"
        else:
            return "cloudy"
    else:
        return "snowy"
    return "snowy"
