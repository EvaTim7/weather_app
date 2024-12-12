import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()

def get_current_weather(city):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    try:
        weather_data = requests.get(request_url).json()
        return weather_data
    except Exception as e:
        return {"error": f"Error fetching weather data: {str(e)}"}

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
