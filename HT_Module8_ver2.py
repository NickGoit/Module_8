from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_datetime = datetime.now().date()

    days_interval = define_days_interval(current_datetime)

    print('current_datetime', current_datetime)

    new_datetime = current_datetime+days_interval
    print('new_datetime', new_datetime)

    dayweek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    empty_list = []
    users_day_dict = {key: list(empty_list) for key in dayweek}

    for user in users:
        coming_birthday = datetime(
            year=current_datetime.year,
            month=user['birthday'].month,
            day=user['birthday'].day
        ).date()

        if current_datetime <= coming_birthday <= new_datetime:
            if coming_birthday.strftime('%A') in ['Saturday', 'Sunday']:
                users_day_dict['Monday'].append(user['name'])
            else:
                users_day_dict[coming_birthday.strftime('%A')].append(user['name'])

    for key, value in users_day_dict.items():
        if value:
            print(f"{key}: {', '.join(value)}")


def define_days_interval(current_day):
    if current_day.weekday() == 5:
        days_interval = timedelta(days=6)
    elif current_day.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)

    return days_interval


users_test = [
    {'name': 'Bill', 'birthday': datetime.strptime('24.11.1980', '%d.%m.%Y')},
    {'name': 'Jill', 'birthday': datetime.strptime('25.10.1990', '%d.%m.%Y')},
    {'name': 'Kim',  'birthday': datetime.strptime('26.10.1991', '%d.%m.%Y')},
    {'name': 'Jane', 'birthday': datetime.strptime('25.10.1995', '%d.%m.%Y')}
    ]


if __name__ == '__main__':
    get_birthdays_per_week(users_test)
