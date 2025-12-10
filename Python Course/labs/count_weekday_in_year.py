import calendar


class MyCalendar:
    def count_weekday_in_year(self, year, weekday):
        if weekday not in [x for x in range(0, 7)]:
            return

        c = calendar.Calendar()
        days = 0

        for month in range(1, 13):
            for week in c.monthdays2calendar(year, month):
                for day in week:
                    if day[0] != 0 and day[1] == weekday:
                        days += 1

        return days


sol = MyCalendar()
print(sol.count_weekday_in_year(2019, 0))  # Expected: 52 (Mondays in 2019)
print(sol.count_weekday_in_year(2000, 6))  # Expected: 53 (Sundays in 2000)
