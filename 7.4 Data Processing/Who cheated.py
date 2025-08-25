

import csv
from datetime import datetime, timedelta

def cheaters():
    with open('start_times.csv') as start_file:
        with open('submissions.csv') as subs_file:
            start_dict = {}
            end_dict = {}
            for line in start_file:
                parts1 = line.split(';')
                name1 = parts1[0]
                start_time = parts1[1].strip()
                start_time = datetime.strptime(start_time, '%H:%M').time()
                minutes = start_time.hour * 60 + start_time.minute
                start_dict[name1] = minutes
            for line in subs_file:
                parts2 = line.split(';')
                name2 = parts2[0]
                end_time = parts2[3].strip()
                end_time = datetime.strptime(end_time, '%H:%M').time()
                minutes2 = end_time.hour * 60 + end_time.minute
                if name2 not in end_dict:
                    end_dict[name2] = [minutes2]
                else:
                    end_dict[name2].append(minutes2)
            cheaters = []
            for key, value in end_dict.items():
                for i in value:
                    if i - start_dict[key] > 180:
                        if key not in cheaters:
                            cheaters.append(key)
            # print(cheaters)

cheaters()


with open('start_times.csv') as start_file:
    with open('submissions.csv') as subs_file:
        start_dict = {}
        end_dict = {}
        for line in start_file:
            parts1 = line.split(';')
            name1 = parts1[0]
            start_time = parts1[1].strip()
            start_time = datetime.strptime(start_time, '%H:%M').time()
            minutes = start_time.hour * 60 + start_time.minute
            start_dict[name1] = minutes
        
        for line in subs_file:
            parts2 = line.split(';')
            name2 = parts2[0]
            tasks = int(parts2[1])
            points = int(parts2[2])
            end_time = parts2[3].strip()
            end_time = datetime.strptime(end_time, '%H:%M').time()
            minutes2 = end_time.hour * 60 + end_time.minute
            if minutes2 - start_dict[name2] > 180:
                continue
            if name2 not in end_dict:
                end_dict[name2] = []
            found = False
            for i in end_dict[name2]:
                if i['task'] == tasks:
                    if points > i['points']:
                        i['points'] = points
                    found = True
                    break
            if found == False:
                end_dict[name2].append({'task':tasks, 'points':points})

        final_dict = {}
        for key, value in end_dict.items():
            if key not in final_dict:
                tot_points = 0
                final_dict[key] = tot_points
            for i in value:
                tot_points += i['points']
            final_dict[key] = tot_points
        # print(end_dict)
        print(final_dict)



                





