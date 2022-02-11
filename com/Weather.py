class Weather:

    def __init__(self):
        self.current_temp = ''
        self.metrics = ''
        self.description = ''
        self.high_temp = ''
        self.low_temp = ''
        self.day_of_week = ''

    def __str__(self):
        w = ''
        if self.current_temp != '':
            w += "\n" + self.current_temp
        if self.metrics != '':
            w += self.metrics
        if self.description != '':
            w += "\n" + self.description
        if self.high_temp != '':
            w += "\nHigh Temp: " + self.high_temp
        if self.low_temp != '':
            w += "\nLow Temp: " + self.low_temp
        if self.day_of_week != '':
            w += "\nDay of Week: " + self.day_of_week
        return w
