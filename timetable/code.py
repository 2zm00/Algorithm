"""
1.0 time table 생성
    1.1 시간, 요일 구분 (평일/주말)
"""

from calendar import *
from datetime import datetime as dt
now = dt.now()

print(format(now.year)+"-"+format(now.month)+ "-"+format(now.day) +" ("+ now.strftime('%a'+")"))
print(now.strftime('%p %H:%M:%S'))


from datetime import datetime, timedelta

def generate_weekday_timetable(start_time, end_time):
    timetable = []
    current_time = start_time
    while current_time < end_time:
        # Check if it's lunch time
        if current_time.hour == 12 and current_time.minute == 40:
            timetable.append(current_time.strftime('%I:%M %p') + ' - ' + (current_time + timedelta(minutes=60)).strftime('%I:%M %p') + ': Lunch')
            current_time += timedelta(minutes=60)
        else:
            # Add class start time
            timetable.append(current_time.strftime('%I:%M %p') + ' - ' + (current_time + timedelta(minutes=30)).strftime('%I:%M %p') + ': Class')
            # Add break time
            current_time += timedelta(minutes=35)
    return timetable

# Define start and end time for weekday timetable
weekday_start_time = datetime.strptime('08:40 AM', '%I:%M %p')
weekday_end_time = datetime.strptime('05:40 PM', '%I:%M %p')

# Generate weekday timetable
weekday_timetable = generate_weekday_timetable(weekday_start_time, weekday_end_time)

# Insert lunch break into timetable
lunch_index = 7  # Assuming lunch break is at index 5
weekday_timetable.insert(lunch_index, '12:40 PM - 01:40 PM: Lunch')

# Print weekday timetable with lunch break
for class_time in weekday_timetable:
    print(class_time)
