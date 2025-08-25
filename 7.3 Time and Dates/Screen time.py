

from datetime import datetime, timedelta

filename = input('Filename: ')
with open(filename, 'w') as file:
    start_date = input('Starting date: ')
    days = int(input('How many days: '))
    starting = datetime.strptime(start_date, "%d.%m.%Y")
    starting = starting.date()
    num_days = timedelta(days = days)
    end_date = starting + num_days
    file.write(f"Time period: {starting} - {end_date} \n")
    print('Please type in screen time in minutes on each day (TV computer mobile):')
    total_min = 0
    minutes = []
    daily_lines = []
    for i in range(days):
        day = timedelta(days = i)
        user = input(f"Screen time {starting + day}: ")
        data = user.split(' ')
        output = user.replace(' ', '/')
        daily_lines.append(f"{starting + day}: {output} \n")
        for i in data:
            i = int(i)
            minutes.append(i)
    for i in minutes:
        total_min += i
    avg_min = total_min / days

    file.write(f"Total minutes: {total_min} \n")
    file.write(f"Average minutes: {avg_min} \n")
    for i in daily_lines:
        file.write(i)






