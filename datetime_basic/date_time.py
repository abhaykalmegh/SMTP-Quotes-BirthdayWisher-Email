from datetime import datetime

# Define object of datetime module.
# By using now() we get current object of datetime.
time_now = datetime.now()

# You get current Year(in number)
year = time_now.year
print(year)

# You get current Month(in number)
month = time_now.month
print(month)

# You get current day(today's date)
day = time_now.day
print(day)

# You get weekdays numbers from 0 to 6 --> (monday to sunday) from below function.
day_of_week = time_now.weekday()
print(day_of_week)

# you can define datatime using datatime module.
date_of_birth = datetime(year=1992, month=12, day=13)
print(date_of_birth)