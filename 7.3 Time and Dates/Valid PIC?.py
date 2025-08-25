

import datetime

def is_it_valid(pic: str):
    flag = True
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = pic[4:6]
        if pic[6] == '+':
            year = '18' + year
            year = int(year)
        elif pic[6] == '-':
            year = '19' + year
            year = int(year)
        elif pic[6] == 'A':
            year = '20' + year
            year = int(year)
        date_dob = datetime.datetime(year, month, day)

        pers_ident = pic[7:10]
        all_nums = pic[:6] + pers_ident
        all_nums = int(all_nums)
        control_num = all_nums % 31
        available = '0123456789ABCDEFHJKLMNPRSTUVWXY'
        control = available[control_num]
        if pic[-1] == control:
            flag = True
        elif pic[-1] != control:
            flag = False
    except:
        flag = False
    return flag
    

print(is_it_valid('230827-906F'))
print(is_it_valid('120488+246L'))
print(is_it_valid('310823A9877'))