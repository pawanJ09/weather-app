from com.Scrapper import Scrapper


if __name__ == '__main__':
    city = input('Enter your city: ')
    s = Scrapper()
    if city == '':
        s.get_weather_forecast()
    else:
        s.get_weather_forecast(city)

