class Mytime:
    def __init__(self, time_str):


        hour, min = time_str.split(":")
        self.hour = int(hour)
        self.min = int(min)


time_str = "05:30"
time = Mytime(time_str)
