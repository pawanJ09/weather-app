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
            w += self.current_temp + self.metrics + " " + self.description
        if self.day_of_week != '':
            w += "\n" + self.day_of_week
        if self.high_temp != '':
            w += " " + self.high_temp + self.metrics
        if self.low_temp != '':
            w += " | " + self.low_temp + self.metrics + " " + self.description
        return w
