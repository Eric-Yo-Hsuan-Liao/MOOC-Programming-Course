
import json
import urllib.request

my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
data = my_request.read()
data = json.loads(data)


def retrieve_all():
    values = []
    for week in data:
        if week['enabled'] == True:
            values.append((week['fullName'], week['name'], week['year'], sum(week['exercises'])))
    for i in values:
        print(f"{i}")
    return values

# retrieve_all()

import math

def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = request.read()
    data = json.loads(data)
    answer_dict = {}
    student_nums = []
    tot_hours = 0
    tot_exercises = 0
    for week in data:
        answer_dict['weeks'] = len(data[week])
        student_nums.append(data[week]['students'])
        max_students = max(student_nums)
        answer_dict['students'] = max_students
        tot_hours += data[week]['hour_total']
        answer_dict['hours'] = tot_hours
        answer_dict['hours_average'] = math.floor(answer_dict['hours'] / answer_dict['students'])
        tot_exercises += data[week]['exercise_total']
        answer_dict['exercises'] = tot_exercises
        answer_dict['exercises_average'] = math.floor(answer_dict['exercises'] / answer_dict['students'])
    return print(answer_dict)

retrieve_course('docker2019')