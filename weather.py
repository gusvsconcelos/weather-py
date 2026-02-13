import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input('Enter a city name: ')
    unit = input(
        '\n[metric (Celsius)] - [imperial (Fahrenheit)] - [standard (Kelvin)]\n'
        'Enter a unit measurement: ')

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units={unit}'

    weather_data = requests.get(requests_url).json()

    print(f'\nCurrent weather for {weather_data["name"]}\n')
    print(f'{weather_data["weather"][0]
          ["description"].capitalize().center(25)}\n')

    weather = weather_data['main']

    for k, v in weather.items():
        print(f'{k.capitalize():<20} {v}')


if __name__ == '__main__':
    get_current_weather()
