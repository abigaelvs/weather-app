from flask import Blueprint, render_template, url_for, request, redirect

from .utils import get_current_weather, kelvin_to_celcius, kelvin_to_fahrenheit, temp_check, get_weather_forecast

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            city = request.form['city']
            try:
                temp = request.form['temp']
            except KeyError:
                temp = ''

            data = get_current_weather(city)
            forecasts = get_weather_forecast(temp, city)

            context = {
                'city': city,
                'country': data['sys']['country'],
                'current_temperature': temp_check(temp, data['main']['temp']),
                'feels_like': temp_check(temp, data['main']['feels_like']),
                'max': temp_check(temp, data['main']['temp_max']),
                'min': temp_check(temp, data['main']['temp_min']),
                'weather': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'temp_simb': (temp[0] if temp != '' else 'K'),
                'forecasts': forecasts
            }
        except Exception:
            return redirect('/error')
    else:
        context = {}
    return render_template('index.html', **context)

@views.route('/error')
def error():
    return render_template('error.html')