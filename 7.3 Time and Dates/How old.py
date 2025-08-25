

from datetime import datetime

user_day = int(input('Day: '))
user_month = int(input('Month: '))
user_year = int(input('Year: '))

user_dob = datetime(user_year, user_month, user_day)
new_mill = datetime(1999, 12, 31)
difference = new_mill - user_dob
if difference.days > 0:
    print(f'You were {difference.days} days old on the eve of the new millennium')
else:
    print(f"You weren't born yet on the eve of the new millennium")

