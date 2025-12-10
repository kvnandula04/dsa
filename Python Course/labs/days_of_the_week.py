class WeekDayError(Exception):
    pass


class Weeker:
    arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.arr:
            raise WeekDayError
        self.day = day
        self.__day_index = Weeker.arr.index(day)

    def __str__(self):
        return Weeker.arr[self.__day_index % 7]

    def add_days(self, n):
        self.__day_index += n
        return self.__str__()

    def subtract_days(self, n):
        self.__day_index -= n
        return self.__str__()


try:
    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't serve your request.")
