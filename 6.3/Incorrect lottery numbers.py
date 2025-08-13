

def filter_incorrect():
    with open('correct_numbers.csv', 'w') as new_file:
        with open('lottery_numbers.csv', 'r') as file:
            for line in file:
                week, numbers = line.split(';') # week is week 52, numbers are all the nums proceeding
                numbers = numbers.strip()
                numbers = numbers.split(',')
                name_week, week_num = week.split(' ') # name_week is just week, week_num is 52
                flag = True
                tracker = []
                try:
                    int(week_num) # see if able to convert week number to int, if not then pass
                    for i in numbers:
                        int(i) # see if able to convert numbers to int, if not then pass
                    if len(numbers) < 7:
                        flag = False
                    for i in numbers:
                        if (int(i) < 1) or (int(i) > 39):
                            flag = False
                    for i in numbers:
                        if int(i) in tracker:
                            flag = False
                        else:
                            tracker.append(int(i))
                    if flag:
                        new_file.write(line)
                except:
                    pass
filter_incorrect()