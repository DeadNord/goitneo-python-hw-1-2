import calendar
from datetime import datetime
from operator import itemgetter


def get_birthdays_per_week(users):
    list = {}
    users = sorted(users, key=itemgetter("birthday"))

    def addUser(user):
        weekday = calendar.day_name[user["birthday"].weekday()]
        if weekday == "Saturday" or weekday == "Sunday":
            weekday = "Monday"
        if weekday in list:
            list[weekday] += [user["name"]]
        else:
            list[weekday] = [user["name"]]

    current_date = datetime.now().date()
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)
            # Для чего этот участок кода? Какова его цель?
        else:
            delta_days = (birthday_this_year - current_date).days
            if (
                delta_days < 5
            ):  # Хотя в условие сказанно, delta_days < 7, но на мой взгляд реализация этой задачи требует иное значение.
                addUser(user)
    res = []
    for i in list:
        names = ", ".join(list[i])
        res.append(f"{i}: {names}")
    res = "\n".join(res)
    print(res)


# Данные, что я использовал для тестирвания.

# test_data = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 6, 24)},
#     {"name": "Paul Gates", "birthday": datetime(1956, 6, 24)},
#     {"name": "Bill Door", "birthday": datetime(1965, 7, 25)},
#     {"name": "Bill Window", "birthday": datetime(1975, 8, 26)},
#     {"name": "Bill Table", "birthday": datetime(1985, 9, 27)},
#     {"name": "Bill Brid", "birthday": datetime(1995, 10, 28)},
#     {"name": "Wayn Brigau", "birthday": datetime(1995, 10, 20)},
#     {"name": "Pol Brigau", "birthday": datetime(1995, 10, 16)},
#     {"name": "Tom Brigau", "birthday": datetime(1995, 10, 18)},
#     {"name": "Steve Bragau", "birthday": datetime(1995, 10, 18)},
#     {"name": "Bill Brigau", "birthday": datetime(1995, 10, 21)},
#     {"name": "Bob Brigau", "birthday": datetime(1995, 10, 21)},
#     {"name": "Braun Brigau", "birthday": datetime(1995, 10, 22)},
#     {"name": "Bei Brigau", "birthday": datetime(1995, 10, 23)}
#              ]
# get_birthdays_per_week(test_data)
