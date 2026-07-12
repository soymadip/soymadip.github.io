"""
We can calculate datetime using 'datetime' & 'zoneinfo' stdlib


current times:

| Represents               | Get current value       | Example                      |
| ------------------------ | ----------------------- | ---------------------------- |
| Calendar date            | `date.today()`          | `2026-07-11`                 |
| Time of day              | `datetime.now().time()` | `17:42:15.123456`            |
| Date + time              | `datetime.now()`        | `2026-07-11 17:42:15.123456` |

"""

from datetime import date, datetime, time

# --------------------- Basic Date-Time Objects --------------------------

# Just a Date
my_birthday: date = date(2005, 7, 15)
print(f"A Date: {my_birthday}")  # 2005-07-15

# Just a Time
lunch_time: time = time(13, 30)
print(f"A Time: {lunch_time}")  # 13:30:00

# Creating Date-Time
appoinment: datetime = datetime(2026, 10, 15, 12, 34)

print(
    f"A DateTime: {appoinment}"  # 2026-10-15 12:34:00  (anything not specified will go to 00)
)


# --------------- Formatting and Parsing (Strings <-> Datetime) ------------------

# `strptime` = String parse time (String -> Datetime)
# `strftime` = String format time (Datetime -> String)

logged_time: str = "2026-07-11 13:53:24"  # a datetime string

# parse a datetime string:                  string          format
parsed_time: datetime = datetime.strptime(logged_time, "%Y-%m-%d %H:%M:%S")

print(type(parsed_time))  # <class 'datetime.datetime'>


# Format DateTime in a string:           datetime obj            format
formatted_time: str = datetime.strftime(parsed_time, "%A, %B %d, %Y")

print(f"formated time: {formatted_time}")  # "Saturday, July 11, 2026"


# Formatting current time in a pretty String:
now_time: datetime = datetime.now()

formatted = now_time.strftime(
    "%A, %B %d, %Y"
)  # Notice that when using instance method we dont need to pass object. just like we learnt in OOP lesson
print(formatted_time)


# ----------- Date Math (using Time Delta) --------------------
print()

from datetime import timedelta

# To add or subtract time, we use timedelta.
# We cannot add two datetimes together (that doesn't make sense), but you can add a duration to a datetime.

today: datetime = datetime.now()
three_days_ago: datetime = today - timedelta(days=3)

print(
    f"Today Date: {today.strftime('%B %d')}\n3 days Ago: {three_days_ago.strftime('%B %d')}"
)

now_hour = datetime.now()
three_hours_later = now_hour + timedelta(hours=3, minutes=12)

print(
    f"\nCurrent Time hour + min: {now_hour.strftime('%H:%M')}\n3 hours 12 minutes later: {three_hours_later.strftime('%H:%M')}"
)

# Or only print Hour
print(f"\nCurrent Time: {now_hour.hour}\n3 hours later: {three_hours_later.hour}")


# Calculate birthday
birth_day = datetime(2026, 7, 15)
today_date: datetime = datetime.now()


remaining: timedelta = (  # subtraction datetimes gives timedelta type
    birth_day - today_date
)

print(f"\nTime remaining till birthday: {remaining}\n")

# comparing
if today_date.date() > birth_day.date():
    print("Birthday is gone")
elif today_date.date() == birth_day.date():
    print("Happy Birthday!")
else:
    print(f"Birthday is coming in: {remaining.days}days, {remaining.seconds} seconds ")


# ------------------ Measuring time ------------------

import time as tm


print("\nStarted counter")
start = tm.perf_counter()

tm.sleep(3) # sleep 3 seconds
end = tm.perf_counter()

took = end - start

print(f"Time took: {int(took)} seconds")
