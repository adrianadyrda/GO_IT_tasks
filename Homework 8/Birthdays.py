from datetime import datetime, timedelta
from typing import List, Dict


def get_birthdays_per_week(users: List[Dict[str, str]]) -> None:
    start_date = datetime.today()
    start_date = start_date + timedelta(days=(7 - start_date.weekday()))
    start_date = start_date - timedelta(days=2)
    end_date = start_date + timedelta(days=7)
    birthdays = {}
    for user in users:
        b_day = user['birthday']
        b_day = datetime(year=start_date.year, month=b_day.month, day=b_day.day)
        if start_date <= b_day <= end_date:
            if b_day.weekday() == 5:
                b_day += timedelta(days=2)
            elif b_day.weekday() == 6:
                b_day += timedelta(days=1)
            if b_day not in birthdays.keys():
                birthdays[b_day] = []
            birthdays[b_day].append(user['name'])

    for date in birthdays.keys():
        day = date.strftime('%A')
        names = birthdays[date]
        names_result = ','.join(names)
        print(f'{day}: {names_result}')

