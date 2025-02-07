from datetime import datetime
from datetime import timedelta

now = datetime.now()
print("Please select your timeframe:\n1-sec\n2-min\n3-hour\n4-day\n5-week\n")
timeframe = input("Timeframe: ")
timeframe = int(timeframe)
if timeframe == 1:
    increase_value = input("How many seconds to change: ")
    increase_value = int(increase_value)
    new_time = now + timedelta(seconds=increase_value)
    print(new_time)
elif timeframe == 2:
    increase_value = input("How many minutes to change: ")
    increase_value = int(increase_value)
    new_time = now + timedelta(minutes=increase_value)
    print(new_time)
elif timeframe == 3:
    increase_value = input("How many hours to change: ")
    increase_value = int(increase_value)
    new_time = now + timedelta(hours=increase_value)
    print(new_time)
elif timeframe == 4:
    increase_value = input("How many days to change: ")
    increase_value = int(increase_value)
    new_time = now + timedelta(days=increase_value)
    print(new_time)
elif timeframe == 5:
    increase_value = input("How many weeks to change: ")
    increase_value = int(increase_value)
    new_time = now + timedelta(weeks=increase_value)
    print(new_time)

