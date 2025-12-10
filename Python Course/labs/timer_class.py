from random import choice


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__total_in_seconds = 0

    def __str__(self):
        output = ""
        output += (
            f"0{self.__hours}" if len(str(self.__hours)) == 1 else str(self.__hours)
        )
        output += ":"
        output += (
            f"0{self.__minutes}"
            if len(str(self.__minutes)) == 1
            else str(self.__minutes)
        )
        output += ":"
        output += (
            f"0{self.__seconds}"
            if len(str(self.__seconds)) == 1
            else str(self.__seconds)
        )

        return output

    def next_second(self):
        self.convert_to_seconds()
        self.__total_in_seconds += 1
        self.convert_back()

    def prev_second(self):
        self.convert_to_seconds()
        self.__total_in_seconds -= 1
        self.convert_back()

    def convert_to_seconds(self):
        self.__total_in_seconds = (
            (self.__hours * 60 * 60) + (self.__minutes * 60) + self.__seconds
        )

    def convert_back(self):
        if self.__total_in_seconds == 86400:
            self.__hours = 0
            self.__minutes = 0
            self.__seconds = 0
        elif self.__total_in_seconds < 0:
            self.__hours = 23
            self.__minutes = 59
            self.__seconds = 59
        else:
            self.__hours = self.__total_in_seconds // 3600
            self.__minutes = (self.__total_in_seconds % 3600) // 60
            self.__seconds = (self.__total_in_seconds % 3600) % 60

        return self.__str__()


# Test

timer = Timer(0, 0, 0)

options = [timer.next_second, timer.prev_second]
for i in range(1000):
    print(timer)
    choice(options)()
