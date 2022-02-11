class City:

    def __init__(self):
        self.name = ''
        self.local_day_time = ''

    def __str__(self):
        city_str = ''
        if self.name != '':
            city_str += self.name
        if self.local_day_time != '':
            city_str += "\n" + self.local_day_time
        return city_str


