import requests
from decouple import config
from collections import defaultdict

API_KEY = config('API_KEY')

def get_current_weather(city):
    """ Get current weather from api (api.openweathermap.org) based on the city that user input
        :param city: city that user input in the form
    """
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    return response.json()

def get_weather_forecast(temp, city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=Bogor&appid={API_KEY}').json()
    results = []
    for forecast in response['list']:
        data = defaultdict()
        data['date'] = forecast['dt_txt']
        data['temp'] = temp_check(temp, forecast['main']['temp'])
        data['feels_like'] = temp_check(temp, forecast['main']['feels_like'])
        data['max'] = temp_check(temp, forecast['main']['temp_max'])
        data['min'] = temp_check(temp, forecast['main']['temp_min'])
        data['icon'] = forecast['weather'][0]['icon']
        results.append(dict(data))
    return results


def kelvin_to_celcius(temp):
    """ Convert kelvin to celcius temp 
        :param temp: number of temperature
    """
    return '{:.2f}'.format(int(temp) - 273)


def kelvin_to_fahrenheit(temp):
    """ Convert kelvin to fahrenheit temp 
        :param temp: number of temperature 
    """
    return  '{:.2f}'.format(((9/5) * (temp - 273)+32))


def temp_check(argument, temp):
    """ Check the temperature that user choose in the form

        :param argument: type of the temperature (Celcius, Fahrenheit)
            if '', then use default temperature from api (Kelvin)
        :param temp: number of temperature
    """
    switcher = {
        'Celcius': kelvin_to_celcius(int(temp)),
        'Fahrenheit': kelvin_to_fahrenheit(int(temp)),
        'Kelvin': temp,
        '': temp
    }
    return switcher.get(argument, "Invalid Temperature")