import requests_html as r
import com.Weather
import com.Location
import globals


class Scrapper:

    def __init__(self):
        self.city = ''

    def get_weather_forecast(self, city='Crystal Lake'):
        self.city = city
        query_param = self.city.replace(' ', '+')
        url = 'https://www.google.com/search?q={}+weather'.format(query_param)
        header = globals.headers
        print(f'{url}')
        session = r.HTMLSession()
        response = session.get(url=url, headers=header)
        print(response.text)

