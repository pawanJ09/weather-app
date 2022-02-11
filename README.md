# Weather App

This is a utility app that returns the current weather and forecast of the provided city. 
This app is fetching the weather data by using Web scraping. I have used BeautifulSoup library to 
achieve this as requests-html could not be used with Python version 3.9.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
python3 -m pip install requests

python3 -m pip install bs4

python3 -m pip install lxml
```

## Running the application locally

You can run the main.py program to get started. This file has the __main__ method.

```shell
python main.py
```

## Usage

Enter your city: Chicago - runs the search and finds the first match for city named Chicago.

Enter your city: Manchester Missouri - runs the search and looks for city in respective 
state/country as provided in case there are multiple cities with the same name.

## Output

### For unique city name

<pre>
Current Weather for Chicago, IL
Friday 5:00 PM
40°F Mostly cloudy

Forecast:

Fri  46°F |  15°F  Scattered snow showers 
Sat  21°F |  12°F  Partly cloudy 
Sun  20°F |  15°F  Partly cloudy 
Mon  34°F |  22°F  Partly cloudy 
Tue  37°F |  35°F  Partly cloudy 
Wed  48°F |  31°F  Scattered showers 
Thu  34°F |  15°F  Snow with brief sleet 
Fri  26°F |  24°F  Partly cloudy
</pre>

### For common city names

<pre>
Current Weather for Manchester, MO
Friday 5:00 PM
47°F Mostly cloudy

Forecast:

Fri  50°F |  15°F  Partly cloudy
Sat  28°F |  15°F  Partly cloudy 
Sun  36°F |  19°F  Partly cloudy 
Mon  50°F |  26°F  Sunny 
Tue  60°F |  48°F  Partly cloudy 
Wed  64°F |  40°F  Scattered showers 
Thu  44°F |  18°F  Rain and snow 
Fri  41°F |  27°F  Sunny
</pre>
