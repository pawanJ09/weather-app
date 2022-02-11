import bs4
import requests
import lxml
from bs4 import BeautifulSoup
from com.Weather import Weather
from com.Location import City
import globals


def invoke_url(query_param):
    """
    This method takes the city name as query param and invokes the URL defined in globals along
    with the headers
    :param query_param: String city name
    :return: requests.models.Response object
    """
    url = globals.url.format(query_param)
    header = globals.headers
    response = requests.get(url=url, headers=header)
    return response


def parse_location(response, soup):
    """
    This method takes the response, parses it and returns an object of City after parsing city,
    state, country and local time
    :param response: requests.models.Response object
    :param soup: bs4.BeautifulSoup object
    :return: com.City object
    """
    loc = City()
    if isinstance(response, requests.models.Response) and isinstance(soup, BeautifulSoup) \
            and response.status_code == 200:
        # Using select to find the div by id
        for c in soup.select('#wob_loc'):
            loc.name = c.text
            break  # Breaking after first occurrence is found
        # Using find to find the div by id. Looks more structured than soup.select()
        p_time = soup.find('div', attrs={'id': 'wob_dts'})
        if p_time is not None:
            loc.local_day_time = p_time.text
    return loc


def parse_current_weather(response, soup):
    """
    This method parses the response and fetches the current weather of the location
    :param response: requests.models.Response object
    :param soup: bs4.BeautifulSoup object
    :return: com.Weather object
    """
    weather = Weather()
    if isinstance(response, requests.models.Response) and isinstance(soup, bs4.BeautifulSoup) \
            and response.status_code == 200:
        current_temp = soup.find('span', attrs={'id': 'wob_tm'})
        if current_temp is not None:
            weather.current_temp = current_temp.text # bs4.Element.Tag.text and getText() both work
        weather.metrics = find_weather_metrics(soup)
        description = soup.find('span', attrs={'id': 'wob_dc'})
        if description is not None:
            weather.description = description.getText()
    return weather


def find_weather_metrics(soup):
    """
    This method fetches the metric from BeautifulSoup object and returns it
    :param soup: bs4.BeautifulSoup object
    :return: string metrics
    """
    for item in soup.find_all('span', attrs={'class': 'wob_t'}):
        try:
            if (("Fahrenheit" in item['aria-label'] or "Celsius" in item['aria-label']) and
                    "true" == item['aria-disabled']):
                return item.getText()
        except KeyError as error:
            continue


def parse_weather_forecast(response, soup):
    """
    This method scrapes the forecast for 1 week from the webpage, parses it and returns the list
    :param response: requests.models.Response object
    :param soup: bs4.BeautifulSoup object
    :return: com.Weather list
    """
    weather_forecast = []
    if isinstance(response, requests.models.Response) and isinstance(soup, bs4.BeautifulSoup) \
            and response.status_code == 200:
        for item in soup.find_all('div', attrs={'class': 'wob_df'}):
            if item is not None:
                weather = Weather()
                weather.metrics = find_weather_metrics(soup)
                parsed_day = item.find('div', attrs={'class': 'Z1VzSb'})
                if parsed_day is not None:
                    weather.day_of_week = parsed_day.text
                parsed_hi_lo = item.find_all('span', attrs={'class': 'wob_t',
                                                            'style': 'display:inline'})
                for c, h in enumerate(parsed_hi_lo):
                    if c == 0:
                        weather.high_temp = h.text
                    elif c == 1:
                        weather.low_temp = h.text
                    else:
                        break
                parsed_description = item.find('div', attrs={'class': 'DxhUm'})
                if parsed_description is not None:
                    # We could have also fetched by finding img but using this approach here for
                    # trial purposes
                    weather.description = parsed_description.img['alt']
                weather_forecast.append(weather)
    return weather_forecast


class Scrapper:

    def __init__(self):
        self.city = ''

    def get_weather_forecast(self, city='Chicago'):
        self.city = city
        query_param = self.city.replace(' ', '+')
        response = invoke_url(query_param)
        soup = BeautifulSoup(response.text, 'lxml')
        location = parse_location(response, soup)
        weather = parse_current_weather(response, soup)
        print('\n\nCurrent Weather for {}'.format(location))
        print(weather)
        weather_forecast = parse_weather_forecast(response, soup)
        print("\nForecast:")
        print(*weather_forecast)




